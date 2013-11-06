import os
VALID_EXSTENSIONS = [".h", ".hpp", ".c", ".cpp", ".py", ".java", ".rb", ".html", ".css", ".erb", ".m"]

def file_length(file_path):
    with open(file_path) as f:
        rowCount = 0
        for i, l in enumerate(f):
            if len(l) > 1: rowCount +=1
    return rowCount

# Main program #
for root, dirs, files in os.walk("./"):
    for file in files:
        fileName, fileExtension = os.path.splitext(file)
        fullPath = os.path.join(root, file)
        if fileExtension in VALID_EXSTENSIONS:
             print ("File: " + fullPath + " Length: " +  str(file_length(fullPath)))