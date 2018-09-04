# File object

with open('text','r') as rf:
 with open('text_copy','w') as wf:
     for line in rf:
       wf.write(line)
