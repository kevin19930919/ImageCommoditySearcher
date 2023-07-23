import re

def parse(keyword:str):
    pattern = r'[^\u4e00-\u9fffA-Za-z0-9]'
    return re.sub(pattern, '', keyword)