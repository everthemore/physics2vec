import numpy as np
import argparse
from helper import *

parser = argparse.ArgumentParser(description="Train a Word2Vec encoding on input, and store the resulting model in output")
parser.add_argument('--input', type=str, required=True,
                   help='a *.npy file with parsed titles')
parser.add_argument('--size', type=int, default=100,
                   help='size of encoding vectors')
parser.add_argument('--window', type=int, default=10,
                   help='size of window scanning over text')
parser.add_argument('--mincount', type=int, default=5,
                   help='minimum number of times a word has to appear to participate')
parser.add_argument('--output', type=str, required=True,
                   help='output filename for saving the model')

args = parser.parse_args()
inputfile = args.input
size = args.size
window = args.window
mincount = args.mincount
outputfile = args.output

print("Training model with\n")
print("{0:30} = {1}".format("input", inputfile))
print("{0:30} = {1}".format("size", size))
print("{0:30} = {1}".format("window", window))
print("{0:30} = {1}".format("mincount", mincount))

all_titles = np.atleast_2d(np.load(inputfile))[0][0]
all_years = sorted(list(all_titles.keys()))
titles = get_titles_for_years(all_titles, all_years)
ngram_titles, bigrams, ngrams = get_ngrams(titles)
model = gensim.models.Word2Vec(ngram_titles, window=window, min_count=mincount, size=size)
print("Saving to {0}".format(outputfile))
model.save(outputfile)
print("Done!")
