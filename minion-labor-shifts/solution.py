def solution(data, n):
    occurrences = dict()

    for _id in data:
        try:
            occurrences[_id] += 1
        except KeyError:
            occurrences[_id] = 1

    return [_id for _id in occurrences if occurrences[_id] <= n for _ in range(occurrences[_id])]
