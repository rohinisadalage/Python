a=int(input("Enter the 1st Number:"));
b=int(input("Enter the 2nd Number:"));
c=int(input("Enter the 3rd Number:"));
if (a>b and a<c) or (a<b and a>c):
    print("The middle number is:",a);
elif (b>a and b<c) or (b<a and b>c):
     print("The middle number is:",b);
else:
    print("The middle number is:",c);
print("Thank You...");