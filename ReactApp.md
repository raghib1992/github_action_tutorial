## Create React App
Install node JS
https://nodejs.org/en/

Create App using CLI
npx create-react-app react-app --use-npm

to start the app
npm run start

to test
npm run test

test with env variable
CI=true npm run test

statistics report f code coverage
CI=true npm run test -- --coverage

to build a package for production
npm run build

To test, deploy build on surge ( only static websites)

npm install --global surge

surge
project build_folder

Note down he domain nam
successful-battle.surge.sh

Install prettier (to check code analysis)

npm install --save-dev --save-exact prettier
npm install --global prettier

To check code (use npx when prettier is not install globally)
npx prettier --check "**/*.js"

To correct the format 
npx prettier --write "**/*.js"

Add in package.json
scripts{
    "format:check": "prettier --check \"**/*.{js,jsx,yml,yaml,json,css,scss,md}\""
}

npm run format:check