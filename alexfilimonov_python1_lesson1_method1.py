x = '0'
x = input("Enter whole positive number x:")
if int(x)<=0 :
    print("Entered number is not in acceptable format")
else :
    i=0	
    maxs=0
    while i<len(x) :	
        if maxs < int(x[i]) :	
            maxs = int(x[i])	
        i=i+1	
    print("The max digit in",x,"is", maxs)	