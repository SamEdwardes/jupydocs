---
id: numpydocstring.NumpyDocString
title: numpydocstring.NumpyDocString
---
Currently jupydocs works only with numpy doc strings. At this time some numpydoc strings may not work as expected because the library is still under development.

All markdown documentation below was generated using jupydocs.




## NumpyDocString

Convert function docstrings into markdown documentation.

### Attributes

| NAME                | TYPE   | DESCRIPTION   |
|:--------------------|:-------|:--------------|
| doc_index_          | list   | TBD           |
| description_        | tbd    | tbd           |
| function            | tbd    | tbd           |
| function_name       | tbd    | tbd           |
| docstring           | tbd    | tbd           |
| numpy_section_regex | tbd    | tbd           |
| docstring_split     | tbd    | tbd           |
| header_level        | tbd    | tbd           |

### Examples

Work in progress

### Methods
 - [NumpyDocString.__init__](#NumpyDocString__init__)
 - [NumpyDocString.create_doc_index](#NumpyDocStringcreate_doc_index)
 - [NumpyDocString.find_section](#NumpyDocStringfind_section)
 - [NumpyDocString.parse_code_blocks](#NumpyDocStringparse_code_blocks)
 - [NumpyDocString.parse_description](#NumpyDocStringparse_description)
 - [NumpyDocString.parse_generic](#NumpyDocStringparse_generic)
 - [NumpyDocString.parse_parameters](#NumpyDocStringparse_parameters)
 - [NumpyDocString.parse_returns](#NumpyDocStringparse_returns)
 - [NumpyDocString.render_class](#NumpyDocStringrender_class)
 - [NumpyDocString.render_md](#NumpyDocStringrender_md)

### NumpyDocString.__init__



#### Parameters

| NAME         | TYPE          | DESCRIPTION                                                                                                         |
|:-------------|:--------------|:--------------------------------------------------------------------------------------------------------------------|
| function     | [type]        | [description]                                                                                                       |
| header_level | str, optional | [description], by default '###'                                                                                     |
| custom_name  | None | str    | If None will use the functions name. If a string as provided will use the provided string instead of a custom name. |

### NumpyDocString.create_doc_index

Create an index of the docstring.

#### Returns

| TYPE   | DESCRIPTION                                                                                          |
|:-------|:-----------------------------------------------------------------------------------------------------|
| list   | A list of tuples, where each item in the list is a tuple with: (section_name, start_line, end_line). |

### NumpyDocString.find_section

A helper function that finds the section of docstring

#### Parameters

| NAME             | TYPE   | DESCRIPTION                                  |
|:-----------------|:-------|:---------------------------------------------|
| doc              | str    | The docstring to be parsed.                  |
| section_keywords | list   | A list of keywords that identify the section |

#### Returns

| TYPE       | DESCRIPTION                                                 |
|:-----------|:------------------------------------------------------------|
| (int, int) | A tuple with the start and end line of the desired section. |

### NumpyDocString.parse_code_blocks

Identify and clean up code blocks.

#### Parameters

| NAME   | TYPE   | DESCRIPTION                                                                            |
|:-------|:-------|:---------------------------------------------------------------------------------------|
| doc    | list   | The docstring in list format, where each item in the list is a line in the doc string. |

#### Returns

| TYPE   | DESCRIPTION                                                       |
|:-------|:------------------------------------------------------------------|
| list   | The docstring with code strings formatted for markdown rendering. |

### NumpyDocString.parse_description

Parse the description section of a docstring.

#### Returns

| TYPE   | DESCRIPTION   |
|:-------|:--------------|
| [type] | [description] |

### NumpyDocString.parse_generic

Parse generic sections

#### Parameters

| NAME     | TYPE   | DESCRIPTION   |
|:---------|:-------|:--------------|
| keywords | [type] | [description] |

#### Returns

| TYPE   | DESCRIPTION   |
|:-------|:--------------|
| [type] | [description] |

### NumpyDocString.parse_parameters

Parse the paramters section of a docstring.

#### Parameters

| NAME   | TYPE   | DESCRIPTION                             |
|:-------|:-------|:----------------------------------------|
| start  | int    | The starting line of docstring section. |
| end    | int    | The ending line of docstring section.   |

#### Returns

| TYPE   | DESCRIPTION                      |
|:-------|:---------------------------------|
| str    | A string in markdown formatting. |

### NumpyDocString.parse_returns

Parse the return section of a docstring

#### Parameters

| NAME     | TYPE   | DESCRIPTION   |
|:---------|:-------|:--------------|
| keywords | [type] | [description] |

#### Returns

| TYPE   | DESCRIPTION   |
|:-------|:--------------|
| [type] | [description] |

### NumpyDocString.render_class

Render an entire class into docstring markdown format

#### Parameters

| NAME       | TYPE           | DESCRIPTION                                                         |
|:-----------|:---------------|:--------------------------------------------------------------------|
| obj        | Class          | A python class object                                               |
| return_str | bool, optional | If true will return a string instead of markdown, by default False. |

#### Returns

| TYPE                            | DESCRIPTION                                       |
|:--------------------------------|:--------------------------------------------------|
| IPython.display.Markdown or str | The docstring rendered into markdown or a string. |

### NumpyDocString.render_md

Render the docstring into a markdown format.

#### Parameters

| NAME       | TYPE           | DESCRIPTION                                                         |
|:-----------|:---------------|:--------------------------------------------------------------------|
| return_str | bool, optional | If true will return a string instead of markdown, by default False. |

#### Returns

| TYPE                            | DESCRIPTION                                       |
|:--------------------------------|:--------------------------------------------------|
| IPython.display.Markdown or str | The docstring rendered into markdown or a string. |


