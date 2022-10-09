#10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. 
# You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

hr_frq = dict()

for line in handle: 
    wrds = line.rstrip().split()
    if 'From' not in wrds: continue
    time = wrds[5]
    hr = time.split(':')[0]
    hr_frq[hr] = hr_frq.get(hr, 0) + 1

tmp = sorted(hr_frq)

for num in tmp :
    print(num, hr_frq[num])