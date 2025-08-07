# Workflow
### Step 1: Create Repo in github, name: gh-first-action
### Step 2: Create workflow file 
- gh-first-action/.github/workflows/first-action.yml
```yml
name: First Workflow
# This workflow_dispatch used for manual trigger
on: workflow_dispatch
jobs:
  first-job:
    # Get the list of hosted runner 
    # https://docs.github.com/en/actions/using-github-hosted-runners/about-github-hosted-runners/about-github-hosted-runners
    runs-on: ubuntu-latest
    steps:
      - name: Print greeitng
        run: echo "Hello World"
      - name: Print goodbye
        run: echo "Good Bye"
      - name: multi line step
        run: |
          echo "First line"
          echo "Second Line"
```
### Step 3: Run workflow in Action tab