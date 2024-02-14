import random
import time

quetions = ["Who are you?", "Why are you?", "What are you?", "Which are you?", "How are you?", "Who are you?", "Why are you?", "What are you?", "Which are you?", "How are you?", "Who are you?", "Why are you?", "What are you?", "Which are you?", "How are you?","Who are you?"]
rightst = []
answers = ["a","b","b","d","c","a","a","c","b","d","a","a","c","d","d","c"]
rightans1 = ["sahi javab bahut badhia aage badhate he", "sahi javab agla saval", "bahut badhia sahi javab agle prashne ke or badhate he"]
rightans2 = ["kyu laga aapo ki ye sahi he", "aap sure the ki yahi sahi javab he?", "ohooooo sir"]
rakam = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000, 640000, 1250000, 2500000, 500000, "1 crore", "& Crore"]

price = 0
i = 0
print("Please enter answer in lower letter.")
while(1):
    print(quetions[i])
    print("(A)                         (B)")
    print("(C)                         (D)")
    ans = input("kya he aapka javab:")
    if(ans!="a" and ans!="b" and ans!="c" and ans!="d"):
        raise ValueError("Answer should be a or  b or c or d (in lower letters.)")
    if(i>=0 and i<=5 and ans==answers[i]):
        n = random.randint(0, 2)
        print(rightans1[n])
    elif(ans=="quite"):
        price=rakam[i-1]
        break
    elif(ans!=answers[i]):
        print("oho galat javab")
        break
    elif(ans==[i]):
        n = random.randint(0, 2)
        print(rightans2[n])
        time.sleep(1)
        print("sahi javab")
    if(i==4 or i==9):
        price = rakam[i]
    i += 1    
print("aap jite he", price, "rupe")