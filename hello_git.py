import json


print("Hello Git world!")
# update

results = [
]

def funct(list = ['a', 'b', 'c'], list2 = ['x', 'y', 'z']):
    score = 0
    for n in list:
        print(f"\nThis is letter {n}. ")

    for m in list2:
        for n in list:
            text = f"{m} and {n};"

            results.append(text)
            if text == 'x and a':

                filename = 'special.json'
                with open(filename, 'w') as f1:
                    score += 1
                    json.dump(score, f1)

    return results



funct()
funct(list=['d','e','f'], list2=['q','p','r'])

filename = 'readme.json'
with open(filename, 'a') as f:
    var = funct()
    json.dump(var, f)

print(len(results))




