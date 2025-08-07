# NodeJs app run locally in laptop
### Step 1: Download node js app locally
### Step 2: cd in to nodejs app folder
```sh
cd 03-second-action-react-demo
```
### Step 3: Install npm
```sh
npm install
```
### Step 3: Run app
```sh
npm run dev
```
### Step 5: Verify in browser
```sh
curl http://localhost:5173
```

# Multiple Job
### Parallel
```yml
name: Deploy Project
on: push
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - name: Get-code
        uses: actions/checkout@v3
      - name: Install NodeJS
        uses: actions/setup-node@v4
        with:
          node-version: 18
      - name: Install dependencies
        run: npm ci
      - name: Run test
        run: npm test
  deploy:
    runs-on: ubuntu-latest
    steps:
      - name: Get-code
        uses: actions/checkout@v3
      - name: Install NodeJS
        uses: actions/setup-node@v4
        with:
          node-version: 18
      - name: Install dependencies
        run: npm ci
      - name: Build Project
        run: npm run build
      - name: Deploy
        run: echo "deploying....."
```

### Workflow with multiple job run in sequential with multiple trigger
```yml
name: Deploy Project
on: [push, workflow_dispatch]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - name: Get-code
        uses: actions/checkout@v3
      - name: Install NodeJS
        uses: actions/setup-node@v4
        with:
          node-version: 18
      - name: Install dependencies
        run: npm ci
      - name: Run test
        run: npm test
  deploy:
    needs: test
    runs-on: ubuntu-latest
    steps:
      - name: Get-code
        uses: actions/checkout@v3
      - name: Install NodeJS
        uses: actions/setup-node@v4
        with:
          node-version: 18
      - name: Install dependencies
        run: npm ci
      - name: Build Project
        run: npm run build
      - name: Deploy
        run: echo "deploying....."
```

### Workflow with multiple triggers
```yml
name: Deploy Project
on: [push, workflow_dispatch]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - name: Get-code
        uses: actions/checkout@v3
      - name: Install NodeJS
        uses: actions/setup-node@v4
        with:
          node-version: 18
      - name: Install dependencies
        run: npm ci
      - name: Run test
        run: npm test
```