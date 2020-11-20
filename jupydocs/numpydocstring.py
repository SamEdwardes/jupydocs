import re

from tabulate import tabulate

from IPython.display import Markdown

# TODO: fix render_methods so that it a returns in table format

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
    doc_index_ : list
        TBD
    description_ : tbd
        tbd
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
        
    Methods
    -------
    Work in progress
        
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
        # record keywords
        self.section_keywords_mapping = {
            'parameters': (['parameter', 'parameters', 'params', 'param'], self.parse_parameters),
            'attributes': (['attribute', 'attributes'], self.parse_parameters),
            'examples': (['example', 'examples'], self.parse_generic),
            'returns': (['return', 'returns'], self.parse_returns),
            'yields': (['yields', 'yield'], self.parse_returns),
            'raises': (['raises'], self.parse_generic),
            'notes': (['note'], self.parse_generic),
            'references': (['reference', 'references'], self.parse_generic),
            'keyword_arguments': (['keyword', 'kward'], self.parse_generic),
            'methods': (['methods'], self.parse_generic),
            'see_also': (['see also'], self.parse_generic),
            'todo': (['to do'], self.parse_generic),
            'warnings': (['warning',  'warns'], self.parse_generic),
        }
        # create an index of all docstring sections
        self.doc_index_ = self.create_doc_index()
        self.description_ = self.parse_description()
        
    def create_doc_index(self):
        """Create an index of the docstring.

        Returns
        -------
        list
            A list of tuples, where each item in the list is a tuple with:
            (section_name, start_line, end_line).
        """
        doc = self.docstring
        doc = doc.split('\n')
        # identify the starting index of each section
        doc_index = []
        for idx, txt in enumerate(doc):
            if re.match(self.numpy_section_regex, txt.strip()):
                doc_index.append([doc[idx - 1].strip(), idx - 1, None])
        # identify the end index of each section
        for idx, x in enumerate(doc_index):
            if idx < len(doc_index) - 1:
                doc_index[idx][2] = doc_index[idx+1][1]
            else:
                doc_index[idx][2] = len(doc) - 1
            doc_index[idx] = tuple(doc_index[idx])
        self.doc_index_ = doc_index
        return doc_index
    
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
        docstring_sections = [
            f'{self.header_level[0:-1]} {self.function_name}\n\n',
            self.description_,
        ]        
        for section_name, start, end in self.doc_index_:
            for keywords, func in self.section_keywords_mapping.values():
                if section_name.strip().lower() in keywords:
                    txt = func(start, end)
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
        
    def parse_parameters(self, start, end):
        """Parse the paramters section of a docstring.

        Parameters
        ----------
        start : int
            The starting line of docstring section.
        end : int
            The ending line of docstring section.

        Returns
        -------
        str
            A string in markdown formatting.
        """
        doc = self.docstring.split('\n')  
        header = doc[start].strip()
        # parse paramters into dataframe
        doc = doc[start+2:end]
        param_table = {'NAME': [], 'TYPE': [], 'DESCRIPTION': []}
        name, param_type, description = None, None, None
        for idx, txt in enumerate(doc):
            if ' : ' in txt:
                if name is None:
                    pass
                else:
                    param_table['NAME'].append(name)
                    param_table['TYPE'].append(param_type)
                    param_table['DESCRIPTION'].append(description.strip())
                name, param_type = txt.strip().split(' : ')
                description = ''
                continue
            else:
                if txt.strip() == '' and idx < len(doc) - 1:
                    txt = '<br></br>'                
                description += ' ' + txt.strip()  
        param_table['NAME'].append(name)
        param_table['TYPE'].append(param_type)
        param_table['DESCRIPTION'].append(description.strip())
        param_md = tabulate(param_table, headers='keys', tablefmt="pipe")
        param_md = f'\n\n{self.header_level} {header}\n\n' + param_md
        return param_md
    
    def parse_returns(self, start, end):
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
        for idx, txt in enumerate(doc[1:]):
            txt = txt.strip()
            if txt == '' and idx < len(doc) - 2:
                txt = '<br></br>'
            else:
                txt = txt
            description.append(txt)
        description = ' '.join(description)
        param_table = {'NAME': [], 'TYPE': [], 'DESCRIPTION': []}
        if name is not None:
            param_table['NAME'].append(name)
        else:
            param_table.pop('NAME', None)
        param_table['TYPE'].append(param_type),
        param_table['DESCRIPTION'].append(description)
        out = f'\n\n{self.header_level} {header}\n\n' 
        out += tabulate(param_table, headers='keys', tablefmt="pipe")
        return out
            
    def parse_generic(self, start, end):
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
    
    
def render_class(obj, header_level='###', render_class_doc_string=True, render_init=False, return_str=False):
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
    if render_class_doc_string:
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
        
    
            
# ============================================================================
# testing
# ============================================================================

def custom_sum(x, y):
    """A new take on the class `sum` function.
    
    Does 1 + 1 always need to equal 2? Not anymore! Thanks to the `custom_sum`
    function 1 + 1 will never equal 2 again.

    Parameters
    ----------
    x : float
        A number.
    y : float
        A number.

    Returns
    -------
    num : Float
        A new take on the traditional sum function. x * 2 + y * 3. Not at all
        useful. But fun!
        
    Example
    -------
    >>> from examplepackage.example import custom_sum
    >>> custom_sum(2, 3)
    13
    
    See also
    --------
    You should normally use the regular python `sum` function. `custom_sum` is
    almost never useful!
    
    """
    return x * 2 + y * 3


# doc_string = NumpyDocString(custom_sum)
# print(doc_string.doc_index_)
# doc_string.render_md()