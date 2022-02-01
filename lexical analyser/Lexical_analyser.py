# Lexical analysing Starts
#

# start of running code      
# read file and save it into an array
# read result of preprocessor
# if u mix preprocessor code with this project u will get better result
fileObj = open("main.txt","r")
code = fileObj.read()
fileObj.close()
print(code)

# where we save tokens
tokens_arr = []
# token for each 
class token:
    def __init__(self,V,T,L,C):
        # character or string
        self.value = V
        # type of value
        self.type = T
        # number of line and character in line
        self.line = L
        self.character = C

# predefine values
keywords = ["if","for","while","return","void","int","char"
        ,"break","case","const","continue","do","long"
        ,"short","sizeof","static","typedef","switch"
        ,"else","double","float","struct"]
punctuators = [",",";","}","{","[","]",")","(","*",":","#"]
operators = ["+","-","/","%","++","--","+=","-=","/=","*=","%=","==","<",">","<=",">=","**","&","="]
# other values are identifiers depends on input

# predefine types
types = ["constant","keyword","punctuator","operator","identifier"]

# types is also used in this program 
types_2 = ["non-constant","space","alphabet","underscore"]

# using isdigit and isalpha for recognise if there is number or alphabets

# vertex and edge
class vertex:
    def __init__(self,CT):
        # type of vertex, it is string, final and non-final
        self.current_type = CT
        # array in edges
        self.connected_in_edges = []
    def add_edge(self,E):
        self.connected_in_edges.append(E)

class edge:
    def __init__(self,I,O,IT):
        # I is a class
        self.in_vertex = I
        # O is a class
        self.out_vertex = O
        # IT is a string
        self.input_types = []
        if(isinstance(IT,list)):
            for i in IT:
                self.input_types.append(i)
        else: self.input_types.append(IT)
        #print(self.input_types)

# building graph
# BEGINNING OF GRAPH
BOG = vertex("final_punctuator")
# ERROR node
ERROR = vertex("ERROR")

## operator
# ‌beginning node -operator-> next node
eogtmp = vertex("final_operator")
firstoperator = eogtmp
ctmp = edge(BOG,eogtmp,types[3])
BOG.add_edge(ctmp)

# arr with constant, alphabet, punctuator and space
arr = []
arr.append(types[0])
arr.append(types[2])
arr.append(types_2[1])
arr.append(types_2[2])

# node -non_operator-> beginning node
ctmp = edge(eogtmp,BOG,arr)
eogtmp.add_edge(ctmp)

# node -operator-> next node
btmp = eogtmp
eogtmp = vertex("final_operator")
ctmp = edge(btmp,eogtmp,types[3])
btmp.add_edge(ctmp)

# node -non_operator-> beginning node
ctmp = edge(eogtmp,BOG,arr)
eogtmp.add_edge(ctmp)

# node -operator-> ERROR node 
ctmp = edge(eogtmp,ERROR,types[3])
eogtmp.add_edge(ctmp)


## punctuator
# beginning node -punctuator-> next node
eogtmp = vertex("final_punctuator")
ctmp = edge(BOG,eogtmp,types[2])
BOG.add_edge(ctmp)

# add operator to arr
arr.append(types[3])
# node -any-> beginning node
ctmp = edge(eogtmp,BOG,arr)
eogtmp.add_edge(ctmp)

## number recognizing
eogtmp = vertex("final_int")
firstnummber = eogtmp
ctmp = edge(BOG,eogtmp,types[0])
BOG.add_edge(ctmp)

# node -number-> same node, self loop
ctmp = edge(eogtmp,eogtmp,types[0])
eogtmp.add_edge(ctmp)

# array with punctuator, operator and space
arr = []
arr.append(types_2[1])
arr.append(types[2])
arr.append(types[3])

# node -punctuator, operator and space-> beginning node
ctmp = edge(eogtmp,BOG,arr)
eogtmp.add_edge(ctmp)

# node -alphabet-> ERROR node
ctmp = edge(eogtmp,ERROR,types_2[2])
eogtmp.add_edge(ctmp)

# for floating point in numbers
# node -dot-> next node
btmp = eogtmp
eogtmp = vertex("notfinal")
ctmp = edge(btmp,eogtmp,".")
btmp.add_edge(ctmp)

# node -anything other than dot-> ERROR node
ctmp = edge(btmp,ERROR,"others")
btmp.add_edge(ctmp)

# dot node -nummber-> next node
btmp = eogtmp
eogtmp = vertex("final_double")
ctmp = edge(btmp,eogtmp,types[0])
btmp.add_edge(ctmp)

# node -number-> same node, self loop
ctmp = edge(eogtmp,eogtmp,types[0])
eogtmp.add_edge(ctmp)

# node -puctuator, operator and space-> beginning node
ctmp = edge(eogtmp,BOG,arr)
eogtmp.add_edge(ctmp)

# node -aphabet->  ERROR node
ctmp = edge(eogtmp,ERROR,types_2[2])
eogtmp.add_edge(ctmp)

# Error node get aways
# Error -number-> first number node
ctmp = edge(ERROR,firstnummber,types[0])
ERROR.add_edge(ctmp)

