
print("Welcome")
a=float(input("What was the total bill?\n"))
b=int(input("How many people to split the bill?\n"))
c=int(input("What percentage tip would you like to give? 10, 12 or 15\n"))
if(c==10):
    print("Each person should pay:",(((a*0.1)+a)/b))
elif(c==12):
    print("Each person should pay:",(((a*0.12)+a)/b))
elif(c==15):
    print("Each person should pay:",(((a*0.15)+a)/b))
    


