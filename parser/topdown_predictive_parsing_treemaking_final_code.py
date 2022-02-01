import collections
# parsing tree classes and declaration
class Tree:
    def __init__(self,node):
        self.head = node

class Branch:
    def __init__(self,data):
        self.data = data
        self.branches = []
    def addbranch(self,branch):
        self.branches.append(branch)
thistree = Tree(Branch("$"))
stacktree = collections.deque()
stacktree.append(thistree.head)
# making stack and starting enter terms
stack = collections.deque()
stack.append("$")
stack.append("S")
input_arr = []

# this is impelimented with top down parsing by predictive parser
# getting input by file
fileObj = open("main.txt","r")
inputt = fileObj.read()
fileObj.close()

# class for each token
class inn:
    def __init__(self,a,b):
        self.type = a
        self.itself = b
z = ""
q = ""
d = 0
for i in inputt:
    if i==" ":
        continue
    if i=='\n':
        input_arr.append(inn(z,q))
        z = ""
        q = ""
        d = 0
        continue
    if i !=":" and d == 0:
        z += i
    elif i !=":" and d == 1:
        q += i
    else:
        d = 1
input_arr.append(inn(z,q))
input_arr.append(inn("$","$"))

# my table
# varibales and terms they go to, first one is variable name and others are where they make
v=[
#0
    ["stm",["loop","stm"],["loop","stm"],["condition","stm"],"mpt","mpt",["dec",";","stm"],["dec",";","stm"],["dec",";","stm"],["dec",";","stm"],["dec",";","stm"],["dec",";","stm"],["dec",";","stm"]],

    ["E",["T","E'"],["T","E'"],["T","E'"]],

    ["E'",["+","T","E'"],["-","T","E'"],["%","T","E'"],"mpt","mpt","mpt","mpt","mpt","mpt","mpt","mpt","mpt","mpt"],

    ["T",["F","T'"],["F","T'"],["F","T'"]],

    ["T'","mpt","mpt","mpt",["*","F","T'"],["/","F","T'"],"mpt","mpt","mpt","mpt","mpt","mpt","mpt","mpt","mpt"],

    ["F",["id"],["num"],["(","E",")","E"]],
#5
    ["S",["vfunc","S"],["types","id","sep","S"],["types","id","sep","S"],["types","id","sep","S"],["types","id","sep","S"],["types","id","sep","S"],["types","id","sep","S"],"mpt"],

    ["types",["int"],["long"],["short"],["char"],["double"],["float"]],

    ["vfunc",["void","(","dfun",")","{","stm","}"],],

    ["sep",["(","dfun",")","{","stm","return","E",";","}"],["dec2",";"],["dec2",";"],["dec2",";"],["dec2",";"],["dec2",";"],["dec2",";"],["dec2",";"]],

    ["dfun",["types","id2","ddfun"],["types","id2","ddfun"],["types","id2","ddfun"],["types","id2","ddfun"],["types","id2","ddfun"],["types","id2","ddfun"],"mpt"],
#10
    ["ddfun",[",","dfun"],"mpt"],

    ["id2",["id"],["*","id"]],

    ["dec",["types","id","dec2"],["types","id","dec2"],["types","id","dec2"],["types","id","dec2"],["types","id","dec2"],["types","id","dec2"],["id","normdec"]],

    ["dec2",["normdec"],["normdec"],["normdec"],["normdec"],["normdec"],"mpt",[",","id","dec2"]],

    ["normdec",["op","E"],["op","E"],["op","E"],["op","E"],["op","E"]],
#15
    ["loop",["while","(","comp",")","{","stm","}"],["for","(","dfor",")","{","stm","}"]],

    ["comp",["E","op2","E"],["E","op2","E"],["E","op2","E"]],

    ["dfor",["id","=","tmp",";","comp",";","efor"]],

    ["efor",["id","eefor"],["eefor","id"],["eefor","id"]],

    ["eefor",["++"],["--"]],
#20
    ["tmp",["id"],["num"]],
    
    ["condition",["if","(","comp",")","{","stm","}",",","cond"]],

    ["cond1",["else","cond2"],"mpt","mpt","mpt","mpt","mpt","mpt","mpt","mpt","mpt","mpt","mpt","mpt"],

    ["cond2",["condition"],["{","stm","}"]],

    ["id",["identifier"],["main"]],
#25
    ["op",["+="],["-="],["/="],["*="],["="]],

    ["op2",["=="],[">"],["<"],["<="],[">="]],
]

