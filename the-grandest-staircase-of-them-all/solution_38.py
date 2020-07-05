from functools import lru_cache


@lru_cache(maxsize=None)
def get_permutations_of_steps(lower, higher):
    total = 0
    for new_lower in range(lower + 1, higher + 1):
        new_higher = higher - new_lower
        if new_lower < new_higher:
            total += get_permutations_of_steps(new_lower, new_higher) + 1
    return total


def solution(n):
    initial_splits = [(x, n - x) for x in range(1, n // 2 + 1)]
    return sum(get_permutations_of_steps(*split) + 1 for split in initial_splits)
