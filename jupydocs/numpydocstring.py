import pandas as pd
import re
from IPython.display import display, Markdown, Latex, HTML, display, IFrame

class NumpyDocString:
    
    
    
    def __init__(self, docstring):
        numpy_section_regex = re.compile(r'^[=\-`:\'"~^_*+#<>]{2,}\s*$')
        self.numpy_section_regex = re.compile(r'-{3,}')
        self.docstring_split = re.split(numpy_section_regex, docstring)
        
        self.docstring = docstring
        self.description_ = self.parse_description()
        self.parameters_ = self.parse_parameters()
        self.attributes = None
        self.examples = None
        self.keyword_arguments = None
        self.methods = None
        self.notes = None
        self.other_parameters = None
        self.returns = None
        self.raises = None
        self.references = None
        self.see_also = None
        self.todo = None
        self.warnings = None
        self.warns = None
        self.yields = None
        
        self.docstring_md_ = ''.join([
            self.description_,
            '\n',
            '## Parameters',
            '\n',
            self.parameters_.to_markdown(index=False)
        ])
    
    def render_md(self):
        return Markdown(self.docstring_md_)
        
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
        
    def parse_parameters(self):
        doc = self.docstring.split('\n')
        param_start = None
        param_end = None
        # find parameter section
        for idx, txt in enumerate(doc):
            if idx == 0:
                continue
            if re.match(self.numpy_section_regex, txt.strip()) and doc[idx - 1].strip().lower() in ['parameter', 'parameters', 'params', 'param']:
                param_start = idx - 1
                continue
            if param_start is not None and re.match(self.numpy_section_regex ,txt.strip()) is not None:
                param_end = idx - 2
                break
        
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
                description += ' ' + txt.strip()
                
        param_df['NAME'].append(name)
        param_df['TYPE'].append(type)
        param_df['DESCRIPTION'].append(description.strip())
        
        param_df = pd.DataFrame(param_df)
        return param_df
    
                
        
        

x = NumpyDocString(pd.DataFrame.__doc__)
x.docstring_md_
md = x.render_md()
md