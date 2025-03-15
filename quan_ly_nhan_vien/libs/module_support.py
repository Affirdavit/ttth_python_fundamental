import csv
def read_file(_path):
    f = open(_path, 'r', encoding='utf-8')
    content = csv.reader(f)
    return content
    f.close()

def print_file(content):
    for row in content:
        print(f"{row[0]:15}{row[1]:30}{row[2]:15}{row[3]:15}{row[4]:15}{row[5]:15}{row[6]:15}")