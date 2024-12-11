with open("day 5/input") as f:
    lines = f.read().strip()
rules,orderings = lines.split("\n\n")
rules = rules.split("\n")

isbeforedict = {}
illegalifbefore = {} # if the number at position j is in illegalifbefore[i], then we know it is an illegal ordering

for rule in rules:
    rule = rule.split("|")
    rule = [int(r.strip()) for r in rule]
    if rule[0] not in isbeforedict:
        isbeforedict[rule[0]] = []
    isbeforedict[rule[0]].append(rule[1]) 
    
    if rule[1] not in illegalifbefore:
        illegalifbefore[rule[1]] = []
    illegalifbefore[rule[1]].append(rule[0])
        
out = []
orderings = orderings.split("\n")
for ordering in orderings:
    
    ordering = ordering.split(",")
    ordering = [int(o) for o in ordering]
    length = len(ordering)
    for i in range(len(ordering)):
        for j in range(i+1,len(ordering)):
            if ordering[i] in illegalifbefore and ordering[j] in illegalifbefore[ordering[i]]:
                break # this ordering is invalid
        else: # this happens if the loop completes without breaking
            continue
        break # this happens if the loop breaks, go to the next ordering
    else: # this happens if the loop completes without breaking
        continue
    
    
    # bubblesort
    for i in range(len(ordering)):
        for j in range(i+1,len(ordering)):
            if ordering[i] in isbeforedict and ordering[j] in isbeforedict[ordering[i]]:
                # swap
                ordering[i],ordering[j] = ordering[j],ordering[i]
                
    
    out.append(ordering[length//2])
    
print(sum(out))


pass


    
    
    
    
    
    
    