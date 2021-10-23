
import itertools
from pprint import pprint

numbers = [2, 22, 333]


def generate():

    final = []

    mutant_numbers = list(itertools.permutations(numbers, 2))

    for line1 in ['Tree', 'tree']:

        print('1--------------')
        for line2 in numbers:
            final.append(line1 + str(line2))

        print('2--------------')
        for line3, line4 in mutant_numbers:
            final.append(line1 + str(line3) + str(line4))

    print(len(final))
    # print(final)

    return list(set(final))


if __name__ == "__main__":

    final = generate()

    # pprint(final)

    print(len(final))

    with open('passwords.txt', 'w') as f:
        for item in final:
            comb_str = ''.join(list(item))
            if len(comb_str)<8:
                # print('skip small', comb_str)
                continue
            f.write("%s\n" % comb_str)

