#!/bin/python3

pro  = { '*' : 10 , '/':10 , '+':9,'-':9,'>':8,'<':8,'<=':8,'>=':8,'==':8,'||':6,'&&':7,'=':5,'go to exit':5,'|':0,'&':0}
stack = []
l = []
def isdigit(x):
    if x >='0' and x <= '9':
        return True
    return False
def ischar(x):
    if (x >='a' and x <= 'z') or (x >='A' and x <= 'Z'):
        return True
    return False
def isopp(x):
    if x in pro.keys():
        return True
    return False
def digit(p,s):
    x=0
    while p < len(s) and isdigit(s[p]):
        x= x*10 + ord(s[p])-ord('0')
        p+=1
    return x , p
def string(p,s):
    x=''
    while p < len(s) and ischar(s[p]):
        x+=s[p]
        p+=1
    return x,p;
def opp(p,s):
    x=''
    while p < len(s) and s[p] in pro.keys():
        x+=s[p]
        p+=1
    return x,p
def pushToStack(x):
    if len(stack) == 0 or pro[stack[-1]] < pro[x]:
        stack.append(x)
    else :
        while len(stack) == 0 or pro[stack[-1]] >= pro[x]:
            l.append(stack.pop())
        stack.append(x)
def haveAeq(pos,s):
    while len(s) > pos:
        if s[pos] == '=':
            return True
        elif s[pos] == ' ':
            pos+=1
        else:
            return False
 
def stringToeq(s):
    p=0
    print(s)
    ifisexit = False
    while p < len(s):
        if isdigit(s[p]):
            no,p = digit(p,s)
            #print(no)
            l.append(no)
        elif ischar(s[p]):
            #print('test2')
            st , p = string(p,s)
            if st == "if":
                pushToStack("go to exit")
                ifisexit = True
            elif st == 'then':
                while len(stack) > 0: 
                    l.append(stack.pop())
            else :
                if haveAeq(p,s):
                    l.append('L '+st)
                else:
                    l.append('R '+st)
            #print('pointer = ' + str(p))
        elif isopp(s[p]):
            #print('test3')
            op , p = opp(p,s)
            #print(op)
            pushToStack(op)
        elif s[p] == ' ':
            p+=1
    return ifisexit

def main():
    s = "if xxx*30 > 0+10 && 10 < sas then x = 100+a*b/ssss+11"
    stringToeq(s)

if __name__ == '__main__':
    ifisexit = main()
    while len(stack) > 0:
        l.append(stack.pop())
    l.append("exit")
    print(l)