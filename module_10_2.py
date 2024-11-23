import threading
from time import sleep, time

class Knight(threading.Thread):

    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power


    def timer(self, counter):
        counter = time.ctime(time.time())



    def run(self):
        enemies = 100
        days = 0
        print(f'{self.name}, на нас напали!')
        while enemies > 0:
            sleep(1)
            days +=1
            enemies -= self.power
            #if enemies < 1:
             #   enemies = 0
            print(f'{self.name} сражается {days} суток, осталось {enemies} воинов врага.')
        print(f'{self.name} одержал победу спустя {days} дней(я)!')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print(f'Все битвы закончились!')
