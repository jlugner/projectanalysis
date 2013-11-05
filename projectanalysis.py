import os
VALID_EXSTENSIONS = [".h", ".hpp", ".c", ".cpp", ".py", ".java", ".rb", ".html", ".css", ".erb", ".m"]

for root, dirs, files in os.walk("./"):
    for file in files:
        fileName, fileExtension = os.path.splitext(file)
        if fileExtension in VALID_EXSTENSIONS:
             print (fileName, fileExtension)

