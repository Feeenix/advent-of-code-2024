



with open("day 7/input","r") as f:
    equations = f.read().strip().split("\n")

equations = [(lambda x:[int(x[0].strip()), [int (p) for p in x[1].strip().split(" ")]])(equation.split(":")) for equation in equations]


print(equations)

result = []

def evaluate(numbers,combo):
    out = numbers[0]
    for i,number in enumerate(numbers[1:]):
        operator = combo>>(i*2) &3
        if operator == 0: # add
            out += number
        if operator == 1: # mul
            out *= number
        if operator == 2: # concat
            out = int(str(out)+str(number))
        if operator == 3: 
            return -1
    return (out)

for equation in equations:
    shouldbe = equation[0]
    
    numbers = equation[1]
    
    for combo in range( 4**(len(numbers)-1)):
        if evaluate(numbers,combo) == shouldbe:
            result.append(shouldbe)
            break




print(sum(result))