def fizzBuzz(r):
    for i in range(1, r):
        if(i % 3 == 0 and i % 5 == 0):
            print(str(i)+" = Fizzbuzz ")
        else:
            if(i % 3 == 0):
                print(str(i)+" = Fizz ")
            else:
                if(i % 5 == 0):
                    print(str(i)+" = Buzz ")
                else:
                    print(str(i))
fizzBuzz(51)