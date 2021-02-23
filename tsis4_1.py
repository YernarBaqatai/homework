import re
is_open  = False
for i int range(int(input())):
    s = input()
    if "{" in s:
        is_open = True
    elif "}" in s:
        is_open = False
    elif is_open:
        data = re.findall("#[0-9a-fA-F]{3,6}", s)
        for i in data:
            print(i)