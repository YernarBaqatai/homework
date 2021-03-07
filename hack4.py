import re
#x = re.findall(r"[QWRTYPSDFGHJKLZXCVBNM|qwrtypsdfghjklzxcvbnm][AEIOU|aeiou]{2,}[QWRTYPSDFGHJKLZXCVBNM|qwrtypsdfghjklzxcvbnm]",s)
s = '[qwrtypsdfghjklzxcvbnm]'
a = re.findall('(?<=' + s +')([aeiou]{2,})' + s, input(), re.I)
if a:
    for sub in a:
        print(sub)
else: print(-1)