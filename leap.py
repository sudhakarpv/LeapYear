user= input("Enter Random Year")
x=int(user)
if(x%4==0 and x%100!=0 or x%400==0):
    print("Yes Leap Year")
else:
    print("No")
