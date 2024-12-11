import re

l = sum([  int(s.replace("mul(","").replace(")","").split(",")[0])*int(s.replace("mul(","").replace(")","").split(",")[1]) for s in (re.findall(r'mul\(\d{1,3},\d{1,3}\)', open('day 3/input').read()))])
pass