#import text script file
def read_file(file):
    f = open(file, 'r')
    content = f.read()
    f.close()
    return content

file_text = read_file(file + '.txt')
print(file_text)