# Preprocess deleting comments
def delete_comments(s):
    ln = len(s)
    tmp = ""
    i = 0
    while(i<ln-1):
        tmp = ""
        # one line comments //
        if(s[i]=='/' and s[i+1]=='/'):
            j = i
            while(s[j]!='\n'):
                tmp += s[j]
                j+=1
            s = s.replace(tmp ,"")
            ln = len(s)
            continue
        # for more than one line comments /* */
        if(s[i] == '/' and s[i+1] == '*'):
            tmp += "/*"
            j = i + 2
            while(s[j]!='*' or s[j+1]!='/'):
                if(s[j]== '\0'):
                    print("Error: Expected to close the comment with '*/'")
                    return 0
                tmp += s[j]
                j+=1
            s = s.replace(tmp + "*/" ,"")
            ln = len(s)
            continue
        i += 1
    return s

# start of running code      
# read file and save it into an array
aborting = False
fileObj = open(r"main.c","r")
code = fileObj.read()
fileObj.close()

# start of preprocess
res = delete_comments(code)
if(res == 0):
    aborting = True
else: code = res

print(code)
#
# End of Preprocess
#