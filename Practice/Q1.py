number1 = int(input("please Inter number :"))
number2 = int(input("Please Inter number :"))
if number1 < number2 :
    for i in range(number1 , number2) :
        print(i)
else :
    for i in range(number2 , number1 ) :
        print(i)
