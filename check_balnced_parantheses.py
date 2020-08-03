def check_brackets(str1):
    stack=[]
    top=0
    first=["(","{","["]
    second=[")","}","]"]
    for i in str1:
        if i in first:
            stack.append(i)
            top=top+1
        if i in second:
            stack.append(i)
            top=top+1
        elif i!=second or i!=first:
            pass
            x=len(stack)
    print("parantheses::",stack)

    if top%2==1:
            print("unbalanced")
    if top%2==0:
        if stack[0]==")" or stack[x]=="(":
            print("unbalnced")
        else:
            print("balanced")
        
str1=input()
check_brackets(str1)

    
