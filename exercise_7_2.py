# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0
total = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    line = line.rstrip()
    count += 1
    startingpt = line.find(':')
    line = line[startingpt+1 :]
    line = line.strip()
    total += float(line)

print("Average spam confidence:", total/count)