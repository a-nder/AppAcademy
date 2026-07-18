while True:
    choice = input("Enter game score: ").strip()
    if choice == "stop":
        print("Game session ended!")
        break
    else:
        score = int(choice)
        if score > 100:
            print("Wow!Thats a new high core")
        else:
            print("Good try, keep playing!")