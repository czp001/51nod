from itertools import permutations
print '\n'.join(sorted(set([''.join(x) for x in permutations(raw_input())])))
