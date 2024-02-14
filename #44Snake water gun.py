import random

s = int(input("Enter '0' for snake '1' for water and '2' for gun:"))
c = random.randint(0, 2)
print(c)

lst = [["Draw", "You won", "You lose"], ["You lose", "Draw", "You won"], ["You won", "You lose", "Draw"]]
print(lst[s][c])