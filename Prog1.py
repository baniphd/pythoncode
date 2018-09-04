fname = 'design.aux'
my_string = 'design.'
k=0
with open(fname, 'r') as f:
   for line in f:
       words = line.split()
       for i in words:
           if(i==my_string):
               k=k+1
print("Occurrences of the word:")
print(k)
