import random

n = int(input("Enter 0 for coding and 1 for decoding:"))
st = input("Enter the statement:")
final = ""
words = st.split(" ")
if n==0:
    for ele in words:
        if len(ele)==2:
            ele = ele[1]+ele[0]
        elif len(ele)>=3:
            ele = ele[1:]+ele[0]
            x = 3
            while(x):
                n = random.randint(97, 122)
                ele = chr(n) + ele
                x -= 1
            x = 3
            while(x):
                n = random.randint(97, 122)
                ele = ele + chr(n)
                x -= 1
        final += ele + " "
if n==1:
    for ele in words:
        if len(ele)==2:
            ele = ele[1]+ele[0]
        elif len(ele)>=3:
            ele = ele[3:len(ele)-3]
            ele = ele[len(ele)-1]+ele[:len(ele)-1]
        final += ele + " "
print(final)