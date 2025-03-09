a=int(input("Enter the English Subject Marks: "));
b=int(input("Enter the Hindi Subject Marks: "));
c=int(input("Enter the Marathi Subject Marks: "));
d=int(input("Enter the Maths Subject Marks "));
e=int(input("Enter the History Subject Marks "));
total=a+b+c+d+e;
percent=(total/500)*100;
if percent>=80:
    print("Congratulations you got a Grade A");
elif percent>=70 and percent<=79:
    print("Congratulations you got a Grade B");
elif percent>=60 and percent<=59:
    print("Congratulations you got a Grade C");
elif percent>50 and percent<=40:
    print("Congratulations you got a Grade D");
else:
    print(" You got a Grade D");
print("Thank You...");