# Program to create fizzbuzz in python
for i in range(1,51):
    if(i%3==0):
        print(str(i)+"= Fizz")
    else:
        if(i%5==0):
            print(str(i)+"= Buzz")
        else:
            if(i%3==0 and i%5==0):
                print(str(i)+"= Fizzbuzz")
            else:
                print(str(i))            