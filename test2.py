names = ["Roger", "Maximilian", "Norismel", "Maria", "Juan", "Ricardo", "Nancy", "Moises"]

def manipulate_names():
    for name in names:
        name_length = len(name)
        print(name_length)

        if (name_length > 5) and ("n" in name or "N" in name):
            print(name)

manipulate_names()

while len(names) > 0:
    names.pop()
    print(names)