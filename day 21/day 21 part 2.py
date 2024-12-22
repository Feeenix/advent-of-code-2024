
with open("day 21/input") as f:
    text = f.read().strip()
    
numpad_mapping={(str(i)):(((i-1)%3,2-(i-1)//3)) for i in range(1,10)} | {"0":((1,3)),"A":((2,3))}
arrow_mapping = {" ^A<v>"[i]:((i%3,i//3)) for i in range(1,6)}
numpad_startpos = numpad_mapping["A"]
arrow_startpos = arrow_mapping["A"]
"""
+---+---+---+
| 7 | 8 | 9 |
+---+---+---+
| 4 | 5 | 6 |
+---+---+---+
| 1 | 2 | 3 |
+---+---+---+
    | 0 | A |
    +---+---+

    +---+---+
    | ^ | A |
+---+---+---+
| < | v | > |
+---+---+---+
"""
def subv(v1,v2):
    return (v1[0]-v2[0],v1[1]-v2[1])


memo = {}


def get_length(char,amount,startpos,depth=0):
    outstr = ""
    if (char,amount,startpos[0],startpos[1],depth) in memo:
        return memo[(char,amount,startpos[0],startpos[1],depth)]
    out = 0
    if depth == 0: # numerical mapping
        vec = subv(numpad_mapping[char],startpos)
        previous = "A"
        if (numpad_mapping[char][0],startpos[1]) == (0,3):
            previous = "A"
            case2 = 0  
            case2str = ""
            if vec[1] > 0:
                case2+=(get_length("v",abs(vec[1]),arrow_mapping[previous],depth+1))
                previous = "v"
            if vec[1] < 0:
                case2+=(get_length("^",abs(vec[1]),arrow_mapping[previous],depth+1))
                previous = "^"
            if vec[0] > 0:
                case2+=(get_length(">",abs(vec[0]),arrow_mapping[previous],depth+1))
                previous = ">"
            if vec[0] < 0:
                case2+=(get_length("<",abs(vec[0]),arrow_mapping[previous],depth+1))
                previous = "<"
            case2+=(get_length("A",amount,arrow_mapping[previous],depth+1))
        
            out+=case2
            outstr += case2str
        elif (startpos[0],numpad_mapping[char][1]) == (0,3):
            previous = "A"
            case2 = 0  
            case2str = ""
            if vec[0] > 0:
                case2+=(get_length(">",abs(vec[0]),arrow_mapping[previous],depth+1))
                previous = ">"
            if vec[0] < 0:
                case2+=(get_length("<",abs(vec[0]),arrow_mapping[previous],depth+1))
                previous = "<"
            if vec[1] > 0:
                case2+=(get_length("v",abs(vec[1]),arrow_mapping[previous],depth+1))
                previous = "v"
            if vec[1] < 0:
                case2+=(get_length("^",abs(vec[1]),arrow_mapping[previous],depth+1))
                previous = "^"
            case2+=(get_length("A",amount,arrow_mapping[previous],depth+1))
        
            out+=case2
            outstr += case2str
        else:
            case1 = 0  
            case1str = ""
            case2 = 0  
            case2str = ""
            if vec[0] > 0:
                case1 += ( get_length(">",abs(vec[0]),arrow_mapping[previous],depth+1))
                previous = ">"
            if vec[0] < 0:
                case1 += ( get_length("<",abs(vec[0]),arrow_mapping[previous],depth+1))
                previous = "<"
            if vec[1] > 0:
                case1 += ( get_length("v",abs(vec[1]),arrow_mapping[previous],depth+1))
                previous = "v"
            if vec[1] < 0:
                case1 += ( get_length("^",abs(vec[1]),arrow_mapping[previous],depth+1))
                previous = "^"
            case1 += ( get_length("A",amount,arrow_mapping[previous],depth+1))
            
            previous = "A"
            if vec[1] > 0:
                case2+=(get_length("v",abs(vec[1]),arrow_mapping[previous],depth+1))
                previous = "v"
            if vec[1] < 0:
                case2+=(get_length("^",abs(vec[1]),arrow_mapping[previous],depth+1))
                previous = "^"
            if vec[0] > 0:
                case2+=(get_length(">",abs(vec[0]),arrow_mapping[previous],depth+1))
                previous = ">"
            if vec[0] < 0:
                case2+=(get_length("<",abs(vec[0]),arrow_mapping[previous],depth+1))
                previous = "<"
            case2+=(get_length("A",amount,arrow_mapping[previous],depth+1))
        
            if case1 < case2:
                out += case1
                outstr += case1str
            else:
                out+=case2
                outstr += case2str
        # out += min(case1,case2)
        
    elif 1<=depth<=25: # arrow mapping
        vec = subv(arrow_mapping[char],startpos)
        previous = "A"
        if (arrow_mapping[char][0],startpos[1]) == (0,0):
            previous = "A"
            case2 = 0  
            case2str = ""
            if vec[1] > 0:
                case2 += (get_length("v",abs(vec[1]),arrow_mapping[previous],depth+1))
                previous = "v"
            if vec[1] < 0:
                case2 += (get_length("^",abs(vec[1]),arrow_mapping[previous],depth+1))
                previous = "^"
            if vec[0] > 0:
                case2 += (get_length(">",abs(vec[0]),arrow_mapping[previous],depth+1))
                previous = ">"
            if vec[0] < 0:
                case2 += (get_length("<",abs(vec[0]),arrow_mapping[previous],depth+1))
                previous = "<"
            case2 += (get_length("A",amount,arrow_mapping[previous],depth+1))
        
            out+=case2
            outstr += case2str
        elif (startpos[0],arrow_mapping[char][1]) == (0,0):
            previous = "A"
            case2 = 0  
            case2str = ""
            if vec[0] > 0:
                case2 += (get_length(">",abs(vec[0]),arrow_mapping[previous],depth+1))
                previous = ">"
            if vec[0] < 0:
                case2 += (get_length("<",abs(vec[0]),arrow_mapping[previous],depth+1))
                previous = "<"
            if vec[1] > 0:
                case2 += (get_length("v",abs(vec[1]),arrow_mapping[previous],depth+1))
                previous = "v"
            if vec[1] < 0:
                case2 += (get_length("^",abs(vec[1]),arrow_mapping[previous],depth+1))
                previous = "^"
            case2 += (get_length("A",amount,arrow_mapping[previous],depth+1))
        
            out+=case2
            outstr += case2str
        else:
            case1 = 0  
            case1str = ""
            case2 = 0  
            case2str = ""
            if vec[0] > 0:
                case1 += ( get_length(">",abs(vec[0]),arrow_mapping[previous],depth+1))
                previous = ">"
            if vec[0] < 0:
                case1 += ( get_length("<",abs(vec[0]),arrow_mapping[previous],depth+1))
                previous = "<"
            if vec[1] > 0:
                case1 += ( get_length("v",abs(vec[1]),arrow_mapping[previous],depth+1))
                previous = "v"
            if vec[1] < 0:
                case1 += ( get_length("^",abs(vec[1]),arrow_mapping[previous],depth+1))
                previous = "^"
            case1 += ( get_length("A",amount,arrow_mapping[previous],depth+1))
            previous = "A"
            
            if vec[1] > 0:
                case2 += (get_length("v",abs(vec[1]),arrow_mapping[previous],depth+1))
                previous = "v"
            if vec[1] < 0:
                case2 += (get_length("^",abs(vec[1]),arrow_mapping[previous],depth+1))
                previous = "^"
            if vec[0] > 0:
                case2 += (get_length(">",abs(vec[0]),arrow_mapping[previous],depth+1))
                previous = ">"
            if vec[0] < 0:
                case2 += (get_length("<",abs(vec[0]),arrow_mapping[previous],depth+1))
                previous = "<"
            case2+=(get_length("A",amount,arrow_mapping[previous],depth+1))
            
            if case1 < case2:
                out += case1
            else:
                out+=case2
    
    else:
        out = amount
    memo[(char,amount,startpos[0],startpos[1],depth)] = out
    return out

def compute(string):
    previous = "A"
    sum_ = 0
    for char in string:
        r= (get_length(char,1,numpad_mapping[previous],0))
        sum_ += r

        previous = char
    
    return sum_
    
    
total = 0
for s in text.split("\n"):
    a = compute(s)
    total += a*int(s[:3])
print(total)         

pass