# Error -puctuator-> beginning node
ctmp = edge(ERROR,BOG,types[2])
ERROR.add_edge(ctmp)

# Error -operator-> first operator node
ctmp = edge(ERROR,firstoperator,types[2])
ERROR.add_edge(ctmp)

## identifier and keywords
arr = []
arr.append(types[2])
arr.append(types[3])
arr.append(types_2[1])

arr_2 = []
arr_2.append(types[0])
arr_2.append(types_2[2])
arr_2.append(types_2[3])
identifier = vertex("final-identifier")
ctmp = edge(identifier,BOG,arr)
identifier.add_edge(ctmp)

ctmp = edge(identifier,identifier,arr_2)
identifier.add_edge(ctmp)

# if and int
v_i = vertex("final-identifier")
ctmp = edge(BOG,v_i,'i')
BOG.add_edge(ctmp)

v_f = vertex("final-keyword")
ctmp = edge(v_i,v_f,'f')
v_i.add_edge(ctmp)

ctmp = edge(v_f,BOG,arr)
v_f.add_edge(ctmp)

ctmp = edge(v_f,identifier,arr_2)
v_f.add_edge(ctmp)

v_n = vertex("final-identifier")
ctmp = edge(v_i,v_n,'n')
v_i.add_edge(ctmp)

ctmp = edge(v_i,BOG,arr)
v_i.add_edge(ctmp)

ctmp = edge(v_i,identifier,arr_2)
v_i.add_edge(ctmp)

v_t = vertex("final-keyword")
ctmp = edge(v_n,v_t,'t')
v_n.add_edge(ctmp)

ctmp = edge(v_n,identifier,arr_2)
v_n.add_edge(ctmp)

ctmp = edge(v_t,BOG,arr)
v_t.add_edge(ctmp)

ctmp = edge(v_t,identifier,arr_2)
v_t.add_edge(ctmp)

# while
v_w = vertex("final-identifier")
ctmp = edge(BOG,v_w,'w')
BOG.add_edge(ctmp)

v_h = vertex("final-identifier")
ctmp = edge(v_w,v_h,'h')
v_w.add_edge(ctmp)

ctmp = edge(v_w,BOG,arr)
v_w.add_edge(ctmp)

ctmp = edge(v_w,identifier,arr_2)
v_w.add_edge(ctmp)

v_i = vertex("final-identifier")
ctmp = edge(v_h,v_i,'i')
v_h.add_edge(ctmp)

ctmp = edge(v_t,BOG,arr)
v_t.add_edge(ctmp)

ctmp = edge(v_h,identifier,arr_2)
v_h.add_edge(ctmp)

v_l = vertex("final-identifier")
ctmp = edge(v_i,v_l,'l')
v_i.add_edge(ctmp)

ctmp = edge(v_i,BOG,arr)
v_i.add_edge(ctmp)

ctmp = edge(v_i,identifier,arr_2)
v_i.add_edge(ctmp)

v_e = vertex("final-keyword")
ctmp = edge(v_l,v_e,'e')
v_l.add_edge(ctmp)

ctmp = edge(v_l,BOG,arr)
v_l.add_edge(ctmp)

ctmp = edge(v_l,identifier,arr_2)
v_l.add_edge(ctmp)

ctmp = edge(v_e,identifier,arr_2)
v_e.add_edge(ctmp)

ctmp = edge(v_e,BOG,arr)
v_e.add_edge(ctmp)
# void
v_v = vertex("final-identifier")
ctmp = edge(BOG,v_v,'v')
BOG.add_edge(ctmp)

v_o = vertex("final-identifier")
ctmp = edge(v_v,v_o,'o')
v_v.add_edge(ctmp)

ctmp = edge(v_v,BOG,arr)
v_v.add_edge(ctmp)

ctmp = edge(v_v,identifier,arr_2)
v_v.add_edge(ctmp)

v_i = vertex("final-identifier")
ctmp = edge(v_o,v_i,'i')
v_o.add_edge(ctmp)

ctmp = edge(v_o,BOG,arr)
v_o.add_edge(ctmp)

ctmp = edge(v_o,identifier,arr_2)
v_o.add_edge(ctmp)

v_d = vertex("final-keyword")
ctmp = edge(v_i,v_d,'d')
v_i.add_edge(ctmp)

ctmp = edge(v_i,BOG,arr)
v_i.add_edge(ctmp)

ctmp = edge(v_i,identifier,arr_2)
v_i.add_edge(ctmp)

ctmp = edge(v_d,identifier,arr_2)
v_d.add_edge(ctmp)

ctmp = edge(v_d,BOG,arr)
v_d.add_edge(ctmp)
# for and float
v_f = vertex("final-identifier")
ctmp = edge(BOG,v_f,'f')
BOG.add_edge(ctmp)

v_o = vertex("final-identifier")
ctmp = edge(v_f,v_o,'o')
v_f.add_edge(ctmp)

v_r = vertex("final-keyword")
ctmp = edge(v_o,v_r,'r')
v_o.add_edge(ctmp)

ctmp = edge(v_o,BOG,arr)
v_o.add_edge(ctmp)

