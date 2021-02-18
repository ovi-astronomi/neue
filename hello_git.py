print("Hello Git world!")
# update


def f(list = ['a', 'b', 'c'], list2 = ['x', 'y', 'z']):

    for n in list:
        print(f"\nThis is letter {n}. ")

    for m in list2:
        for n in list:
            print(f"{m} and {n};")

f()
f(list=['d','e','f'], list2=['q','p','r'])
