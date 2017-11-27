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

## Quickstart ##
If you're already familiar with python, all you need to have are the modules numpy, pyoai, inflect and gensim. These should all be easy to install using pip3. Then the workflow is as follows:
1. python3 arXivHarvest.py --section physics:cond-mat --output condmattitles.txt
2. python3 parsetitles.py --input condmattitles.txt --output condmattitles.npy
3. python3 trainmodel.py --input condmattitles.npy --size 100 --window 10 --mincount 5 --output condmatmodel-100-10-5
4. python3 askmodel.py --input condmatmodel-100-10-5 --add particle charge

In step 1, we get the titles from arXiv. This is a time-consuming step; it took 1.5hrs for the physics:cond-mat section, and so I've provided the files for those in the repository already (i.e. you can skip steps 1 and 2). In step 2 we take out the weird symbols etc, and parse it into a \*.npy file. In the third step, we train a model with vector size 100, window size 10 and minimum count for words to participate of 5. Step 4 can be repeated as often as one desires. 

## More details
Apart from the above scripts, I provide 3 python notebooks that perform more than just the analysis of arXiv titles. I highly 
recommend using notebooks. Very easy to install, and super useful. See here: http://jupyter.org/. You can also just copy-and-paste the code from the notebooks into a \*.py script and run those.

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
