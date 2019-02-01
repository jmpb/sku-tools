import re

def find_sku(name):
    s = ""
    for i, c in enumerate(name):
        p = re.compile(r"[A-Z0-9-/\\_.]+")
        # if index is in middle of name
        if i > 0 and i < len(name) - 1:
            if p.match(name[i]):
                if p.match(name[i + 1]) or p.match(name[i - 1]):
                    s += name[i]
        # if first index in name
        elif i == 0:
            if p.match(name[i]):
                if p.match(name[i + 1]):
                    s += name[i]
        # if last index in name
        else:
            if p.match(name[i]):
                if p.match(name[i - 1]):
                    s += name[i]
    return s