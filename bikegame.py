bike_started = False  
command = ""  

while True:  
    command = input("> ").lower()  
    if command == "help":
        print("start - to start the bike")
        print("stop - to stop the bike")
        print("quit - to exit")
    elif command == "start":
        if bike_started:
            print("Bike is already started")  
        else:
            bike_started = True  
            print("Bike started...Ready to go")
    elif command == "stop":
        if bike_started:
            bike_started = False  
            print("Bike stopped")
        else:
            print("Bike is already stopped")  
    elif command == "quit":
        break 
    else:
        print("I don't understand")  