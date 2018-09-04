    def find(net, design.nets, nets.txt):
      with open(infile) as a, open(outfile, 'w') as b:
       for line in a:
        if substr in line:
         b.write(line + '\n')

    # Example usage:
    find('test string', 'a.txt', 'b.txt')
