"""
PROJECT 1 DRAFT
"""

def create_file():
    words = []
    unq = []
    infile = open("test.txt", 'w')
    infile.write("Dan Kahn teaches the course CMPSC131\n")
    infile.write("CMPSC131 is an important course \n")
    infile.close()

    infile2 = open("test.txt", 'r')
    for i in infile2:
        line1 = i.split()
        for j in infile2:
            line2 = j.split()

    words = words + [line1] + [line2]

    print(line1)
    print(line2)
    print(words)

    infile2.close()


create_file()