#--------------------------------------------------------------------
# arXivHarvest.py
#
# Harvests (using OAI metadata available through an arXiv URL)
# the titles and abstracts of a given arXiv section (cond-mat,
# quant-ph, etc). 
#
# The result of running this script will be two .txt files,
# one containing the titles, and the other the corresponding
# abstracts.
#
# The title.txt file is structured as (example):
# 2017 3 This is the title of a paper published in 2017
#   that was too long to fit on a single line, so it con-
#   tinues with two whitespaces on the next line
# 1998 12 This one is older but has a much shorter title
#
# The abstract.txt file has no year/month information, and
# is ordered the same way as the title.txt file (so first
# abstract belongs to the first title, etc).
#--------------------------------------------------------------------
# Import modules
from oaipmh.client import Client
from oaipmh.metadata import MetadataRegistry, MetadataReader
import time

# Change this to harvest a different arXiv set
section="physics:cond-mat"
# And change these to specify the txt file to save the data in
title_file = "all_cond_mat_titles.txt"
abstr_file = "all_cond_mat_abstracts.txt"

# Create a new MetadataReader, and list just the fields we are interested in
oai_dc_reader = MetadataReader(
    fields={
    'title':       ('textList', 'oai_dc:dc/dc:title/text()'),
    'abstract':    ('textList', 'oai_dc:dc/dc:description/text()'),
    'date':        ('textList', 'oai_dc:dc/dc:date/text()'),
    },
    namespaces={
    'oai_dc': 'http://www.openarchives.org/OAI/2.0/oai_dc/',
    'dc' : 'http://purl.org/dc/elements/1.1/'}
)

# And create a registry for parsing the oai info, linked to the reader
registry = MetadataRegistry()
registry.registerReader('oai_dc', oai_dc_reader)

# arXiv OAI url we will query
URL = "http://export.arxiv.org/oai2"
# Create OAI client; now we're all set for listing some records
client = Client(URL, registry)

# Open files for writing
titlef    = open(title_file, 'w')
abstractf = open(abstr_file, 'w')

# Keep track of run-time and number of papers 
start_time = time.time()
count = 0

# Harvest
for record in client.listRecords(metadataPrefix='oai_dc', set=section):
    # Extract the title
    title = record[1].getField('title')[0]
    # Extract the abstract
    abstract = record[1].getField('abstract')[0]
    # And get the date (this is stored as yyyy-mm-dd in the arXiv metadata)
    date  = record[1].getField('date')[0]
    year  = int(date[0:4])
    month = int(date[5:7])

    # Write to file (add year info to the titles)
    titlef.write("%d %d "%(year,month) + title + "\n")
    abstractf.write(abstract + "\n")

    count += 1
    # Flush every 100 papers to the files
    if count % 100 == 0 and count > 1:
        print("Harvested {0} papers so far (elapsed time = {1})".format(count, time.time() - start_time))
        titlef.flush(); abstractf.flush()

# Close files
abstractf.close()
titlef.close()

# Report runtime and number of papers processed
runtime = time.time() - start_time
print("It took {} seconds to collect {} titles and abstracts".format(runtime, count))