import numpy as np

with open("day 21/input") as f:
    text = f.read().strip()
    
numpad_mapping={(str(i)):np.array(((i-1)%3,2-(i-1)//3)) for i in range(1,10)} | {"0":np.array((1,3)),"A":np.array((2,3))}
arrow_mapping = {" ^A<v>"[i]:np.array((i%3,i//3)) for i in range(1,6)}
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

memo = {}

def get_length(char,amount,startpos,depth=0):
    outstr = ""
    if (char,amount,startpos[0],startpos[1],depth) in memo:
        return memo[(char,amount,startpos[0],startpos[1],depth)]
    out = 0
    if depth == 0: # numerical mapping
        vec = numpad_mapping[char]-startpos
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
        
    elif 1<=depth<=2: # arrow mapping
        vec = arrow_mapping[char]-startpos
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
        # out += min(case1,case2)
    
    else:
        # print(char*amount,end="")
        out = amount
    memo[(char,amount,startpos[0],startpos[1],depth)] = out
    return out



# def get_length()


# inverse_arrow_mapping = {tuple(value):key for key,value in (arrow_mapping.items())}
# inverse_numpad_mapping = {tuple(value):key for key,value in (numpad_mapping.items())}

# def reverser_arrows(string):
#     out = []
#     pointer = arrow_startpos
#     for char in string:
#         if char == "A":
#             out.append(inverse_arrow_mapping[tuple(pointer)])
#             continue
#         v = [np.array([0,-1]),np.array([0,1]),np.array([-1,0]),np.array([1,0])][list("^v<>").index(char)]
#         if tuple(pointer) not in inverse_arrow_mapping:
#             raise Exception
        
#         pointer += v
        
#     # print("".join(out))
#     return ("".join(out))

# def reverser_numpad(string):
#     out = []
#     pointer = numpad_startpos
#     for char in string:
#         if char == "A":
#             out.append(inverse_numpad_mapping[tuple(pointer)])
#             continue
#         v = [np.array([0,-1]),np.array([0,1]),np.array([-1,0]),np.array([1,0])][list("^v<>").index(char)]
#         if tuple(pointer) not in inverse_numpad_mapping:
#             raise Exception
#         pointer += v
#     # print("".join(out))
#     return ("".join(out))


def compute(string):
    previous = "A"
    sum_ = 0
    for char in string:
        r= (get_length(char,1,numpad_mapping[previous],0))
        sum_ += r

        previous = char
    # print(string)
    # print(st)
    # print(reverser_numpad(reverser_arrows(reverser_arrows(st))))


    # print()
    
    return sum_
    
    
total = 0
for s in text.split("\n"):
    a = compute(s)
    # print(f"{a}*{int(s[:3])} = {a*int(s[:3])}")
    total += a*int(s[:3])
print(total)         
# print(compute("029A"))         
# print(sum([compute(s)*int(s[:3]) for s in text.split("\n")]))         

    
# reverser_numpad(reverser_arrows(reverser_arrows("<v<A>>^A<vA<A>>^AAvAA<^A>A<v<A>>^AAvA^A<vA>^AA<A>A<v<A>A>^AAAvA<^A>A")))

pass








"""
<<vA  A>A>^AAvA<^A>AvA^A     <<vA>>^AAvA^A<vA>^AA<A>A<<vA>A>^AAAvA<^A>A
<<vA  >>^A<vA<A>>^AAvAA<^A>A <<vA>>^AAvA^A<vA>^AA<A>A<<vA>A>^AAAvA<^A>A


<<vAA>^A>A <AA>AvAA^A<vAAA>^A
<Av<AA>>^A <AA>AvAA^A<vAAA>^A

<<^ A^^A>>AvvvA
^<< A^^A>>AvvvA
"""













