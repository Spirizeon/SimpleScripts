n = int(input("enter number of characters: "))
import random as r
perd = ""
i = n
while i > 0:
        added_char = chr(r.randint(33,126))
        if added_char.isspace == True:
                continue
        perd += added_char
        i -= 1
print("here is your password: ",perd) 
print("count =",len(perd))
