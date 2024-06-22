print("******WELCOME TO OUR CALCULATOR*****")
while(True):
 print("1.Addition")
 print("2.Subtraction")
 print("3.Multiplication")
 print("4.Quotient")
 print("5.Remainder")
 print("6.Power")
 print("7.Exit")
 try: 
   choice=int(input("Enter your choice:"))
 except:
  print("Wrong choice!!Try Again")
  continue
 if choice==7:
   print("THANK YOU FOR USING OUR CALCULATOR")
   break 
 n1=eval(input("Enter first number:"))
 n2=eval(input("Enter second number:"))

 if choice==1:
   print(f"Addition of two numbers:{n1+n2}")
 elif choice==2:
   print(f"Subtraction of two numbers:{n1-n2}")
 elif choice==3:
   print(f"Multiplication of two numbers:{n1*n2}")
 elif choice==4:
   print(f"Division of two numbers:{n1/n2}") 
 elif choice==5:
   print(f"Remainder of two numbers:{n1%n2}")
 elif choice==6:
   print(f"Power of two numbers:{n1**n2}")       
     
