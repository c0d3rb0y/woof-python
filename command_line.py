import time;
def cmd():
    time.sleep(0.2);
    print("Loading woof");
    time.sleep(0.5);
    print("Woof is ready - type help for help");
    while 1 == 1:
        cmdfound = 0;
        rawin = input(">> ");
        if ("say" in rawin[:4]):
            print(rawin[4:]);
            cmdfound = 1;
        if ("close" in rawin[:6]):
            exit();
            cmdfound = 1;
        if ("help" in rawin[:5]):
            print("Commands:\n","say message - says whatever you replace message with\n","close - closes the program\n","help - shows all the commands\n");
            cmdfound = 1;
        if (("amogus" in rawin) and (cmdfound == 0)):
            time.sleep(0.5);
            print("")
            print("When the impostor is sus!");
            cmdfound = 1;
        if (cmdfound == 0):
            try:
                exec(rawin);
            except:
                print("Error:", rawin,"is not a valid Woof or Python command.");
#startoptions is unused we dont need this code, but im keep it for later
def startoptions(input):
    if (input == "1"):
        print("Starting Woof");
        cmd();
    else:
        if (input == "2"):
            exit()
        else:
            print("you werent supposed to do that... i have no idea what you just said im literally programmed to know 2 things");
print(" __      __              _____ ");
print("/  \    /  \____   _____/ ____\ ");
print("\   \/\/   /  _ \ /  _ \   __\ ");
print(" \        (  <_> |  <_> )  |");
print("  \__/\  / \____/ \____/|__|   ");
print("       \/                   ");
print("Version Alpha 1.0");
time.sleep(0.5);
print("Starting Woof");
cmd();
