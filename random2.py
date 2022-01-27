import time
import random
import csv

start = time.time()

random_list = [str(random.randint(10, 25)) + '\n' for num in range(100000)]

with open('output_of_random2.csv', 'w') as output:
    fields = ['reading']
    output.writelines(random_list)

end = time.time()
print(start - end)