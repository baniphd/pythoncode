import re
err_occur = []                         # The list where we will store results.
pattern = re.compile("net_", re.IGNORECASE)  # Compile a case-insensitive regex pattern.
with open ('design.nets', 'rt') as in_file:        # open file for reading text.
    for linenum, line in enumerate(in_file):        # Keep track of line numbers.
        if pattern.search(line) != None:          # If substring search finds a match,
            err_occur.append((linenum, line.rstrip('\n'))) # strip linebreaks, store line and line number in list as tuple.
            for linenum, line in err_occur:              # Iterate over the list of tuples, and
                #print("Line ", linenum, ": ", line, sep='') # print results as "Line [linenum]: [line]".
                    