ctmp = edge(v_o,identifier,arr_2)
v_o.add_edge(ctmp)

ctmp = edge(v_r,BOG,arr)
v_r.add_edge(ctmp)

ctmp = edge(v_r,identifier,arr_2)
v_r.add_edge(ctmp)

v_l = vertex("final-identifier")
ctmp = edge(v_f,v_l,'l')
v_f.add_edge(ctmp)

ctmp = edge(v_f,BOG,arr)
v_f.add_edge(ctmp)

ctmp = edge(v_f,identifier,arr_2)
v_f.add_edge(ctmp)

v_o = vertex("final-identifier")
ctmp = edge(v_l,v_o,'o')
v_l.add_edge(ctmp)

ctmp = edge(v_l,BOG,arr)
v_l.add_edge(ctmp)

ctmp = edge(v_l,identifier,arr_2)
v_l.add_edge(ctmp)

v_a = vertex("final-identifier")
ctmp = edge(v_o,v_a,'a')
v_o.add_edge(ctmp)

ctmp = edge(v_o,BOG,arr)
v_o.add_edge(ctmp)

ctmp = edge(v_o,identifier,arr_2)
v_o.add_edge(ctmp)

v_t = vertex("final-keyword")
ctmp = edge(v_a,v_t,'t')
v_a.add_edge(ctmp)

ctmp = edge(v_a,BOG,arr)
v_a.add_edge(ctmp)

ctmp = edge(v_a,identifier,arr_2)
v_a.add_edge(ctmp)

ctmp = edge(v_t,BOG,arr)
v_t.add_edge(ctmp)

ctmp = edge(v_t,identifier,arr_2)
v_t.add_edge(ctmp)
# break
v_b = vertex("final-identifier")
ctmp = edge(BOG,v_b,'b')
BOG.add_edge(ctmp)

v_r = vertex("final-identifier")
ctmp = edge(v_b,v_r,'r')
v_b.add_edge(ctmp)

ctmp = edge(v_b,BOG,arr)
v_b.add_edge(ctmp)

ctmp = edge(v_b,identifier,arr_2)
v_b.add_edge(ctmp)

v_e = vertex("final-identifier")
ctmp = edge(v_r,v_e,'e')
v_r.add_edge(ctmp)

ctmp = edge(v_r,BOG,arr)
v_r.add_edge(ctmp)

ctmp = edge(v_r,identifier,arr_2)
v_r.add_edge(ctmp)

v_a = vertex("final-identifier")
ctmp = edge(v_e,v_a,'a')
v_e.add_edge(ctmp)

ctmp = edge(v_e,BOG,arr)
v_e.add_edge(ctmp)

ctmp = edge(v_e,identifier,arr_2)
v_e.add_edge(ctmp)

v_k = vertex("final-keyword")
ctmp = edge(v_a,v_k,'k')
v_a.add_edge(ctmp)

ctmp = edge(v_a,BOG,arr)
v_a.add_edge(ctmp)

ctmp = edge(v_a,identifier,arr_2)
v_a.add_edge(ctmp)

ctmp = edge(v_k,BOG,arr)
v_k.add_edge(ctmp)

ctmp = edge(v_k,identifier,arr_2)
v_k.add_edge(ctmp)
# long
v_l = vertex("final-identifier")
ctmp = edge(BOG,v_l,'l')
BOG.add_edge(ctmp)

v_o = vertex("final-identifier")
ctmp = edge(v_l,v_o,'o')
v_l.add_edge(ctmp)

ctmp = edge(v_l,BOG,arr)
v_l.add_edge(ctmp)

ctmp = edge(v_l,identifier,arr_2)
v_l.add_edge(ctmp)

v_n = vertex("final-identifier")
ctmp = edge(v_o,v_n,'n')
v_o.add_edge(ctmp)

ctmp = edge(v_o,BOG,arr)
v_o.add_edge(ctmp)

ctmp = edge(v_o,identifier,arr_2)
v_o.add_edge(ctmp)

v_g = vertex("final-keyword")
ctmp = edge(v_n,v_g,'g')
v_n.add_edge(ctmp)

ctmp = edge(v_n,BOG,arr)
v_n.add_edge(ctmp)

ctmp = edge(v_n,identifier,arr_2)
v_n.add_edge(ctmp)

ctmp = edge(v_g,BOG,arr)
v_g.add_edge(ctmp)

ctmp = edge(v_g,identifier,arr_2)
v_g.add_edge(ctmp)
# else
v_e = vertex("final-identifier")
ctmp = edge(BOG,v_e,'e')
BOG.add_edge(ctmp)

v_l = vertex("final-identifier")
ctmp = edge(v_e,v_l,'l')
v_e.add_edge(ctmp)

ctmp = edge(v_e,BOG,arr)
v_e.add_edge(ctmp)

ctmp = edge(v_e,identifier,arr_2)
v_e.add_edge(ctmp)

v_s = vertex("final-identifier")
ctmp = edge(v_l,v_s,'s')
v_l.add_edge(ctmp)

ctmp = edge(v_l,BOG,arr)
v_l.add_edge(ctmp)

