import csv
import sys
from datetime import datetime

def read_file(_path):
    f = open(_path, 'r', encoding='utf-8')
    content = []
    for row in csv.reader(f):
        content.append(row)
    f.close()
    return content

def print_file(content):
    for row in content:
        print(f"{row[0]:15}{row[1]:30}{row[2]:15}{row[3]:30}{row[4]:15}")

def write_file(_path, content):
    f = open(_path, 'w', encoding='utf-8', newline='')
    writer = csv.writer(f)
    writer.writerows(content)
    print("Luu noi dung thanh cong")
    f.close()

# Looking for student who fail a certain course
def search_fail(content):
    ten_mon = input("Nhap ten mon hoc: ")
    lst = []
    for row in content:
        if row[3] == ten_mon.upper() and float(row[4]) < 5:
            lst.append(row)
    return lst

def avg_score(subject_id, content):
    tong_diem = 0
    so_sv = 0
    for row in content:
        if row[2] == subject_id:
            so_sv += 1
            tong_diem += float(row[4])
    return tong_diem / so_sv
