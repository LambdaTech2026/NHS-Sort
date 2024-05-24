import csv
from emailtoname import *

teacher_list = []

def getTeacherList(file):
  with open(file, mode='r') as data:
    csv_reader = csv.DictReader(data)
    for row in csv_reader:
      for i in range(1, 6):
        teach = row[f"Teacher #{i} Email"]
        teach = search(teach)
        if (teach not in teacher_list) and (teach != "None"):
          teacher_list.append(teach)
  return teacher_list

