import os
from datetime import datetime

path = input('Enter the location where you want to create the attendance log file: ')
'''Please add the path were you want your attendance log to be created'''


def makeFileAttend():
    filePnt = open(f'{path}/Attendance.csv', 'w+')
    filePnt.write(f'Name,Date,Time')
    filePnt.close()


def makeAttendance(name):
    with open(f'{path}/Attendance.csv', 'r+') as f:
        nameList = []
        attendanceList = f.readlines()
        for line in attendanceList:
            entry = line.split(',')
            nameList.append(entry[0])
        if name not in nameList:
            timeDateNow = datetime.now()
            dateToday = timeDateNow.strftime("%B %d %Y")
            timeNow = timeDateNow.strftime("%H:%M:%S")
            f.write(f'\n{name},{dateToday},{timeNow}')

    f.close()
