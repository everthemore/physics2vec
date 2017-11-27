import numpy as np
import argparse
import gensim

parser = argparse.ArgumentParser(description="Ask a trained Word2Vec model some questions")
parser.add_argument('--input', type=str, required=True,
                   help='a trained model file')
parser.add_argument('--add', type=str, nargs='*', default="",
                   help='size of encoding vectors')
parser.add_argument('--subtract', type=str, nargs='*', default="",
                   help='size of window scanning over text')

args = parser.parse_args()
inputfile = args.input
positive = args.add
negative = args.subtract

# Load the model
model = gensim.models.Word2Vec.load(inputfile)

# Build a nicer query string
querystring = ""
for i in range(len(positive)):
    querystring = querystring + positive[i]

    if i < len(positive) - 1:
        querystring = querystring + " + "

if len(negative) != 0:
    querystring = querystring + " - "

for i in range(len(negative)):
    querystring = querystring + negative[i]

    if i < len(negative) - 1:
        querystring = querystring + " - "

print(querystring + " = \n")

# Get and display the answers
result = model.most_similar(positive=positive, negative=negative, topn=10)
for r in result:
	print("{0:40} (with similarity score {1})".format(r[0], r[1]))
print("\n")
