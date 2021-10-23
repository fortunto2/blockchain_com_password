
from pprint import pprint

names = [

    ['first', 'First'],
    ['Second', 'second'],
    ['Tree', 'tree', 'treeee'],
]

numbers = [2, 22, 444,55,666]

import itertools

# print(list(ite1rtools.product(*names)))
# print(list(itertools.combinations([names[0][0], names[1][0], names[2][0]], 3)))

def generate():

    final = []

    for line1 in names[0]:
        for line2 in names[1]:
            for line3 in names[2]:
                for line4 in numbers:

                    for i in range(1, 4):
                        # print(i, line1, line2, line3, line4)

                        mutant = list(itertools.permutations([line1, line2, line3], i))

                        final = final + mutant

                        for m in mutant:

                            final.append(m + tuple([str(line4)]))

    return list(set(final))


if __name__ == "__main__":

    final = generate()

    pprint(final)

    print(len(final))

    with open('passwords.txt', 'w') as f:
        for item in final:
            comb_str = ''.join(list(item))
            if len(comb_str)<8:
                # print('skip small', comb_str)
                continue
            f.write("%s\n" % comb_str)

