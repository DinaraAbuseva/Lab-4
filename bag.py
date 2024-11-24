stuff = {
    'r': (3, 25), 
    'p': (2, 15), 
    'a': (2, 15), 
    'm': (2, 20), 
    'k': (1, 15), 
    'x': (3, 20), 
    't': (1, 25),
    'f': (1, 15), 
    'd': (1, 10), 
    's': (2, 20), 
    'c': (2, 20)
}


def get_table(stuff, max_value=9):
    items = list(stuff.items())
    V = [
        [([], start_hp) for _ in range(max_value + 1)] for _ in range(len(items) + 1)
        ]

    for i in range(1, len(items) + 1):
        for j in range(1, max_value + 1):
            item = items[i - 1]
            name, mass, hp = item[0], item[1][0], item[1][1]
            if mass > j:
                V[i][j] = V[i - 1][j]
            else:
                V[i][j] = max(
                    V[i - 1][j], 
                    (V[i - 1][j - mass][0] + [name], V[i - 1][j - mass][1] + hp * 2), 
                    key=lambda x: x[1]
                    )
    return V


start_hp = -sum(v for _, v in stuff.values()) + 15
table = get_table(stuff, 9) 
optimal_table = list(table[-1][-1])  
if 'd' not in optimal_table[0]:  
    rep = min(
        list(filter(lambda i: stuff[i][0] == 1, optimal_table[0])), 
        key=lambda i: stuff[i][1]
        )
    optimal_table[1] = optimal_table[1] - stuff[rep][1] * 2 + stuff['d'][1] * 2
    optimal_table[0].remove(rep)
    optimal_table[0].append('d')


bag=[]
for i in optimal_table[0]:
    bag.extend([i]*stuff[i][0])

print(
    ''.join(
        [f'[{bag[i]}],' if i % 3 != 2 else f'[{bag[i]}]\n' for i in range(len(bag))]
        )
    )
print('Итоговые очки выживания:', optimal_table[1])