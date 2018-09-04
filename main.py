my_file = 'design.aux'

my_string = 'design.'

with open(my_file,"r") as infile:
    numlines = 0
    found = 0
    for line in infile:
        numlines += 1
        found += line.count(my_string)

#infile.close()
print (my_string,"Design files found", found, "times")
if found ==6 :
     print("All neccessary file found.Ready to go.")
else :
    print("Some file is missing")

# PART 2 - PACKING
