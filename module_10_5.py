import multiprocessing
from datetime import datetime
from multiprocessing import Pool


def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        while True:
             line = file.readline()
             all_data.append(line)
             if not line:
                 break

files = ['file 1.txt', 'file 2.txt', 'file 3.txt', 'file 4.txt']
start1 = datetime.now()

for f in files:
    print(f)
    read_info(f)

end1 = datetime.now()
time1 =  end1 - start1
print(f'Время работы вызова : {time1}')






if __name__ == '__main__':
    start2 = datetime.now()
    with Pool(4) as p:
        print(p.map(read_info, files))

    end2 = datetime.now()
    time2 = end2 - start2
    print(f'Время работы мультипроцесса : {time2}')



filenames = [f'./file {number}.txt' for number in range(1, 5)]


