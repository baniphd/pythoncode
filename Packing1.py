with open("design.nets","r") as f:
    with open('read.txt','a') as f1:
        doIHaveToCopyTheLine=False
        for line in f.readlines():
            if 'net net_' in line:
                    doIHaveToCopyTheLine=True
                    if doIHaveToCopyTheLine:
                        f1.write(line)
