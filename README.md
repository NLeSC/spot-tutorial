# spot-tutorial

This repo contains the gitbook source files for the SPOT tutorial. 

For development, follow these steps:

```bash
git clone https://github.com/NLeSC/spot-tutorial.git 
cd spot-tutorial
git branch mybranch
git checkout mybranch
cd src
yarn install
yarn run gitbook
rm -rf ../docs/tutorial/* && mv _book/* ../docs/tutorial/

```