ctmp = edge(v_l,identifier,arr_2)
v_l.add_edge(ctmp)

v_e = vertex("final-keyword")
ctmp = edge(v_s,v_e,'e')
v_s.add_edge(ctmp)

ctmp = edge(v_s,BOG,arr)
v_s.add_edge(ctmp)

ctmp = edge(v_s,identifier,arr_2)
v_s.add_edge(ctmp)

ctmp = edge(v_e,BOG,arr)
v_e.add_edge(ctmp)

ctmp = edge(v_e,identifier,arr_2)
v_e.add_edge(ctmp)
# printf
v_p = vertex("final-identifier")
ctmp = edge(BOG,v_p,'p')
BOG.add_edge(ctmp)

v_r = vertex("final-identifier")
ctmp = edge(v_p,v_r,'r')
v_p.add_edge(ctmp)

ctmp = edge(v_p,BOG,arr)
v_p.add_edge(ctmp)

ctmp = edge(v_p,identifier,arr_2)
v_p.add_edge(ctmp)

v_i = vertex("final-identifier")
ctmp = edge(v_r,v_i,'i')
v_r.add_edge(ctmp)

ctmp = edge(v_r,BOG,arr)
v_r.add_edge(ctmp)

ctmp = edge(v_r,identifier,arr_2)
v_r.add_edge(ctmp)

v_n = vertex("final-identifier")
ctmp = edge(v_i,v_n,'n')
v_i.add_edge(ctmp)

ctmp = edge(v_i,BOG,arr)
v_i.add_edge(ctmp)

ctmp = edge(v_i,identifier,arr_2)
v_i.add_edge(ctmp)

v_t = vertex("final-identifier")
ctmp = edge(v_n,v_t,'t')
v_n.add_edge(ctmp)

ctmp = edge(v_n,BOG,arr)
v_n.add_edge(ctmp)

ctmp = edge(v_n,identifier,arr_2)
v_n.add_edge(ctmp)

v_f = vertex("final-keyword")
ctmp = edge(v_t,v_f,'f')
v_t.add_edge(ctmp)

ctmp = edge(v_t,BOG,arr)
v_t.add_edge(ctmp)

ctmp = edge(v_t,identifier,arr_2)
v_t.add_edge(ctmp)

ctmp = edge(v_f,BOG,arr)
v_f.add_edge(ctmp)

ctmp = edge(v_f,identifier,arr_2)
v_f.add_edge(ctmp)
# typedef
v_p = vertex("final-identifier")
ctmp = edge(BOG,v_p,'t')
BOG.add_edge(ctmp)

v_r = vertex("final-identifier")
ctmp = edge(v_p,v_r,'y')
v_p.add_edge(ctmp)

ctmp = edge(v_p,BOG,arr)
v_p.add_edge(ctmp)

ctmp = edge(v_p,identifier,arr_2)
v_p.add_edge(ctmp)

v_i = vertex("final-identifier")
ctmp = edge(v_r,v_i,'p')
v_r.add_edge(ctmp)

ctmp = edge(v_r,BOG,arr)
v_r.add_edge(ctmp)

ctmp = edge(v_r,identifier,arr_2)
v_r.add_edge(ctmp)

v_n = vertex("final-identifier")
ctmp = edge(v_i,v_n,'e')
v_i.add_edge(ctmp)

ctmp = edge(v_i,BOG,arr)
v_i.add_edge(ctmp)

ctmp = edge(v_i,identifier,arr_2)
v_i.add_edge(ctmp)

v_t = vertex("final-identifier")
ctmp = edge(v_n,v_t,'d')
v_n.add_edge(ctmp)

ctmp = edge(v_n,BOG,arr)
v_n.add_edge(ctmp)

ctmp = edge(v_n,identifier,arr_2)
v_n.add_edge(ctmp)

v_f = vertex("final-identifier")
ctmp = edge(v_t,v_f,'e')
v_t.add_edge(ctmp)

ctmp = edge(v_t,BOG,arr)
v_t.add_edge(ctmp)

ctmp = edge(v_t,identifier,arr_2)
v_t.add_edge(ctmp)

v_x = vertex("final-keyword")
ctmp = edge(v_f,v_x,'f')
v_f.add_edge(ctmp)

ctmp = edge(v_f,BOG,arr)
v_f.add_edge(ctmp)

ctmp = edge(v_f,identifier,arr_2)
v_f.add_edge(ctmp)

ctmp = edge(v_x,BOG,arr)
v_x.add_edge(ctmp)

ctmp = edge(v_x,identifier,arr_2)
v_x.add_edge(ctmp)
# return
v_p = vertex("final-identifier")
ctmp = edge(BOG,v_p,'r')
BOG.add_edge(ctmp)

v_r = vertex("final-identifier")
ctmp = edge(v_p,v_r,'e')
v_p.add_edge(ctmp)

ctmp = edge(v_p,BOG,arr)
v_p.add_edge(ctmp)

ctmp = edge(v_p,identifier,arr_2)
v_p.add_edge(ctmp)

v_i = vertex("final-identifier")
ctmp = edge(v_r,v_i,'t')
v_r.add_edge(ctmp)

