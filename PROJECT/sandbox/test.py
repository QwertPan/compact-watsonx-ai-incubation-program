import csv
from datetime import date
from io import StringIO
sched_raw = """2024-07-30,17:00-18:30,"Email Campaign"
2024-07-30,18:30-19:00,"Break"
2024-07-30,19:00-20:00,"Team Check-In"
2024-07-31,17:00-19:00,"Market Research"
2024-07-31,19:00-19:30,"Break"
2024-07-31,19:30-21:00,"Invoice Processing"
2024-08-01,17:00-18:30,"System Update\""""
f = StringIO(sched_raw)
r = csv.reader(f)

arr = []
for row in r:
    arr.append(row)
print(arr)
nf = open("sched.csv", "w")
nfwriter = csv.writer(nf)
for row in arr:
    nfwriter.writerow(row)
nf.close()

nf = open("sched.csv", "r")
csvf = csv.reader(nf)
arr = []
for row in csvf:
    arr.append(row)
print("New thing:\n", arr)

#sched_arr = [["", "19:20-20:10"]]
#time_arr = [[int(sched_arr[0][1][0:2]), int(sched_arr[0][1][3:5])], [int(sched_arr[0][1][6:8]), int(sched_arr[0][1][9:11])]]
#time = (time_arr[1][0]-time_arr[0][0])*60 + (time_arr[1][1]-time_arr[0][1])
#print(time_arr)
#print(time)