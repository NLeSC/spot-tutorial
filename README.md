This repo contains the gitbook source files for the [SPOT](https://github.com/NLeSC/spot) tutorial. For the rendered gitbook, go [here](https://nlesc.github.io/spot-tutorial/tutorial/).

For development, follow these steps:

```bash
# get a copy of this repository
git clone https://github.com/NLeSC/spot-tutorial.git 
# change directory into the newly cloned repository
cd spot-tutorial
# create your own branch
git branch mybranch
# switch to your new branch
git checkout mybranch
# change into the directory holding the tutorial source files
cd src

# make your changes to the gitbook source files

# install the development dependencies (notably, tools to create a gitbook)
yarn install
# run the script named 'gitbook' to compile the gitbook from source
yarn run gitbook

# use a browser to navigate to _book/index.html to view the updated gitbook
# mv the updated gitbook to the /docs/tutorial directory so that they
# can be hosted on github.io / gh-pages
rm -rf ../docs/tutorial/* && mv _book/* ../docs/tutorial/

# don't forget to git add, git commit, and git push

```


