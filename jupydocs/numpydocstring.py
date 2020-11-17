import pandas as pd
import re
from IPython.display import display, Markdown, Latex, HTML, display, IFrame

class NumpyDocString:
    
    def __init__(self, function, header_level='###'):
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
        self.attributes = self.parse_parameters(['attribute', 'attributes'])
        self.examples_ = self.parse_examples(['example', 'examples'])
        self.keyword_arguments = None
        self.methods_ = None
        self.notes_ = None
        self.other_parameters = None
        self.returns_ = self.parse_returns(['return', 'returns'])
        self.raises_ = None
        self.references_ = None
        self.see_also_ = None
        self.todo_ = None
        self.warnings_ = None 
        self.warns_ = None
        self.yields_ = None
    
    def render_md(self, return_str=False):
        docstring_sections = []
        for txt in [
            f'{self.header_level[0:-1]} {self.function_name}\n\n',
            self.description_, 
            self.parameters_, 
            self.returns_,
            self.examples_
        ]:
            if txt is not None:
                docstring_sections.append(txt)
        docstring_md = ''.join(docstring_sections)
        if return_str:
            return docstring_md
        else:
            return Markdown(docstring_md)
        
    def parse_description(self):
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
        param_start, param_end = self.find_section(self.docstring, keywords)
        if param_start is None:
            return None
        doc = self.docstring.split('\n')  
        # parse paramters into dataframe
        param_list = doc[param_start:param_end]
        param_df = {'NAME': [], 'TYPE': [], 'DESCRIPTION': []}
        name, type, description = None, None, None
        for idx, txt in enumerate(param_list):
            if idx == 0 or idx == 1:
                continue
            elif ' : ' in txt:
                if name is None:
                    pass
                else:
                    param_df['NAME'].append(name)
                    param_df['TYPE'].append(type)
                    param_df['DESCRIPTION'].append(description.strip())
                name, type = txt.strip().split(' : ')
                description = ''
                continue
            else:
                if txt.strip() == '':
                    txt = '<br><br>'                
                description += ' ' + txt.strip()  
        param_df['NAME'].append(name)
        param_df['TYPE'].append(type)
        param_df['DESCRIPTION'].append(description.strip())
        param_md = pd.DataFrame(param_df).to_markdown(index=False)
        param_md = f'\n\n{self.header_level} Parameters\n\n' + param_md
        return param_md
    
    def parse_returns(self, keywords):
        start, end = self.find_section(self.docstring, keywords)
        if start is None:
            return None
        doc = self.docstring.split('\n')
        doc = doc[start+2:end]
        doc = '\n'.join(doc)
        doc = f'\n\n{self.header_level} Returns\n\n' + doc
        return doc
            
    def parse_examples(self, keywords):
        start, end = self.find_section(self.docstring, keywords)
        if start is None:
            return None
        doc = self.docstring.split('\n')
        doc = doc[start+2:end]
        doc = self.parse_code_blocks(doc)
        doc = '\n'.join(doc)
        doc = f'\n\n{self.header_level} Examples\n\n' + doc
        return doc
           
    def parse_code_blocks(self, doc):
        clean_doc = []
        inside_code_block = False
        for idx, txt in enumerate(doc):
            txt = txt.strip()
            if txt[0:3] == '>>>' or txt[0:3] == '...':
                if inside_code_block == False:
                    txt = '```python\n' + txt
                inside_code_block = True
            elif (txt == '' and inside_code_block == True) or (idx == len(doc)-1):
                inside_code_block = False
                txt = txt + '\n```\n'
            else:
                txt = txt
            clean_doc.append(txt)
        return clean_doc
    
    def find_section(self, doc, section_keywords):
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
    Float
        x * 2 + y * 3
        
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

docstring = NumpyDocString(custom_sum)
docstring.render_md(True)