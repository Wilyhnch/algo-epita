# all td exe


import bintree
import queue
import stack
import fun

testspace = "as s ddf wqds deefsdf "
testspace2 = " wef wsdvrwvr vf "
fullpar = "((3*(5+1))+((3-2)*7))"
expnrl =  "3*(5+1)+(3-2)*7"
ez = "(5+1)"


#full parenthesies expression evaluation
def expfullpar (exp):
    opstack = stack.Stack()
    valstack = stack.Stack()
    for c in exp:
        if fun.isop(c):
            if c == ')':
                b = valstack.pop()
                valstack.push(fun.eval(opstack.pop(),valstack.pop(),b))
            elif c !='(':
                opstack.push(c)
        elif fun.isop(c) == False:
            valstack.push(int(c))
    return valstack.pop()

#print(expfullpar(fullpar))


#Normal expression evaluation
def expwipar (exp):




print(expwipar(expnrl))
