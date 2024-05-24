import csv
from emailtoname import *

whole_list = []

def sortStudents(teacherlist, file):
  with open(file, mode='r') as data:
    csv_reader = csv.DictReader(data)
    rows = list(csv_reader)  
    for teacher in teacherlist:
      whole_list.append(teacher)
      for row in rows:  
        for i in range(1, 6):
          teach = row[("Teacher #" + str(i) +  " Email")]
          teach = search(teach)
          if teach != "None":
            if teacher.lower() == teach.lower():
              whole_list.append(row['Last Name'])
              whole_list.append(row['First Name'])
              whole_list.append(row["Student ID"])
      whole_list.append("*")
    return whole_list
