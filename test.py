
from datetime import datetime
def markAttendance(name):
    with open('Attendance.csv', 'r+') as f:
        myDataList = f.readlines()
        if myDataList == []:
            f.write("Name , Time")
            myDataList = ["Name , Time"]
            print("Yes")


        nameList = []
        for line in myDataList:
            entry = line.split(',')
            nameList.append(entry[0])
            if name not in nameList:
                now = datetime.now()
                dtString = now.strftime('%H:%M:%S')
                f.writelines(f'\n{name},{dtString}')
                print("updated")
                
markAttendance("Rajat")