# link
- github action context: *https://docs.github.com/en/actions/learn-github-actions/contexts*
- github action function: *https://docs.github.com/en/actions/learn-github-actions/expressions*

```yml
name: Output Information
on: [push,worflow_dispatch]
jobs:
  info:
    runs-on: ubuntu-latest
    steps:
      - name: Output Github Context
        run: echo "${{ toJSON(github) }}"
        # github is metadata and to make it readable use toJSON
        # ${{ }}, this is a function used to make github to not read as plain text
```