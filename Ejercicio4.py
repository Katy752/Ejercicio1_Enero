for n in range(1, 101):
    if not n%3:
        if not n%5:
            print('FizzBuzz')
        else:
            print('Fizz')
    else:
        if not n%5:
            print('Buzz')
        else:
            print(n)