ctmp = edge(v_r,BOG,arr)
v_r.add_edge(ctmp)

ctmp = edge(v_r,identifier,arr_2)
v_r.add_edge(ctmp)

v_n = vertex("final-identifier")
ctmp = edge(v_i,v_n,'u')
v_i.add_edge(ctmp)

ctmp = edge(v_i,BOG,arr)
v_i.add_edge(ctmp)

ctmp = edge(v_i,identifier,arr_2)
v_i.add_edge(ctmp)

v_t = vertex("final-identifier")
ctmp = edge(v_n,v_t,'r')
v_n.add_edge(ctmp)

ctmp = edge(v_t,BOG,arr)
v_t.add_edge(ctmp)

ctmp = edge(v_n,identifier,arr_2)
v_n.add_edge(ctmp)

v_f = vertex("final-keyword")
ctmp = edge(v_t,v_f,'n')
v_t.add_edge(ctmp)

ctmp = edge(v_t,BOG,arr)
v_t.add_edge(ctmp)

ctmp = edge(v_t,identifier,arr_2)
v_t.add_edge(ctmp)

ctmp = edge(v_f,BOG,arr)
v_f.add_edge(ctmp)

ctmp = edge(v_f,identifier,arr_2)
v_f.add_edge(ctmp)
# do and double
v_p = vertex("final-identifier")
ctmp = edge(BOG,v_p,'d')
BOG.add_edge(ctmp)

v_r = vertex("final-keyword")
ctmp = edge(v_p,v_r,'o')
v_p.add_edge(ctmp)

ctmp = edge(v_p,BOG,arr)
v_p.add_edge(ctmp)

ctmp = edge(v_p,identifier,arr_2)
v_p.add_edge(ctmp)

v_i = vertex("final-identifier")
ctmp = edge(v_r,v_i,'u')
v_r.add_edge(ctmp)

ctmp = edge(v_r,BOG,arr)
v_r.add_edge(ctmp)

ctmp = edge(v_r,identifier,arr_2)
v_r.add_edge(ctmp)

v_n = vertex("final-identifier")
ctmp = edge(v_i,v_n,'b')
v_i.add_edge(ctmp)

ctmp = edge(v_i,BOG,arr)
v_i.add_edge(ctmp)

ctmp = edge(v_i,identifier,arr_2)
v_i.add_edge(ctmp)

v_t = vertex("final-identifier")
ctmp = edge(v_n,v_t,'l')
v_n.add_edge(ctmp)

ctmp = edge(v_n,BOG,arr)
v_n.add_edge(ctmp)

ctmp = edge(v_n,identifier,arr_2)
v_n.add_edge(ctmp)

v_f = vertex("final-keyword")
ctmp = edge(v_t,v_f,'e')
v_t.add_edge(ctmp)

ctmp = edge(v_t,BOG,arr)
v_t.add_edge(ctmp)

ctmp = edge(v_t,identifier,arr_2)
v_t.add_edge(ctmp)

ctmp = edge(v_f,BOG,arr)
v_f.add_edge(ctmp)

ctmp = edge(v_f,identifier,arr_2)
v_f.add_edge(ctmp)
# char case const continue
v_p = vertex("final-identifier")
ctmp = edge(BOG,v_p,'c')
BOG.add_edge(ctmp)

v_h = vertex("final-identifier")
ctmp = edge(v_p,v_h,'h')
v_p.add_edge(ctmp)

v_a = vertex("final-identifier")
ctmp = edge(v_h,v_a,'a')
v_h.add_edge(ctmp)

ctmp = edge(v_h,BOG,arr)
v_h.add_edge(ctmp)

ctmp = edge(v_h,identifier,arr_2)
v_h.add_edge(ctmp)

v_r = vertex("final-keyword")
ctmp = edge(v_a,v_r,'r')
v_a.add_edge(ctmp)

ctmp = edge(v_a,BOG,arr)
v_a.add_edge(ctmp)

ctmp = edge(v_a,identifier,arr_2)
v_a.add_edge(ctmp)

ctmp = edge(v_r,BOG,arr)
v_r.add_edge(ctmp)

ctmp = edge(v_r,identifier,arr_2)
v_r.add_edge(ctmp)

v_r = vertex("final-identifier")
ctmp = edge(v_p,v_r,'a')
v_p.add_edge(ctmp)

v_i = vertex("final-identifier")
ctmp = edge(v_r,v_i,'s')
v_r.add_edge(ctmp)

ctmp = edge(v_r,identifier,arr_2)
v_r.add_edge(ctmp)

v_n = vertex("final-keyword")
ctmp = edge(v_i,v_n,'e')
v_i.add_edge(ctmp)

ctmp = edge(v_i,BOG,arr)
v_i.add_edge(ctmp)

ctmp = edge(v_i,identifier,arr_2)
v_i.add_edge(ctmp)

ctmp = edge(v_n,BOG,arr)
v_n.add_edge(ctmp)

ctmp = edge(v_n,identifier,arr_2)
v_n.add_edge(ctmp)

