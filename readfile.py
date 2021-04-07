import time
# Using readlines()
file1 = open("testfile.howl", 'r')
Lines = file1.readlines()

varlist = ["thisisaplaceholder"]
saveused = 0;

count = 0
# Strips the newline character
for line in Lines:
    count += 1
    rawin = line.strip()
    waittime = 0;
    num1 = 0;
    num2 = 0;
    cmdfound = 0;
    syntaxfailed = 0;
    loadedstr = "empty";
    loadedint = 0;
    usablestr = "";
    strtdatbarloc = 0;
    varindex = 0;
    if ("read" in rawin[:4]):
        cmdfound = 1;
        syntaxfailed = 1;
        for string in varlist:
            syntaxfailed = 0;
            #String To Data Barrier Location
            strtdatbarloc = string.find(":=") + 2;
            if(rawin[5:] in string[:strtdatbarloc - 2]):
                print(string[strtdatbarloc:]);

    if ("save" in rawin[:4]):
        cmdfound = 1;
        syntaxfailed = 1;
        if ("new" in rawin[5:]):
            for string in varlist:
                strtdatbarloc = string.find(":=");
                decodedname = string[:strtdatbarloc]
                if ("thisisaplace" in decodedname) and (saveused == 0):
                    saveused = 1;
                    varlist.clear()
                if not(decodedname in rawin[9:]):
                    syntaxfailed = 0;
                    loadedstr = rawin[9:]
                    varlist += [loadedstr + ":=empty"]
                    loadedstr = "empty"
                if decodedname in rawin[9:]:
                    print("ERROR: Saved Item " + decodedname + " already exists.");
                    syntaxfailed = 0;
            
        if ("set" in rawin[5:]):
            syntaxfailed = 1;
            spaceloc = rawin[10:].find(" ") + 10;
            try:
                checkifint2 = int(rawin[spaceloc:])
                for number in varlist:
                    syntaxfailed = 0;
                    #String To Data Barrier Location
                    strtdatbarloc = number.find(":=") + 2;
                    if(rawin[9:spaceloc - 1] in number[:strtdatbarloc - 2]):
                        varindex = varlist.index(rawin[9:spaceloc])
                        varlist[varindex] = string + ":=" + rawin[spaceloc:]
            except:
                for string in varlist:
                    syntaxfailed = 0;
                    #String To Data Barrier Location
                    strtdatbarloc = string.find(":=") + 2;
                    if(rawin[9:spaceloc - 1] in string[:strtdatbarloc - 2]):
                        varindex = varlist.index(string)
                        varlist[varindex] = rawin[9:spaceloc] + ":=" + rawin[spaceloc + 1:]

    if ("wait" in rawin[:4]):
        waittime = 0;
        cmdfound = 1;
        waittime = float(rawin[5:])
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
                print("Error:", rawin,"is not a valid Woof or Python command.");
    if (syntaxfailed == 1):
        print("Error:", rawin,"is not correct Woof or Python syntax.")
