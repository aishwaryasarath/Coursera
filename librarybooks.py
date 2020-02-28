fhand = open('library-books.txt')
count = 0
for line in fhand:
    line = line.rstrip()
    if line.startswith('Title: '):
        print(line.lstrip('Title:'))
