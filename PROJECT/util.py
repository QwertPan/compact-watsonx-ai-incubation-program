import csv
def rtime2len(rtime): # convert <24h>-<24h> format to length in minutes
    # reference: 19:20-20:10
    # 20-19=1; 1*60=60
    # 10-20=-10; 60-10=50
    # 50 minutes

    # get time numbers into array by extracting substrings
    time_arr = [[int(rtime[0:2]), int(rtime[3:5])], [int(rtime[6:8]), int(rtime[9:11])]]
    # calculate time
    time = (time_arr[1][0]-time_arr[0][0])*60 + (time_arr[1][1]-time_arr[0][1])

    return time
