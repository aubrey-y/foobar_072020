def solution(l):
    triples = 0
    multiples_of = [0 for _ in range(len(l))]
    for i in range(len(l) - 1, 0, -1):
        for k in range(i - 1, -1, -1):
            if l[i] % l[k] == 0:
                multiples_of[i] += 1
    for i in range(len(l) - 1, 0, -1):
        for k in range(i - 1, -1, -1):
            if l[i] % l[k] == 0:
                triples += multiples_of[k]
    return triples
