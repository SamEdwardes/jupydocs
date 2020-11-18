---
id: numpydocstring
title: NumpyDocString
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
| function            | tbd    | tbd           |
| function_name       | tbd    | tbd           |
| docstring           | tbd    | tbd           |
| numpy_section_regex | tbd    | tbd           |
| docstring_split     | tbd    | tbd           |
| header_level        | tbd    | tbd           |
| description_        | tbd    | tbd           |
| parameters_         | tbd    | tbd           |
| attributes_         | tbd    | tbd           |
| examples_           | tbd    | tbd           |
| returns_            | tbd    | tbd           |
| yields_             | tbd    | tbd           |
| raises_             | tbd    | tbd           |
| notes_              | tbd    | tbd           |
| references_         | tbd    | tbd           |
| keyword_arguments_  | tbd    | tbd           |
| methods_            | tbd    | tbd           |
| see_also_           | tbd    | tbd           |
| todo_               | tbd    | tbd           |
| warnings_           | tbd    | tbd           |

### Examples


Work in progress


### Methods

### find_section

A helper function that finds the section of docstring

#### Parameters

| NAME             | TYPE   | DESCRIPTION                                  |
|:-----------------|:-------|:---------------------------------------------|
| doc              | str    | The docstring to be parsed.                  |
| section_keywords | list   | A list of keywords that identify the section |

#### Returns

| TYPE       | DESCRIPTION                                                           |
|:-----------|:----------------------------------------------------------------------|
| (int, int) | A tuple with the start and end line of the desired section. <br></br> |

### parse_code_blocks

Identify and clean up code blocks.

#### Parameters

| NAME   | TYPE   | DESCRIPTION                                                                            |
|:-------|:-------|:---------------------------------------------------------------------------------------|
| doc    | list   | The docstring in list format, where each item in the list is a line in the doc string. |

#### Returns

| TYPE   | DESCRIPTION                                                                 |
|:-------|:----------------------------------------------------------------------------|
| list   | The docstring with code strings formatted for markdown rendering. <br></br> |

### parse_description

Parse the description section of a docstring.

#### Returns

| TYPE   | DESCRIPTION             |
|:-------|:------------------------|
| [type] | [description] <br></br> |

### parse_generic

Parse generic sections

#### Parameters

| NAME     | TYPE   | DESCRIPTION   |
|:---------|:-------|:--------------|
| keywords | [type] | [description] |

#### Returns

| TYPE   | DESCRIPTION             |
|:-------|:------------------------|
| [type] | [description] <br></br> |

### parse_parameters

Parse the paramters section of a docstring.

#### Parameters

| NAME     | TYPE   | DESCRIPTION   |
|:---------|:-------|:--------------|
| keywords | [type] | [description] |

#### Returns

| TYPE   | DESCRIPTION             |
|:-------|:------------------------|
| [type] | [description] <br></br> |

### parse_returns

Parse the return section of a docstring

#### Parameters

| NAME     | TYPE   | DESCRIPTION   |
|:---------|:-------|:--------------|
| keywords | [type] | [description] |

#### Returns

| TYPE   | DESCRIPTION             |
|:-------|:------------------------|
| [type] | [description] <br></br> |

### render_md

Render the docstring into a markdown format.

#### Parameters

| NAME       | TYPE           | DESCRIPTION                                                         |
|:-----------|:---------------|:--------------------------------------------------------------------|
| return_str | bool, optional | If true will return a string instead of markdown, by default False. |

#### Returns

| TYPE                            | DESCRIPTION                                                 |
|:--------------------------------|:------------------------------------------------------------|
| IPython.display.Markdown or str | The docstring rendered into markdown or a string. <br></br> |






## render_class

Render an entire class into docstring markdown format

### Parameters

| NAME       | TYPE           | DESCRIPTION                                                         |
|:-----------|:---------------|:--------------------------------------------------------------------|
| obj        | Class          | A python class object                                               |
| return_str | bool, optional | If true will return a string instead of markdown, by default False. |

### Returns

| TYPE                            | DESCRIPTION                                                 |
|:--------------------------------|:------------------------------------------------------------|
| IPython.display.Markdown or str | The docstring rendered into markdown or a string. <br></br> |


