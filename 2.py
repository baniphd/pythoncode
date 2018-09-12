import re
pattern = re.compile("o", re.IGNORECASE)  # Compile a case-insensitive regex pattern.
with open ('PackingDemo.txt', 'rt') as in_file:
   with  open('read1.txt', 'w') as outfile:
        copy = False
        for linenum, line in enumerate(in_file):# Keep track of line numbers.
            if "net" in line:
                print(line)
                outfile.write(line)
            if pattern.search(line) != None:          # If substring search finds a match,
                print(line)
                outfile.write(line)
                copy = False
            elif line.strip() == "endnet":
                    copy = True
            elif copy:
                           outfile.write(line)
              # grep text_to_search -C n PckingDemo.txt
               
