queue = []

while True:
    ch = input("1.Add 2.Process 3.Show 4.Cancel 5.Exit: ")

    if ch == "1":
        e = input("Event: ")
        queue.append(e)

    elif ch == "2":
        if queue:
            print("Processed:", queue.pop(0))

    elif ch == "3":
        print(queue)

    elif ch == "4":
        e = input("Cancel event: ")
        if e in queue:
            queue.remove(e)

    else:
        break
