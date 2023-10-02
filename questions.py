def term(a):
    if a%2==0:
        list=[]
        for i in range(1,a):
            if i%2==0:
                list[i]=i-1
            else:
                list[i]=i+1
        print(list)
           
            
x=int(input('enter term'))


term(x)



    
