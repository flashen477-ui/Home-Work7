class Calculator:

    @staticmethod
    def checker(func):
        def wrapper(num_1, num_2):
            try:
                func(num_1, num_2)
            except:
                print('We have problems.')
        return wrapper

    @staticmethod
    @checker
    def multiplay(num_1, num_2):
        print(num_1 * num_2)

    @staticmethod
    @checker
    def substract(num_1, num_2):
        print(num_1 - num_2)

    @staticmethod
    @checker
    def divide(num_1, num_2):
        print(num_1 / num_2)

    @staticmethod
    @checker
    def plus(num_1, num_2):
        print(num_1 + num_2)

calculate = Calculator()
calculate.multiplay(10, 12)
calculate.substract(4, 25)

calculate.multiplay('10', '12')
calculate.substract('4', '25')

calculate.divide(36, 6)
calculate.divide('36', '6')

calculate.plus(78, 23)