# Minify html files

Minify html using the minify html library
 

## Usage

### `workflow.yml` Example

Place in a `.yml` file such as this one in your `.github/workflows` folder. [Refer to the documentation on workflow YAML syntax here.](https://help.github.com/en/articles/workflow-syntax-for-github-actions)

```yaml
name: Minify Files

on:
  push:
    branches:
    - master

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@master
    - uses: docker://textadi/minifier-compressor-html-action:v2
      env:
        DIR: templates
        DESTINATION_DIR: minify_templates
        PARAM_MINIFY_CSS: False
        PARAM_MINIFY_JS: True
```

You can also use an image from the repository. 
To do this, specify `text-adi/minifier-compressor-html-action@v2` instead of `docker://textadi/minifier-compressor-html-action:v2`

### Configuration

| Key                                        | Value                                                                                                    | Suggested Type | Required | Default                            |
|--------------------------------------------|----------------------------------------------------------------------------------------------------------| ------------- |---------|------------------------------------|
| `DIR`                                      | Directory with html to be minified                                                                       | `env` | Yes     |                                    |
| `DESTINATION_DIR`                          | The directory where the minify files will be saved. If not set, the original html files will be minified | `env` | No      | The value from the `DIR` parameter |
| `PARAM_KEEP_CLOSING_TAGS`                  | The corresponding parameter in minifyhtml                                                                        | `env` | No      | False                              |
| `PARAM_KEEP_COMMENTS`                            | The corresponding parameter in minifyhtml                                                                        | `env` | No      | False                              |
| `PARAM_KEEP_HTML_AND_HEAD_OPENING_TAGS`          | The corresponding parameter in minifyhtml                                                                        | `env` | No      | False                              |
| `PARAM_KEEP_INPUT_TYPE_TEXT_ATTR`                | The corresponding parameter in minifyhtml                                                                        | `env` | No      | False                              |
| `PARAM_KEEP_SSI_COMMENTS`                        | The corresponding parameter in minifyhtml                                                                        | `env` | No      | False                              |
| `PARAM_MINIFY_CSS`                               | The corresponding parameter in minifyhtml                                                                        | `env` | No      | False                              |
| `PARAM_MINIFY_JS`                                | The corresponding parameter in minifyhtml                                                                        | `env` | No      | False                              |
| `PARAM_PRESERVE_BRACE_TEMPLATE_SYNTAX`           | The corresponding parameter in minifyhtml                                                                        | `env` | No      | False                              |
| `PARAM_PRESERVE_CHEVRON_PERCENT_TEMPLATE_SYNTAX` | The corresponding parameter in minifyhtml                                                                        | `env` | No      | False                              |
| `PARAM_REMOVE_BANGS`                             | The corresponding parameter in minifyhtml                                                                        | `env` | No      | False                              |
| `PARAM_REMOVE_PROCESSING_INSTRUCTIONS`           | The corresponding parameter in minifyhtml                                                                        | `env` | No      | False                              |
