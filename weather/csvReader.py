import csv
from pprint import pprint
with open('NYPD_Motor_Vehicle_Collisions.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        for data in row:
            print(data.strip()+"\n")

