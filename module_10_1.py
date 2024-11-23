from datetime import datetime
from time import sleep
import threading

def write_words(word_count, file_name):
    file = open(file_name, 'a', encoding='utf-8')
    for i in range(1, word_count+1):
        file.write(f'Какое-то слово № {i+1}\n')
        sleep(0.1)
    file.close()
    print(f'Завершилась запись в файл {file_name}')

t1_start = datetime.now()

write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

t1_stop = datetime.now()
t1 = t1_stop - t1_start
print(f'Затраченное время: {t1}')

t2_start = datetime.now()

thread_1 = threading.Thread(target=write_words, args=(10, 'example5.txt'))
thread_2 = threading.Thread(target=write_words, args=(30, 'example6.txt'))
thread_3 = threading.Thread(target=write_words, args=(200, 'example7.txt'))
thread_4 = threading.Thread(target=write_words, args=(100, 'example8.txt'))

thread_1.start()
thread_2.start()
thread_3.start()
thread_4.start()

thread_1.join()
thread_2.join()
thread_3.join()
thread_4.join()

t2_stop = datetime.now()
t2 = t2_stop - t2_start
print(f'Затраченное время: {t2}')


