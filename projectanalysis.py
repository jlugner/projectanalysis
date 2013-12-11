#!/usr/bin/env python
import os
import operator
import argparse
import file_operations as fo

VALID_EXSTENSIONS  = [".h", ".hpp", ".c", ".cpp", ".py", ".java", ".rb", ".html", ".css", ".erb", ".m", ".hs"]
searchMode = False
countRows  = False

# Main program, argument parsing
parser = argparse.ArgumentParser(description= "Various tools for working on a project.")
parser.add_argument("--search", help="Search project for the given string", dest="search_param")
parser.add_argument("--count", help="Count the number of rows in the project", action="store_true", default=True)
args = parser.parse_args()

extensions_map = dict((k,0) for k in VALID_EXSTENSIONS)

# Main Algorithm
for root, dirs, files in os.walk("./"):
    for file in files:
        fileName, fileExtension = os.path.splitext(file)
        fullPath = os.path.join(root, file)
        if fileExtension in VALID_EXSTENSIONS:
            if args.search_param:
                fo.search(fullPath, args.search_param)
            if args.count:
                fileLength = fo.file_length(fullPath)
                extensions_map[fileExtension] += fileLength

if args.count:
    print("Number of rows of code:")
    sorted_map = sorted(extensions_map.iteritems(), key=operator.itemgetter(1))
    for  key, val in sorted_map:
        if not val == 0: print(key + ": " + str(val))