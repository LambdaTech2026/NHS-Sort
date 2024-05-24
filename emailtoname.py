import csv
from teacherdetect import * 

def search(email):
  with open("teacheremails.csv", mode='r') as data:
    csv_reader = csv.reader(data)
    for row in csv_reader:
      if accuracy(row, email):
        return row[0]
    return "None"


def accuracy(row, email):
  score = 0
  name1 = giveName(row[1]).strip()
  name2 = giveName(email).strip()
  for i in range(len(name2)):
      if i < len(name1):
          if name1[i].lower() == name2[i].lower():
              score += 1

  if(len(name2) != 0):
    accuracy = (score / len(name2)) * 100
  else:
    return False
  if accuracy >= 80:
      with open("accuracy.txt", mode='a') as doc:
          doc.write(row[0] + ": " + str(accuracy) + "\n")
      return True
  else:
      return False


