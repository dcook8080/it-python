 from banner import banner
import os

banner("HTML Tag Counter" , "Dylan Cook")


def load(htmlfile):
    data = []
    print(f".....loading from {htmlfile}")
    if os.path.exists(htmlfile):
        with open(htmlfile) as fin:
            for entry in fin.readlines():
                data.append(entry)
    return data


def tag_count(line):
    tag_num = 0
    previous_char = None
    for char in line:
        if char != "/" and previous_char == "<":
            tag_num += 1
        previous_char = char
    return tag_num


num_tags = 0
print(" Welcome to HTML Tag Counter")
print("")
filename = input("Enter HTML file name: ")
htmlfile = load(filename)

for line in htmlfile:
    num_tags += tag_count(line)
print(num_tags)


