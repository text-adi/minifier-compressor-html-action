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
    - uses: docker://textadi/minifier-compressor-html-action:v1
      env:
        DIR: templates
        DIR: minify_templates
```

You can also use an image from the repository. 
To do this, specify `text-adi/minifier-compressor-html-action@v1` instead of `docker://textadi/minifier-compressor-html-action:v1`

### Configuration

| Key | Value                                                                                                      | Suggested Type | Required | Default                    |
| ------------- |------------------------------------------------------------------------------------------------------------| ------------- |---------|----------------------------|
| `DIR` | Directory with html to be minified                                                                         | `env` | Yes     |                            |
| `DESTINATION_DIR` | The directory where the minify files will be saved. If not set, the original html files will be minified | `env` | No      | The value from the `DIR` parameter |