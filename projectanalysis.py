import os
VALID_EXSTENSIONS = [".h", ".hpp", ".c", ".cpp", ".py", ".java", ".rb", ".html", ".css", ".erb", ".m"]

for root, dirs, files in os.walk("./"):
    for file in files:
        fileName, fileExtension = os.path.splitext(file)
        if fileExtension in VALID_EXSTENSIONS:
             print ("Path:", root, "File:", file, "Length:", file_length(file))


def file_length(file_path):
    with open(file_path) as f:
        for i, l in enumerate(f):
            pass
    return i + 1