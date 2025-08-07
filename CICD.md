List of Branches:
1. master (deploy to prod server)
2. developer (lastest code)
3. feature1 (developer work on this to add new code)

Workflow
1. feature1 --> pull request --> workflow --> Approval --> developer
    - Install dependencies
    - check code formatting
    - run automated test
    - upload code coverage as an Artifacts
    - cache dependencies

2. developer --> workflow --> Staging
    - Install dependencies
    - check code formatting
    - run automated test
    - upload code coverage as an Artifacts
    - Build Project
    - Upload build as an Artifacts
    - deploy to Staging server
    - cache dependencies

3. developer --> pull request--> workflow --> master
    - Install dependencies
    - check code formatting
    - run automated test
    - upload code coverage as an Artifacts
    - cache dependencies

4. master --> workflow --> prod
    - Install dependencies
    - check code formatting
    - run automated test
    - upload code coverage as an Artifacts
    - Build Project
    - Upload build as an Artifacts
    - create a release
    - deploy to Production server
    - upload coverage to codeCov

Job Failure --> Create Issues
Issue created --> Slack Message
Release created --> slack Message

**************************************************

## Branch Protection Rule
setting --> Branches
master
Required Pull request reviews before merging
    - Dismiss stale pull request approvals when new commits are pushed
    - required review from code owners
Required status check to pass before merging
    - Required branches to be up to date before merging
Include Administrator


*************************************************
## Create new branch
git checkout -b workflow

## Create new workflow for staging environment
```
name: CI

on:
  pull_request:
    branches: [develop]
  push:
    branches:
      - "develop"

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - uses: actions/cache@v3
        with:
          path: ~/.npm
          # https://github.com/actions/cache/blob/main/examples.md#node---npm
          key: ${{ runner.os }}-node-${{ hashFiles('**/package-lock.json') }}
          restore-keys: |
            ${{ runner.os }}-node-
      - name: Use NodeJS
        uses: actions/setup-node@v1
        with:
          node-version: "12.x"
      - name: Install node js by command install or CI
        run: npm ci 
      - run: npm run format:check
      - run: npm test -- --coverage 
        env:
          CI: true
      - name: Upload test Coverage
        uses: actions/upload-artifact@v3
        with:
          name: code-coverage
          path: coverage
      - uses: actions/download-artifact@v3
        with:
          name: code-coverage
      - name: build Project
        if: github.event_name == 'push'
        run: npm run build
      - name: Upload Build Folder
        if: github.event_name == 'push'
        uses: actions/upload-artifact@v3
        # https://github.com/actions/upload-artifact
        with:
          name: build
          path: build
      - uses: actions/download-artifact@v3
        if: github.event_name == 'push'
        with:
          name: build
        # if: github.event_name == 'push'
        #with:
      - name: deploy to staging
        if: github.event_name == 'push'
        run:  npx surge --project ./build --domain successful-battle.surge.sh
        env:
          SURGE_LOGIN: ${{ secrets.surge_login }}
          # to generate the token 'surge token'
          SURGE_TOKEN: ${{ secrets.surge_token }}
          # to know the the login id 'surge whoami'
```
************************************************
## Semantic Versioning

2.1.3
2 major Version (some breaking changes)
1 minor version (new features, non breaking functionality)
3 bug fixing

*************************************************

## Conventional Commits
type <fix feature>
scope <optional>
description <>
eg- fix change cart endpoint closes issue#12
    fear: added Facebook authentication

### Install semantic release
https://github.com/semantic-release/semantic-release/blob/master/docs/usage/installation.md
npm install --save-dev semantic-release
vi release.config.js
```
module.exports = {
    branches: "master",
    repositoryUrl: https://github.com/raghib1992/react-app, 
    plugins: ['@semantic-release/commit-analyzer', '@semantic-release/release-notes-generator', '@semantic-release/npm', '@semantic-release/github']
}
```
npx semantic-release