# for each variable there is a sort of things in same the row that for what should be made where we see 
# the table uper bound, uper row
upb=[
#0
    ["while","for","if","return","}","id","int","long","short","char","double","float"],

    ["id","(","num"],

    ["+","-","%",")","*","/",";","==",">","<","<=",">="],

    ["id","num","("],

    ["-","%","+","*","/",")","$",";","==",">","<","<=",">="],

    ["id","num","("],
#5
    ["void","int","long","short","char","double","float","$"],

    ["int","long","short","char","double","float"],

    ["void"],

    ["(","+=","-=","/=","*=","=",";"],

    ["int","long","short","char","double","float",")"],
#10
    [",",")"],

    ["id","*"],

    ["int","long","short","char","double","float","id"],

    ["+=","-=","/=","*=","=",";",","],

    ["+=","-=","/=","*=","="],
#15
    ["while","for"],

    ["(","id","num"],

    ["id"],

    ["id","++","--"],

    ["++","--"],
#20
    ["id","num"],

    ["if"],

    ["else","while","for","if","return","}","id","int","long","short","char","double","float"],

    ["if","{"],

    ["id","main"],
#25
    ["+=","-=","/=","*=","="],

    ["==",">","<","<=",">="],
]

# seaching in table
def my_sentences(a,b):
    c = b.itself
    for i in range(len(v)):
        if(v[i][0] == a):
            for j in range(len(upb[i])):
                if upb[i][j] == c :
                    return v[i][1+j]
                elif upb[i][j] == "id" and b.type == "identifier":
                    return v[i][1+j]
                elif upb[i][j] == "num" and (b.type == "number" or (b.type in upb[7])):
                    return v[i][1+j]
                elif upb[i][j] == "op2" and b.type == "operator":
                    return v[i][1+j]
    return 0

inlength = len(input_arr)
slength = len(stack)
sslength = len(stacktree)

# where it makes tree nodes
def parsingtree(x,y):
    current = stacktree.pop()
    if x[0] == "identifier" or x[0] == "num":
        thisbranch = Branch(y)
        stacktree.append(thisbranch)
        current.addbranch(thisbranch)
    elif x == "mpt":
        thisbranch = Branch(x)
        current.addbranch(thisbranch)
    else:
        for i in range(len(x)-1,-1,-1):
            thisbranch = Branch(x[i])
            stacktree.append(thisbranch)
            current.addbranch(thisbranch)

def parsefunction():
    if(stack[slength-1]=="identifier" and input_arr[0].type=="identifier") or (stack[slength-1]=="num" and (input_arr[0].type == "number" or (input_arr[0].type in upb[7]))):
        stack.pop()
        input_arr.pop(0)
        stacktree.pop()
        inlength = len(input_arr)
    elif(stack[slength-1]!=input_arr[0].itself):
        res = my_sentences(stack[slength-1],input_arr[0])
        parsingtree(res,input_arr[0].itself)
        stack.pop()
        if res == 0:
            return 0
        elif(res != "mpt"):
            for i in range(len(res)-1, -1, -1):  
                stack.append(res[i])
    elif input_arr[0]!='$':
        stack.pop()
        input_arr.pop(0)
        stacktree.pop()
        inlength = len(input_arr)
    return 1    

# running code where is it begin
result = 1
while(input_arr[0]!='$' and stack[slength-1]!='$' and result==1):
    result = parsefunction()
    slength = len(stack)
    sslength = len(stacktree)
        
'''print("start LSR tree traversal")
def go(node):
    if(len(node.branches)==0):
        print(node.data)
        return
    for i in range(len(node.branches)-1,-1,-1):
        print(node.branches[i].data)
        go(node.branches[i])
go(thistree.head)
print("end tree traversal")'''

# showing result
if result:
    print("accepted")
else:
    print("error happened at beginning of this point")
    for i in input_arr:
        if(i.itself == ";"):
            break
        print(i.itself,end=" ")
