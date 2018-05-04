class Fizzbuzz:

    def run(num):
        if num % 15 == 0:
            return 'Fizzbuzz'
        elif num % 3 == 0:
            return 'Fizz'
        elif num % 5 == 0:
            return 'Buzz'
        else:
            return num
