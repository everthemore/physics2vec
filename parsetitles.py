import numpy as np
from helper import *
import argparse

parser = argparse.ArgumentParser(description="Parse titles into a *.npy file")
parser.add_argument('--input', type=str, required=True,
                   help='text file with titles from harvest')
parser.add_argument('--output', type=str, required=True,
                   help='output filename for *.npy file')

args = parser.parse_args()
inputfile = args.input
outputfile = args.output

print("Parsing file.. (make take a short while)")
all_titles = load_and_parse_all_titles(inputfile)
np.save(outputfile, all_titles)
print("Done!")
