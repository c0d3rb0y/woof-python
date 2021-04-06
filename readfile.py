import time
# Using readlines()
file1 = open("testfile.howl", 'r')
Lines = file1.readlines()
count = 0
# Strips the newline character
for line in Lines:
    count += 1
    rawin = line.strip()
    num1 = 0;
    num2 = 0;
    cmdfound = 0;
    if ("wait" in rawin[:4]):
        waittime = 0
        cmdfound = 1;
        waittime = int(rawin[5:])
        time.sleep(waittime)

    if ("add" in rawin[:3]):
        cmdfound = 1;
        spaceloc = rawin[4:].find(" ") + 4;
        #print("Space Location:",spaceloc);
        if spaceloc == -1:
            print("Failed to find space between numbers");
        try:
            num1 = float(rawin[4:spaceloc]);
            #print("Float 1:",num1);
        except:
            print("Failed to find number.");
        try:
            num2 = float(rawin[spaceloc:]);
            #print("Float 2:",num2);
        except:
            print("Failed to find number.");
        print(num1+num2);

    if ("sub" in rawin[:3]):
        cmdfound = 1;
        spaceloc = rawin[4:].find(" ") + 4;
        #print("Space Location:",spaceloc);
        if spaceloc == -1:
            print("Failed to find space between numbers");
        try:
            num1 = float(rawin[4:spaceloc]);
            #print("Float 1:",num1);
        except:
            print("Failed to find number.");
        try:
            num2 = float(rawin[spaceloc:]);
            #print("Float 2:",num2);
        except:
            print("Failed to find number.");
        print(num1-num2);

    if ("mult" in rawin[:4]):
        cmdfound = 1;
        spaceloc = rawin[5:].find(" ") + 5;
        #print("Space Location:",spaceloc);
        if spaceloc == -1:
            print("Failed to find space between numbers");
        try:
            num1 = float(rawin[5:spaceloc]);
            #print("Float 1:",num1);
        except:
            print("Failed to find number.");
        try:
            num2 = float(rawin[spaceloc:]);
            #print("Float 2:",num2);
        except:
            print("Failed to find number.");
        print(num1*num2);

    if ("div" in rawin[:3]):
        cmdfound = 1;
        spaceloc = rawin[4:].find(" ") + 4;
        #print("Space Location:",spaceloc);
        if spaceloc == -1:
            print("Failed to find space between numbers");
        try:
            num1 = float(rawin[4:spaceloc]);
            #print("Float 1:",num1);
        except:
            print("Failed to find number.");
        try:
            num2 = float(rawin[spaceloc:]);
            #print("Float 2:",num2);
        except:
            print("Failed to find number.");
        print(num1/num2);

            
    if ("say" in rawin[:3]):
        print(rawin[4:]);
        cmdfound = 1;
        
    if ("close" in rawin[:5]):
        exit();
        cmdfound = 1;

    if (cmdfound == 0):
        try:
            exec(rawin);
        except:
            print("Error:", rawin,"is not valid Woof or Python syntax.");
