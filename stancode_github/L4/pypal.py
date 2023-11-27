
WITHDRAW_LIMIT = 1000
MONEY = 0


class Pypal:
    def __init__(self, name, money=MONEY, limit=WITHDRAW_LIMIT):
        self._n = name
        self.__m = money
        self.l = limit

    def get_amount(self):
        return self.__m

    def set_newname(self, newname):
        self._n = newname
        print('Done')

    def withdraw(self, amount):
        if amount > self.l:
            print('Exceed limit')
        elif amount > self.__m:
            print('Illegal withdraw')
        else:
            self.__m -= amount
            print(f'{self._n} remains: {self.__m}')

    def __str__(self):   # toString
        return f'{self._n} remains {self.__m}/ limits:{self.l}'


def test():
    obj = Pypal('Ben', money=1000, limit=700)
    print(obj)


if __name__ == '__main__':
    print('Thank you')
    test()

