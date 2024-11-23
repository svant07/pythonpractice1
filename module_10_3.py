from threading import Thread, Lock
import random
from time import sleep
import threading

#lock = threading.Lock()
class Bank(Thread):
    def __init__(self):
        self.balance = 0
        super().__init__()
        self.lock = Lock()

    def deposit(self):
        for i in range(100):
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            a = random.randint(50,500)
            self.balance += a
            print(f'Пополнение: {a}. Баланс: {self.balance}')
            sleep(0.001)

    def take(self):
        for i in range(100):
            b = random.randint(50,500)
            print(f'Запрос на {b}')
            if b <= self.balance:
                self.balance -= b
                print(f'Снятие: {b}. Баланс: {self.balance}')
            else:
                print(f'Запрос отклонён, недостаточно средств')
                self.lock.acquire()
            sleep(0.001)


bk = Bank()

th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')

