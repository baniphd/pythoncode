my_file = 'Auxilary.txt'

my_string = 'design.'

infile = open(my_file,"r")

 

numlines = 0

found = 0

for line in infile:

    numlines += 1

    found += line.count(my_string)

infile.close()

 
print (my_string,"sting was found", found, "times")
