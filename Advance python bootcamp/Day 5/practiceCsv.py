import csv

file = open('data.csv','w')

datawrite=csv.writer(file)

header = ['name','roll']
body = [
    ['abhinav','0503'],
    ['bhanu teja','051A']
]
datawrite.writerow(header)
datawrite.writerows(body)
file.close()