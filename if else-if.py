a=int(input("Enter the 1st Number:"));
b=int(input("Enter the 2nd Number:"));
c=int(input("Enter the 3rd Number:"));
if a>b and a>c:
    print("The max number is:",a);
elif b>c and b>a:
     print("The max number is:",b);
else:
    print("The max number is:",c);
print("Thank You...");