v_o = vertex("final-identifier")
ctmp = edge(v_p,v_o,'o')
v_p.add_edge(ctmp)


v_n = vertex("final-identifier")
ctmp = edge(v_o,v_n,'n')
v_o.add_edge(ctmp)

ctmp = edge(v_p,BOG,arr)
v_p.add_edge(ctmp)

ctmp = edge(v_p,identifier,arr_2)
v_p.add_edge(ctmp)

v_s = vertex("final-identifier")
ctmp = edge(v_n,v_s,'s')
v_n.add_edge(ctmp)

v_t = vertex("final-keyword")
ctmp = edge(v_s,v_t,'t')
v_s.add_edge(ctmp)

ctmp = edge(v_s,BOG,arr)
v_s.add_edge(ctmp)

ctmp = edge(v_s,identifier,arr_2)
v_s.add_edge(ctmp)

ctmp = edge(v_t,BOG,arr)
v_t.add_edge(ctmp)

ctmp = edge(v_t,identifier,arr_2)
v_t.add_edge(ctmp)

v_t = vertex("final-identifier")
ctmp = edge(v_n,v_t,'t')
v_n.add_edge(ctmp)

ctmp = edge(v_o,BOG,arr)
v_o.add_edge(ctmp)

ctmp = edge(v_o,identifier,arr_2)
v_o.add_edge(ctmp)

ctmp = edge(v_n,identifier,arr_2)
v_n.add_edge(ctmp)

v_i = vertex("final-identifier")
ctmp = edge(v_t,v_i,'i')
v_t.add_edge(ctmp)

ctmp = edge(v_t,BOG,arr)
v_t.add_edge(ctmp)

ctmp = edge(v_t,identifier,arr_2)
v_t.add_edge(ctmp)

v_n = vertex("final-identifier")
ctmp = edge(v_i,v_n,'n')
v_i.add_edge(ctmp)

ctmp = edge(v_i,BOG,arr)
v_i.add_edge(ctmp)

ctmp = edge(v_i,identifier,arr_2)
v_i.add_edge(ctmp)

v_u = vertex("final-identifier")
ctmp = edge(v_n,v_u,'u')
v_n.add_edge(ctmp)

ctmp = edge(v_n,BOG,arr)
v_n.add_edge(ctmp)

ctmp = edge(v_n,identifier,arr_2)
v_n.add_edge(ctmp)

v_e = vertex("final-keyword")
ctmp = edge(v_u,v_e,'e')
v_u.add_edge(ctmp)

ctmp = edge(v_u,BOG,arr)
v_u.add_edge(ctmp)

ctmp = edge(v_u,identifier,arr_2)
v_u.add_edge(ctmp)

ctmp = edge(v_e,BOG,arr)
v_e.add_edge(ctmp)

ctmp = edge(v_e,identifier,arr_2)
v_e.add_edge(ctmp)
# struct, short sizeof static scanf
v_s= vertex("final-identifier")
ctmp = edge(BOG,v_s,'s')
BOG.add_edge(ctmp)

v_tt = vertex("final-identifier")
ctmp = edge(v_s,v_tt,'t')
v_s.add_edge(ctmp)

v_a = vertex("final-identifier")
ctmp = edge(v_tt,v_a,'a')
v_tt.add_edge(ctmp)

v_t = vertex("final-identifier")
ctmp = edge(v_a,v_t,'t')
v_a.add_edge(ctmp)

ctmp = edge(v_a,BOG,arr)
v_a.add_edge(ctmp)

ctmp = edge(v_a,identifier,arr_2)
v_a.add_edge(ctmp)

v_i = vertex("final-identifier")
ctmp = edge(v_t,v_i,'i')
v_t.add_edge(ctmp)

ctmp = edge(v_t,BOG,arr)
v_t.add_edge(ctmp)

ctmp = edge(v_t,identifier,arr_2)
v_t.add_edge(ctmp)

v_c = vertex("final-keyword")
ctmp = edge(v_i,v_c,'c')
v_i.add_edge(ctmp)

ctmp = edge(v_i,BOG,arr)
v_i.add_edge(ctmp)

ctmp = edge(v_i,identifier,arr_2)
v_i.add_edge(ctmp)

ctmp = edge(v_c,BOG,arr)
v_c.add_edge(ctmp)

ctmp = edge(v_c,identifier,arr_2)
v_c.add_edge(ctmp)

v_r = vertex("final-identifier")
ctmp = edge(v_tt,v_r,'r')
v_tt.add_edge(ctmp)

ctmp = edge(v_tt,BOG,arr)
v_tt.add_edge(ctmp)

ctmp = edge(v_tt,identifier,arr_2)
v_tt.add_edge(ctmp)

v_u = vertex("final-identifier")
ctmp = edge(v_r,v_u,'u')
v_r.add_edge(ctmp)

ctmp = edge(v_r,BOG,arr)
v_r.add_edge(ctmp)

ctmp = edge(v_r,identifier,arr_2)
v_r.add_edge(ctmp)

v_c = vertex("final-identifier")
ctmp = edge(v_u,v_c,'c')
v_u.add_edge(ctmp)

