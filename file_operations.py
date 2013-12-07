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

#def in_file(file_path):
#   with open(file_path) as f:
        