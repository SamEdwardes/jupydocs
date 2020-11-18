import re

import pandas as pd
from IPython.display import Markdown

# TODO: fix render methods so that it a returns in table format

class NumpyDocString:
    """Convert function docstrings into markdown documentation.
    
    Parameters
    ----------
    function : function
        A python function that has been documented using numpy styling
    header_level : str, optional
        [description], by default '##'
        
    Attributes
    ----------
    function : tbd
        tbd
    function_name : tbd
        tbd
    docstring : tbd
        tbd
    numpy_section_regex : tbd
        tbd
    docstring_split : tbd
        tbd
    header_level : tbd
        tbd
    description_ : tbd
        tbd
    parameters_ : tbd
        tbd
    attributes_ : tbd
        tbd
    examples_ : tbd
        tbd
    returns_ : tbd
        tbd
    yields_ : tbd
        tbd
    raises_ : tbd
        tbd
    notes_ : tbd
        tbd
    references_ : tbd
        tbd
    keyword_arguments_ : tbd
        tbd
    methods_ : tbd
        tbd
    see_also_ : tbd
        tbd
    todo_ : tbd
        tbd
    warnings_ : tbd
        tbd
        
    Examples
    --------
    
    Work in progress
    """
    
    def __init__(self, function, header_level='###'):
        """[summary]

        Parameters
        ----------
        function : [type]
            [description]
        header_level : str, optional
            [description], by default '###'
        """
        # boilderplate
        self.function = function
        self.function_name = function.__name__
        self.docstring = function.__doc__
        numpy_section_regex = re.compile(r'^[=\-`:\'"~^_*+#<>]{2,}\s*$')
        self.numpy_section_regex = re.compile(r'-{3,}')
        self.docstring_split = re.split(numpy_section_regex, self.docstring)
        self.header_level = header_level
        # docstring sections
        self.description_ = self.parse_description()
        self.parameters_ = self.parse_parameters(['parameter', 'parameters', 'params', 'param'])
        self.attributes_ = self.parse_parameters(['attribute', 'attributes'])
        self.examples_ = self.parse_generic(['example', 'examples'])
        self.returns_ = self.parse_returns(['return', 'returns'])
        self.yields_ = self.parse_returns(['yields', 'yield'])
        self.raises_ = self.parse_generic(['raises'])
        self.notes_ = self.parse_generic(['note'])
        self.references_ = self.parse_generic(['reference', 'references'])
        self.keyword_arguments_ = self.parse_generic(['keyword', 'kward'])
        self.methods_ = self.parse_generic(['methods'])
        self.see_also_ = self.parse_generic(['see also'])
        self.todo_ = self.parse_generic(['to do'])
        self.warnings_ = self.parse_generic(['warning',  'warns']) 
    
    def render_md(self, return_str=False):
        """Render the docstring into a markdown format.

        Parameters
        ----------
        return_str : bool, optional
            If true will return a string instead of markdown, by default False.

        Returns
        -------
        IPython.display.Markdown or str
            The docstring rendered into markdown or a string.
        """
        docstring_sections = []
        for txt in [
            f'{self.header_level[0:-1]} {self.function_name}\n\n',
            self.description_,
            self.parameters_,
            self.attributes_,
            self.examples_,
            self.returns_,
            self.yields_,
            self.raises_,
            self.notes_,
            self.references_,
            self.keyword_arguments_,
            self.methods_,
            self.see_also_,
            self.todo_,
            self.warnings_,
        ]:
            if txt is not None:
                docstring_sections.append(txt)
        docstring_md = ''.join(docstring_sections)
        if return_str:
            return docstring_md
        else:
            return Markdown(docstring_md)
        
    def parse_description(self):
        """Parse the description section of a docstring.

        Returns
        -------
        [type]
            [description]
        """
        doc = self.docstring.split('\n')
        param_start = 0
        param_end = None
        # find parameter section
        for idx, txt in enumerate(doc):
            if idx == 0:
                continue
            if param_start is not None and re.match(self.numpy_section_regex ,txt.strip()) is not None:
                param_end = idx - 2
                break  
        description = doc[param_start:param_end]
        description = [x.strip() for x in description]
        description = ['\n\n' if x == '' else x + ' ' for x in description]
        description = ''.join(description).strip()
        return description
        
    def parse_parameters(self, keywords):
        """Parse the paramters section of a docstring.

        Parameters
        ----------
        keywords : [type]
            [description]

        Returns
        -------
        [type]
            [description]
        """
        start, end = self.find_section(self.docstring, keywords)
        if start is None:
            return None
        doc = self.docstring.split('\n')  
        header = doc[start].strip()
        # parse paramters into dataframe
        doc = doc[start+2:end]
        param_df = {'NAME': [], 'TYPE': [], 'DESCRIPTION': []}
        name, param_type, description = None, None, None
        for idx, txt in enumerate(doc):
            if ' : ' in txt:
                if name is None:
                    pass
                else:
                    param_df['NAME'].append(name)
                    param_df['TYPE'].append(param_type)
                    param_df['DESCRIPTION'].append(description.strip())
                name, param_type = txt.strip().split(' : ')
                description = ''
                continue
            else:
                if txt.strip() == '':
                    txt = '<br></br>'                
                description += ' ' + txt.strip()  
        param_df['NAME'].append(name)
        param_df['TYPE'].append(param_type)
        param_df['DESCRIPTION'].append(description.strip())
        param_md = pd.DataFrame(param_df).to_markdown(index=False)
        param_md = f'\n\n{self.header_level} {header}\n\n' + param_md
        return param_md
    
    def parse_returns(self, keywords):
        """Parse the return section of a docstring

        Parameters
        ----------
        keywords : [type]
            [description]

        Returns
        -------
        [type]
            [description]
        """
        start, end = self.find_section(self.docstring, keywords)
        if start is None:
            return None
        doc = self.docstring.split('\n')
        header= doc[start].strip()
        doc = doc[start+2:end]
        name, param_type, description = None, None, None
        first_line = doc[0].strip().split(' : ')
        if len(first_line) == 2:
            name = first_line[0] 
            param_type = first_line[1]
        else:
            name = None
            param_type = first_line[0]
        description = []
        for txt in doc[1:]:
            txt = txt.strip()
            if txt == '':
                txt = '<br></br>'
            else:
                txt = txt
            description.append(txt)
        description = ' '.join(description)
        df = pd.DataFrame()
        if name is not None:
            df['NAME'] = [name]
        df['TYPE'] = param_type,
        df['DESCRIPTION'] = description
        out = f'\n\n{self.header_level} {header}\n\n' 
        out += df.to_markdown(index=False)
        return out
            
    def parse_generic(self, keywords):
        """Parse generic sections

        Parameters
        ----------
        keywords : [type]
            [description]

        Returns
        -------
        [type]
            [description]
        """
        start, end = self.find_section(self.docstring, keywords)
        if start is None:
            return None
        doc = self.docstring.split('\n')
        header = doc[start].strip()
        doc = doc[start+2:end]
        doc = self.parse_code_blocks(doc)
        doc = '\n'.join(doc)
        doc = f'\n\n{self.header_level} {header}\n\n' + doc
        return doc
           
    def parse_code_blocks(self, doc):
        """Identify and clean up code blocks.

        Parameters
        ----------
        doc : list
            The docstring in list format, where each item in the list is a line
            in the doc string.

        Returns
        -------
        list
            The docstring with code strings formatted for markdown rendering.
        """
        clean_doc = []
        inside_code_block = False
        for idx, txt in enumerate(doc):
            txt = txt.strip()
            if txt[0:3] == '>>>' or txt[0:3] == '...':
                if inside_code_block == False:
                    txt = '```python\n' + txt
                inside_code_block = True
            elif (txt == '' and inside_code_block == True) or (idx == len(doc)-1 and inside_code_block == True):
                inside_code_block = False
                txt = txt + '\n```\n'
            else:
                txt = txt
            clean_doc.append(txt)
        return clean_doc
    
    def find_section(self, doc, section_keywords):
        """A helper function that finds the section of docstring

        Parameters
        ----------
        doc : str
            The docstring to be parsed.
        section_keywords : list
            A list of keywords that identify the section

        Returns
        -------
        (int, int)
            A tuple with the start and end line of the desired section.
        """
        doc = self.docstring.split('\n')
        section_start = None
        section_end = None
        for idx, txt in enumerate(doc):
            if idx == 0:
                continue
            if re.match(self.numpy_section_regex, txt.strip()) and doc[idx - 1].strip().lower() in section_keywords:
                section_start = idx - 1
                continue
            if section_start is not None and re.match(self.numpy_section_regex ,txt.strip()) is not None:
                section_end = idx - 2
                break
        return section_start, section_end
    
    
def render_class(obj, header_level='###', render_init=False, return_str=False):
    """Render an entire class into docstring markdown format

    Parameters
    ----------
    obj : Class
        A python class object
    return_str : bool, optional
        If true will return a string instead of markdown, by default False.

    Returns
    -------
    IPython.display.Markdown or str
        The docstring rendered into markdown or a string.
    """
    if render_init:
        methods = ['__init__']
    else:
        methods = []
    for x in dir(obj):
        if x[0:2] != '__' and x[-2] != '__':
            methods.append(x)       
    docstring = []
    docstring.append(NumpyDocString(obj, header_level).render_md(True))
    docstring.append(f'{header_level} Methods')
    for method in methods:
        doc = NumpyDocString(getattr(obj, method), header_level + '#')
        doc = doc.render_md(True)
        docstring.append(doc) 
    docstring = '\n\n'.join(docstring)
    if return_str:
        return docstring
    else:
        return Markdown(docstring)
        
    
            
