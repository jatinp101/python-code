#9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages.
#  The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. 
# The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file.
#  After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

email_freq = dict()

for line in handle:
    line = line.rstrip()
    wrds = line.split()

    if 'From' not in wrds: continue

    email_freq[wrds[1]] = email_freq.get(wrds[1],0) + 1

most_email = None
most_count = None

for email in email_freq:
    count = email_freq[email]
    if most_count == None or most_count < count:
        most_email = email
        most_count = count

print(most_email, most_count)
        