undo = []
redo = []
doc = ""

while True:
    ch = input("1.Add 2.Undo 3.Redo 4.Show 5.Exit: ")

    if ch == "1":
        text = input("Enter text: ")
        undo.append(doc)
        doc += text
        redo.clear()

    elif ch == "2":
        if undo:
            redo.append(doc)
            doc = undo.pop()

    elif ch == "3":
        if redo:
            undo.append(doc)
            doc = redo.pop()

    elif ch == "4":
        print("Doc:", doc)

    else:
        break
