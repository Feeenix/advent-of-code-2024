import re

mul = lambda s:int(s.replace("mul(","").replace(")","").split(",")[0])*int(s.replace("mul(","").replace(")","").split(",")[1])
with open('day 3/input') as f:
    text = f.read()
    l = sum([sum([  mul(s) for s in (re.findall(r'mul\(\d{1,3},\d{1,3}\)', subtext))]) \
        for subtext in re.findall(r'do\(\).*?don\'t\(\)', text, re.DOTALL) + (re.findall(r'^.*?(?=do\(\)|don\'t\(\))', text))])
    
    
# regular expression to find the string from start to either a "do()"" or "don't()".
# re = "^.*?(?=do\(\)|don't\(\))"











pass