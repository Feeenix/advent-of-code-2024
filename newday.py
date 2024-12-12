import os
d = os.listdir(".")
for day in range(1,26):
    if not ("day "+str(day) in d):
        os.mkdir("day "+str(day))
        with open("day "+str(day)+"/day "+str(day)+".py","w") as f:
            f.write("with open(\"day "+str(day)+"/testcase\") as f:\n    text = f.read().strip()")
            pass
        with open("day "+str(day)+"/day "+str(day)+" part 2.py","w"):
            pass
        with open("day "+str(day)+"/input","w"):
            pass
        with open("day "+str(day)+"/testcase","w"):
            pass
        break
        