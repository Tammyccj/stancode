
from pypal import Pypal


def bank():
    j_account = Pypal('Jerry', money=1000, limit=700)
    j_account.withdraw(1000)
    j_account.set_newname('Jelly')
    j_account.withdraw(700)
    j_account.withdraw(700)
    amount = j_account.get_amount()
    print('Amount:', amount)



if __name__ == '__main__':
    bank()

