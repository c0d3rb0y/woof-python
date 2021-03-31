import time;
def cmd():
    print("Loading woof");
    saydef = "say message - says whatever you replace message with\n"
    closedef = "close - closes the program\n"
    helpdef = "help - shows all the commands\n"
    mathdef = "add 1 1, sub 1 1, mult 1 1, div 1 1 - replace 1 with whatever you want to use in the equation. add = add, sub = subtract, mult = multiply, and div = divide\n"
    amogusdef = "amogus - red is sus, vote him out"
    cmdlist1 = ["say", "close", "help", "add", "sub", "mult", "div", "amogus"]
    cmdlist2 = ["say", "close", "help", "add", "sub", "mult", "div", "amogus"]
    cmdlist3 = ["say", "close", "help", "add", "sub", "mult", "div", "amogus"]
    if cmdlist1 != cmdlist2:
        print("Error with commands detected. Woof may not function correctly.");
    else:
        if (cmdlist1 == cmdlist2) and (cmdlist1 != cmdlist3) and (cmdlist2 != cmdlist3):
            print("This is a developer version. Not everything will work correctly.");
    print("Woof is ready - type help for help");
    while 1 == 1:
        num1 = 0;
        num2 = 0;
        cmdfound = 0;
        rawin = input(">> ");
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
        
        if ("help" in rawin[:4]):
            print("Commands:\n",saydef,closedef,helpdef,mathdef);
            cmdfound = 1;
        
        if (("amogus" in rawin) and (cmdfound == 0)):
            print("When the impostor is sus!");
            cmdfound = 1;
        
        if (cmdfound == 0):
            try:
                exec(rawin);
            except:
                print("Error:", rawin,"is not valid Woof or Python syntax.");
#startoptions is unused we dont need this code, but im keep it for later if i ever need it again.
                
#def startoptions(input):
#    if (input == "1"):
#        print("Starting Woof");
#        cmd();
#    else:
#        if (input == "2"):
#            exit()
#        else:
#            print("you werent supposed to do that... i have no idea what you just said im literally programmed to know 2 things");
print(" __      __              _____ ");
print("/  \    /  \____   _____/ ____\ ");
print("\   \/\/   /  _ \ /  _ \   __\ ");
print(" \        (  <_> |  <_> )  |");
print("  \__/\  / \____/ \____/|__|   ");
print("       \/                   ");
print("Version Alpha 1.2");
time.sleep(1);
print("Starting Woof");
cmd();
