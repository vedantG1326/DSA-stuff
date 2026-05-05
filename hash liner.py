table = [None]*10

def hashf(key):
    return key % 10

def insert(key):
    i = hashf(key)
    while table[i] is not None:
        i = (i+1)%10
    table[i] = key

def search(key):
    i = hashf(key)
    while table[i] is not None:
        if table[i] == key:
            return True
        i = (i+1)%10
    return False

insert(15)
insert(25)
print(table)
print(search(25))
