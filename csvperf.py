import csv
# import numpy as np 
# import matplotlib.pyplot as plt 

# with open('performance.csv') as csv_file:
#     csv_reader = csv_reader(csv_file, delimiter=',')
    
f = open('performance.csv')
csv_f = csv.reader(f)

for row in csv_f:    
	my_list = [0, 1, 2, 3, 4]
	my_set = set(my_list)


    print(my_set)


    
