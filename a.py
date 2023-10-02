def term(a):
    while 0<a and a<100:
    if a%2==0:
        list=[]
        i=1
        while i<=a:
           list.append(i+1)
           list.append(i)
           i=i+2
        return list
    else:
        return -1

x=int(input())
print(term(x))
