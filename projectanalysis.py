import os

VALID_EXSTENSIONS  = [".h", ".hpp", ".c", ".cpp", ".py", ".java", ".rb", ".html", ".css", ".erb", ".m"]
COMMENT_INDICATORS = ["/*", "#", "//", "{-", "--"]

def file_length(file_path):
    with open(file_path) as f:
        rowCount = 0
        for i, l in enumerate(f):
            if len(l) > 1 and not is_comment(l[:2]): rowCount +=1
    return rowCount

def is_comment(str):
    for comment in COMMENT_INDICATORS:
        if str.startswith(comment):
            return True
    return False

# Main program #
extensions_map = dict((k,0) for k in VALID_EXSTENSIONS)

for root, dirs, files in os.walk("./"):
    for file in files:
        fileName, fileExtension = os.path.splitext(file)
        fullPath = os.path.join(root, file)
        if fileExtension in VALID_EXSTENSIONS:
             extensions_map[fileExtension] += file_length(fullPath)
print(extensions_map)
