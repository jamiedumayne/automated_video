def read_text(text_file):
    os.chdir("/home/jamie/Documents/Test/Tiktok_bot/scripts/")
    f = open(text_file, 'r')
    content = f.read()
    f.close()

file = 'test_penguin.txt'
read_text(file)