import csv
from teachersort import *
from sortstudents import * 
from formatstudents import *
from emailtoname import *
from teacherdetect import * 

def main(file_path):
  return Format(sortStudents(getTeacherList(file_path), file_path))
  
