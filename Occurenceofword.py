#File object

fname = input("Enter file name: ")
#print(fname)
word=input("Enter word to be searched:")
k = 0
with open(fname, 'r') as f:
    for line in f:
        words = line.split()
        for i in words:
	#	print(words)
          if(i==word):
                k=k+1
print("Occurrences of the word:")
print(k)
