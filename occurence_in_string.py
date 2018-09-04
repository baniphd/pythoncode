occur = []                         # The list where we will store results.
substr = "design"                        # Substring to use for search.
with open ('design.aux', 'rt') as in_file:        # open file for reading text.
        for linenum,line in enumerate(in_file):    # Keep track of line numbers
            if line.lower().find(substr) != -1: #If case-insensitive substring search matches, then:
                occur.append((linenum, line.rstrip('\n'))) # strip linebreaks, store line and line number in list as tuple.
                for linenum, line in occur:              # Iterate over the list of tuples, and
                    print("Line ", linenum, ": ", line, sep='')  # print results as "Line [linenum]: [line]".
                    