ctmp = edge(v_u,BOG,arr)
v_u.add_edge(ctmp)

ctmp = edge(v_u,identifier,arr_2)
v_u.add_edge(ctmp)

v_t = vertex("final-keyword")
ctmp = edge(v_c,v_t,'t')
v_c.add_edge(ctmp)

ctmp = edge(v_c,BOG,arr)
v_c.add_edge(ctmp)

ctmp = edge(v_c,identifier,arr_2)
v_c.add_edge(ctmp)

ctmp = edge(v_t,BOG,arr)
v_t.add_edge(ctmp)

ctmp = edge(v_t,identifier,arr_2)
v_t.add_edge(ctmp)

v_c = vertex("final-identifier")
ctmp = edge(v_s,v_c,'c')
v_s.add_edge(ctmp)

v_a = vertex("final-identifier")
ctmp = edge(v_c,v_a,'a')
v_c.add_edge(ctmp)

ctmp = edge(v_c,BOG,arr)
v_c.add_edge(ctmp)

ctmp = edge(v_c,identifier,arr_2)
v_c.add_edge(ctmp)

v_n = vertex("final-identifier")
ctmp = edge(v_a,v_n,'n')
v_a.add_edge(ctmp)

ctmp = edge(v_a,BOG,arr)
v_a.add_edge(ctmp)

ctmp = edge(v_a,identifier,arr_2)
v_a.add_edge(ctmp)

v_f = vertex("final-keyword")
ctmp = edge(v_n,v_f,'f')
v_n.add_edge(ctmp)

ctmp = edge(v_n,BOG,arr)
v_n.add_edge(ctmp)

ctmp = edge(v_n,identifier,arr_2)
v_n.add_edge(ctmp)

ctmp = edge(v_f,BOG,arr)
v_f.add_edge(ctmp)

ctmp = edge(v_f,identifier,arr_2)
v_f.add_edge(ctmp)

v_w = vertex("final-identifier")
ctmp = edge(v_s,v_w,'w')
v_s.add_edge(ctmp)

v_i = vertex("final-identifier")
ctmp = edge(v_w,v_i,'i')
v_w.add_edge(ctmp)

ctmp = edge(v_w,BOG,arr)
v_w.add_edge(ctmp)

ctmp = edge(v_w,identifier,arr_2)
v_w.add_edge(ctmp)

v_t = vertex("final-identifier")
ctmp = edge(v_i,v_t,'t')
v_i.add_edge(ctmp)

ctmp = edge(v_i,BOG,arr)
v_i.add_edge(ctmp)

ctmp = edge(v_i,identifier,arr_2)
v_i.add_edge(ctmp)

v_c = vertex("final-identifier")
ctmp = edge(v_t,v_c,'c')
v_t.add_edge(ctmp)

ctmp = edge(v_t,BOG,arr)
v_t.add_edge(ctmp)

ctmp = edge(v_t,identifier,arr_2)
v_t.add_edge(ctmp)

v_h = vertex("final-keyword")
ctmp = edge(v_c,v_h,'h')
v_c.add_edge(ctmp)

ctmp = edge(v_c,BOG,arr)
v_c.add_edge(ctmp)

ctmp = edge(v_c,identifier,arr_2)
v_c.add_edge(ctmp)

ctmp = edge(v_h,BOG,arr)
v_h.add_edge(ctmp)

ctmp = edge(v_h,identifier,arr_2)
v_h.add_edge(ctmp)

v_i = vertex("final-identifier")
ctmp = edge(v_s,v_i,'i')
v_s.add_edge(ctmp)

v_z = vertex("final-identifier")
ctmp = edge(v_i,v_z,'z')
v_i.add_edge(ctmp)

ctmp = edge(v_i,BOG,arr)
v_i.add_edge(ctmp)

ctmp = edge(v_i,identifier,arr_2)
v_i.add_edge(ctmp)

v_e = vertex("final-identifier")
ctmp = edge(v_z,v_e,'e')
v_z.add_edge(ctmp)

ctmp = edge(v_z,BOG,arr)
v_z.add_edge(ctmp)

ctmp = edge(v_z,identifier,arr_2)
v_z.add_edge(ctmp)

v_o = vertex("final-identifier")
ctmp = edge(v_e,v_o,'o')
v_e.add_edge(ctmp)

ctmp = edge(v_e,BOG,arr)
v_e.add_edge(ctmp)

ctmp = edge(v_e,identifier,arr_2)
v_e.add_edge(ctmp)

v_f = vertex("final-keyword")
ctmp = edge(v_o,v_f,'f')
v_o.add_edge(ctmp)

ctmp = edge(v_o,BOG,arr)
v_o.add_edge(ctmp)

ctmp = edge(v_o,identifier,arr_2)
v_o.add_edge(ctmp)

ctmp = edge(v_f,BOG,arr)
v_f.add_edge(ctmp)

ctmp = edge(v_f,identifier,arr_2)
v_f.add_edge(ctmp)

v_h = vertex("final-identifier")
ctmp = edge(v_s,v_h,'h')
v_s.add_edge(ctmp)

ctmp = edge(v_s,BOG,arr)
v_s.add_edge(ctmp)

