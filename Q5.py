number = input("Inter 3-digit number :")
num1 = 0
if len(number) == 3 :
  for i in number :
    num1 = num1 + int(i)
  print(f"Sum of digits is {num1}")
else :
  print("The number of digits in the input is not equal to 3")
  
  
  
    
