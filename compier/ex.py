#!/bin/python3


stack = []
table = {}

def digit(s):
    x=0
    for i in s:
        x = x *10 + i - '0'
    return x

def main():
    f = open("./output.txt" , "r")
    for i in f:
        if i[0] >= '0' and i[0] <= '9':
            no = digit(i)
            stack.append(no)
        elif i[0] == 'R':
            if i.split(" ")[1] not in table.keys():
                table[i.split(" ")[1]] = 0
            stack.append(table[i.split(" ")[1]])
        elif i[0] == 'L':
        elif i == '=':
        elif i == ">=":
        elif i == "<=":
        elif i == ">":
        elif i == "<":
        elif i == "==":
        elif i == "+":
        elif i == "-":
        elif i == "*":
        elif i == "/":
        elif i == "&":
        elif i = "|":
        
    f.close()