ctmp = edge(v_s,identifier,arr_2)
v_s.add_edge(ctmp)

v_o = vertex("final-identifier")
ctmp = edge(v_h,v_o,'o')
v_h.add_edge(ctmp)

ctmp = edge(v_h,BOG,arr)
v_h.add_edge(ctmp)

ctmp = edge(v_h,identifier,arr_2)
v_h.add_edge(ctmp)

v_r = vertex("final-identifier")
ctmp = edge(v_o,v_r,'r')
v_o.add_edge(ctmp)

ctmp = edge(v_o,BOG,arr)
v_o.add_edge(ctmp)

ctmp = edge(v_o,identifier,arr_2)
v_o.add_edge(ctmp)

v_t = vertex("final-keyword")
ctmp = edge(v_r,v_t,'t')
v_r.add_edge(ctmp)

ctmp = edge(v_r,BOG,arr)
v_r.add_edge(ctmp)

ctmp = edge(v_r,identifier,arr_2)
v_r.add_edge(ctmp)

ctmp = edge(v_t,BOG,arr)
v_t.add_edge(ctmp)

ctmp = edge(v_t,identifier,arr_2)
v_t.add_edge(ctmp)
# main
v_m = vertex("final-identifier")
ctmp = edge(BOG,v_m,'m')
BOG.add_edge(ctmp)

v_a = vertex("final-identifier")
ctmp = edge(v_m,v_a,'a')
v_m.add_edge(ctmp)

ctmp = edge(v_m,identifier,arr_2)
v_m.add_edge(ctmp)

v_i = vertex("final-identifier")
ctmp = edge(v_a,v_i,'i')
v_a.add_edge(ctmp)

ctmp = edge(v_a,identifier,arr_2)
v_a.add_edge(ctmp)

v_n = vertex("final-keyword")
ctmp = edge(v_i,v_n,'n')
v_i.add_edge(ctmp)

ctmp = edge(v_i,identifier,arr_2)
v_i.add_edge(ctmp)

ctmp = edge(v_n,BOG,arr)
v_n.add_edge(ctmp)

ctmp = edge(v_n,identifier,arr_2)
v_n.add_edge(ctmp)

ctmp = edge(BOG,identifier,arr_2)
BOG.add_edge(ctmp)

# what the type function return program types works with the graph
def WTT(x):
    if(x.isdigit()):
        return "constant"
    if(x.isalpha()):
        return "alphabet"
    if x in punctuators:
        return "punctuator"
    if x in operators:
        return "operator"
    if x == " ":
        return "space"
    if x == "_":
        return "underscore"
    return x
# lexical Error handler
def Error(x):
    if(x.alpha()):
        tokens_arr.append("Error::identifier error , in line:"+str(line)+" character:"+str(character))
    if(x.digit()):
        tokens_arr.append("Error::identifier error , in line:"+str(line)+" character:"+str(character))
    if(operators in x):
        tokens_arr.append("Error::operator error , in line:"+str(line)+" character:"+str(character))
## Beginning of Lexical main
identifier_arr = []
current_node = BOG
current_string = ""
line = 0
character=0
length = len(code)
z = -1
delay_in = ''
while(z<length-1):
    z += 1
    i = code[z]
    #print(i)
    if i=='"':
        #print("str")
        tmp = ""
        tmp += i
        while(1):
            z+=1
            i = code[z]
            tmp += i
            if i=='"' or i=='\0':
                delay_in = ("string"+" :: "+tmp)
                break
        continue
    elif i=="'":
        #print("char")
        tmp = "'"
        while(1):
            z+=1
            i = code[z]
            tmp += i
            if i!="'" or i == '\0':
                delay_in = ("char"+" :: "+tmp)
                break
        continue
    if i=='\n':
        line += 1
        character = 0
        continue
    elif i=='\t':
        character += 1
        z+=1
        continue
    elif i=='\0':
        break
    character += 1
    res = WTT(i)
    find = 0
    for j in current_node.connected_in_edges:
        if find == 1:
            find =0
            break
        for w in j.input_types:
            if (i == w) or (res == w):
                find = 1
                if j.out_vertex == BOG:
                    arr = current_node.current_type[6:]
                    if arr == "operator":
                        if current_string in operators:
                            tokens_arr.append(arr+" :: "+current_string)
                            if len(delay_in) != 0:
                                tokens_arr.append(delay_in)
                                delay_in = ''
                            current_string = ""
                            current_node = BOG
                            z-=1
                            break
                        else:
                            tokens_arr.append("Error::identifier miss-match , in line:"+str(line)+" character:"+str(character))
                            break
                    if arr == "identifier":
                        identifier_arr.append(current_string)
                    tokens_arr.append(arr+" :: "+current_string)
                    if len(delay_in) != 0:
                        tokens_arr.append(delay_in)
                        delay_in = ''
                    current_string = ""
                    current_node = BOG
                    z-=1
                else:
                    current_node = j.out_vertex
                    current_string += i
                break
            elif w == "error" or w == "others":
                find = 1
                ERROR(i)
                break
for i in tokens_arr:
    print(i)