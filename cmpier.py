#!/bin/python3

pro  = { '*' : 10 , '/':10 , '+':9,'-':9,'>':8,'<':8,'<=':8,'>=':8,'==':8,'|':6,'&':7,'=':5,'go to exit':5}
stack = []
l = []
checkstack = []

def check(now , old):
    if now == 'if' and old == "":
        checkstack.append('if')
        return now
    elif now == 'then' and (old == 'str' or old =='no') and len(checkstack) > 0:
        checkstack.pop()
        return None
    elif now == 'op' and (old == 'str' or old == 'no'):
        return now
    elif now == 'str' and (old == 'op' or old == None or old =='if' or old == 'bit' or old == "eq"):
        return now
    elif now == 'no' and (old == 'op' or old == None or old=='bit' or old == "eq"):
        return now
    elif now == 'eq' and old == 'str':
        return now
    elif now == 'bit' and (old == 'str' or old == 'no'):
        return now
    else :
        #print("now = " + str(now))
        #print("old = " + str(old))
        print('syntax error')
        exit()

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
        while len(stack) > 0 and pro[stack[-1]] >= pro[x]:
            l.append(stack.pop())
        stack.append(x)
def haveAeq(pos,s):
    while len(s) > pos:
        if s[pos] == '=':
            x,p =opp(pos,s)
            if x == '=':
                return True
            else :return False
        elif s[pos] == ' ':
            pos+=1
        else:
            return False
 
def stringToeq(s):
    p=0
    print(s)
    ifisexit = False
    old = ""
    while p < len(s):
        if isdigit(s[p]):
            no,p = digit(p,s)
            old = check("no" , old)
            #print(no)
            l.append(no)
        elif ischar(s[p]):
            #print('test2')
            st , p = string(p,s)
            if st == "if":
                pushToStack("go to exit")
                old = check("if" , old)
                ifisexit = True
            elif st == 'then':
                old = check("then" , old)
                while len(stack) > 0: 
                    l.append(stack.pop())
            else :
                old = check("str" , old)
                if haveAeq(p,s):
                    l.append('L '+st)
                else:
                    l.append('R '+st)
            #print('pointer = ' + str(p))
        elif isopp(s[p]):
            #print('test3')
            op , p = opp(p,s)
            if op == '|' or op == '&':
                old = check("bit" , old)
            elif op == '=':
                old = check("eq" , old)
            else : 
                old = check("op" , old)
            #print(op)
            pushToStack(op)
        elif s[p] == ' ':
            p+=1
        else:
            print("syntax error")
            exit()
    return ifisexit

def main():
    s = "if xxx*30 > 0+10 & 10 < sas  then d==100+a*b/ssss+11"
    stringToeq(s)
if __name__ == '__main__':
    ifisexit = main()
    while len(stack) > 0:
        l.append(stack.pop())
    l.append("exit")
    print(l)
