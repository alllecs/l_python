
text = []
with open("test_new2.4.in.txt", "r") as f:
    for line in f:
#        line = line.rstrip()
        text.append(line.rstrip())
#        print(line)
text.reverse()
with open("test_new2.4.out.txt", "w") as f:
    for line in text:
#        print(line)
        f.write("\n".join(line))

#lines = open("input.txt").readlines()
#with open("output.txt", "w") as out:
#   out.writelines(reversed(lines))
#
