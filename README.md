# physics2vec
Things to do with arXiv metadata :-)

## Summary
This repository is (currently) a collection of python scripts and notebooks that
1. Do a **Word2Vec encoding** of physics jargon (using gensim's CBOW or skip-gram, if you care for specifics).
   
   Examples: "particle + charge = electron" and "majorana + braiding = non-abelian"  
   Remark: These examples were _learned_ from the cond-mat section titles only.

2. Analyze the **n-grams** (i.e. fixed n-word expressions) in the titles over the years (what should we work on? ;-))
3. Produce a **WordCloud** of your favorite arXiv section (such as the above, from the cond-mat section)
![alt text](https://raw.githubusercontent.com/everthemore/physics2vec/master/caltechwordcloud.png "arXiv:cond-mat wordcloud")

## Notes
These scripts were tested and run using **Python 3**. I have not checked backwards compatibility.
Feel free to reach out to me in case things don't work out-of-the-box. I have not (yet) tried to make the scripts
and notebooks super user-friendly, though I did try to comment the code such that you may figure things out by
trial-and-error. 

## Pre-requisites
I currently only provide 3 python notebooks that perform the analysis of arXiv titles. Scripts might follow, but I highly 
recommend using notebooks. Very easy to install, and super useful. See here: http://jupyter.org/ If you really don't want to,
you can also just copy-and-paste the code from the notebooks into a \*.py script and run it.

You are going to need to following python modules in addition, all installable using pip3 (sudo pip3 install [module-name]).

1. numpy 

   Must-have for anything scientific you want to do with python (arrays, linalg)     
   Numpy (http://www.numpy.org/)
   
2. pyoai 

   Open Archive Initiaive module for querying the arXiv servers for metadata     
   https://pypi.python.org/pypi/pyoai
   
3. inflect
   
   Module for generating/checking plural/singular versions of words     
   https://pypi.python.org/pypi/inflect
   
4. gensim

   Very versatile module for topic modelling (analyzing basically anything you want from text, including word2vec)  
   https://radimrehurek.com/gensim/

Not required, but highly recommended is the module "matplotlib" for creating plots. You can comment/remove the
sections in the code that refer to it if you really don't want to. 

Optionally, if you wish to make a WordCloud, you will need

5. Matplotlib (https://matplotlib.org/)
6. PIL (http://www.pythonware.com/products/pil/)
7. WordCloud (https://github.com/amueller/word_cloud)


## How-To

1. **Optional**: run arXivHarvest.py to harvest titles and abstracts. Adjust the parameters at the top of 
this file (they are aptly named) if you wish to change the arXiv section and/or filenames. Beware, this script runs for
about 1.5hrs on the cond-mat subsection. 

   If you wish to just play with given data, alltitles.txt already contains the cond-mat titles. 
   Unfortunately, allabstracts.txt is too large to be uploaded (~200MB). 
   
2. Open one of the provided notebooks. Each will have a cell that loads&parses the titles text file you indicate, and then 
saves the parsed results in a .npy version. The parsing takes a couple of minutes, so saving it once and then re-loading
(by setting reparse = False) saves some time.

