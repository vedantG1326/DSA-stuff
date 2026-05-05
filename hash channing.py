table = [[] for _ in range(10)]

def hashf(key):
    return key % 10

def insert(key):
    i = hashf(key)
    table[i].append(key)

def search(key):
    i = hashf(key)
    return key in table[i]

def delete(key):
    i = hashf(key)
    if key in table[i]:
        table[i].remove(key)

insert(15)
insert(25)
print(search(15))
delete(15)
print(table)
