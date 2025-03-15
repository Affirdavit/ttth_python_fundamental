def read_file(_path):
    f = open(_path, 'r', encoding='utf-8')
    content = f.read()
    f.close()
    return content

def write_file(_path):
    f = open(_path, 'a', encoding='utf-8')
    new_content = '\n'
    new_content += input("Nhap noi dung moi: ")
    f.write(new_content)
    f.close()

def stat(_path):
    f = open(_path, 'r', encoding='utf-8')
    num_line, num_word, num_char = 0, 0, 0
    for row in f:
        num_line += 1
        lst_word = row.split()
        num_word += len(lst_word)
        num_char += len(row)
    return num_line, num_word, num_char