import csv
from csv import writer
from diction import dict

def Format(wholeList):
  key = ""
  value = []
  for item in wholeList:
      if item == "*":
          dict[key] = value
          key = ""
          value = []
      else:
          if not key:
              key = item
          else:
              value.append(item)
  ViewDict()
  return "FORMATED.csv"

def ViewDict():
  headers = ["Name (L)", "Name (F)", "Name (F)", "ID"]
  with open("FORMATED.csv", mode='a') as ret:
    writerObj = writer(ret)
    writerObj.writerow(headers)
    for key, value in dict.items():
        print(f"Teacher: {key}, Students: {value}\n")
        writerObj.writerow([key, "", "", ""])
        count = 0
        while(count < len(value)):
          writerObj.writerow([value[count], value[count + 1], value[count + 1], value[count + 2]])
          count += 3
        writerObj.writerow(["","","",""])


