queue = []

def addCall(id, time):
    queue.append((id, time))

def answerCall():
    if queue:
        print("Answered:", queue.pop(0))

def viewQueue():
    print(queue)

def isEmpty():
    print("Empty" if not queue else "Not Empty")

addCall(101, 5)
addCall(102, 3)
viewQueue()
answerCall()
isEmpty()
