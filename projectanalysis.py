#!/usr/bin/env python
import os
import operator
import argparse
import file_operations as fo

VALID_EXSTENSIONS  = [".h", ".hpp", ".c", ".cpp", ".py", ".java", ".rb", ".html", ".css", ".erb", ".m", ".hs"]

# Main program, argument parsing
parser = argparse.ArgumentParser()
parser.parse_args()

extensions_map = dict((k,0) for k in VALID_EXSTENSIONS)

# Main Algorithm
for root, dirs, files in os.walk("./"):
    for file in files:
        fileName, fileExtension = os.path.splitext(file)
        fullPath = os.path.join(root, file)
        if fileExtension in VALID_EXSTENSIONS:
            fileLength = fo.file_length(fullPath)
            extensions_map[fileExtension] += fileLength

print("Number of rows of code:")
sorted_map = sorted(extensions_map.iteritems(), key=operator.itemgetter(1))
for  key, val in sorted_map:
    if not val == 0: print(key + ": " + str(val))