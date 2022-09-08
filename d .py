number=int(input("enter the number"))
reversenumber=0
while number>0:
        reminder=number%10
        reversenumber=reversenumber*10+reminder
        number=number//10
        print(reversenumber)
        
        print("enter the input value as integers only")
