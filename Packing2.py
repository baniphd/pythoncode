with open('design.nets','r') as infile:
    with  open('read1.txt', 'w') as outfile:
        copy = False
        stringdata = infile.read().replace('net net','net')
        print(stringdata)
        for line in stringdata:
            if line.strip() == "net":
                copy = True
            elif line.strip() == "endnet":
                copy = False
            elif copy:
                  outfile.write(line)
