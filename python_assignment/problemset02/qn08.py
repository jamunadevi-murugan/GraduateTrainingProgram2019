import math
lastvalue1=0
def eval_loop(s):
    global lastvalue1
    evaluation=s
    if evaluation=="done":
        return lastvalue1
    else:
        evaluation=eval(s)
        lastvalue1=evaluation
        return evaluation
currentvalue=0
j=''
while j!='done':
    evalvalue = input()
    j=evalvalue
    currentvalue=eval_loop(evalvalue)
    print(currentvalue)
