---
id: module_numpydocstring
title: numpydocstring module
---
Currently jupydocs works only with numpy doc strings. At this time some numpydoc strings may not work as expected because the library is still under development.




## NumpyDocString

Convert function docstrings into markdown documentation.

### Parameters

| NAME         | TYPE          | DESCRIPTION                                                    |
|:-------------|:--------------|:---------------------------------------------------------------|
| function     | function      | A python function that has been documented using numpy styling |
| header_level | str, optional | [description], by default '##'                                 |

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

### Methods

Work in progress


### Examples

Work in progress



## NumpyDocString methods




### create_doc_index

Create an index of the docstring.

#### Returns

| TYPE   | DESCRIPTION                                                                                          |
|:-------|:-----------------------------------------------------------------------------------------------------|
| list   | A list of tuples, where each item in the list is a tuple with: (section_name, start_line, end_line). |

### find_section

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

### parse_code_blocks

Identify and clean up code blocks.

#### Parameters

| NAME   | TYPE   | DESCRIPTION                                                                            |
|:-------|:-------|:---------------------------------------------------------------------------------------|
| doc    | list   | The docstring in list format, where each item in the list is a line in the doc string. |

#### Returns

| TYPE   | DESCRIPTION                                                       |
|:-------|:------------------------------------------------------------------|
| list   | The docstring with code strings formatted for markdown rendering. |

### parse_description

Parse the description section of a docstring.

#### Returns

| TYPE   | DESCRIPTION   |
|:-------|:--------------|
| [type] | [description] |

### parse_generic

Parse generic sections

#### Parameters

| NAME     | TYPE   | DESCRIPTION   |
|:---------|:-------|:--------------|
| keywords | [type] | [description] |

#### Returns

| TYPE   | DESCRIPTION   |
|:-------|:--------------|
| [type] | [description] |

### parse_parameters

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

### parse_returns

Parse the return section of a docstring

#### Parameters

| NAME     | TYPE   | DESCRIPTION   |
|:---------|:-------|:--------------|
| keywords | [type] | [description] |

#### Returns

| TYPE   | DESCRIPTION   |
|:-------|:--------------|
| [type] | [description] |

### render_md

Render the docstring into a markdown format.

#### Parameters

| NAME       | TYPE           | DESCRIPTION                                                         |
|:-----------|:---------------|:--------------------------------------------------------------------|
| return_str | bool, optional | If true will return a string instead of markdown, by default False. |

#### Returns

| TYPE                            | DESCRIPTION                                       |
|:--------------------------------|:--------------------------------------------------|
| IPython.display.Markdown or str | The docstring rendered into markdown or a string. |






## render_class

Render an entire class into docstring markdown format

### Parameters

| NAME       | TYPE           | DESCRIPTION                                                         |
|:-----------|:---------------|:--------------------------------------------------------------------|
| obj        | Class          | A python class object                                               |
| return_str | bool, optional | If true will return a string instead of markdown, by default False. |

### Returns

| TYPE                            | DESCRIPTION                                       |
|:--------------------------------|:--------------------------------------------------|
| IPython.display.Markdown or str | The docstring rendered into markdown or a string. |


