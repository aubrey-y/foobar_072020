import re


def subtract_in_base(x, y, b):
    answer = [None for _ in range(len(x))]

    for i in range(len(x) - 1, -1, -1):
        carry = 0
        if x[i] < y[i]:
            carry += b
            for k in range(i - 1, -1, -1):
                if x[k] != "0":
                    x = x[:k] + str(int(x[k]) - 1) + x[k + 1:]
                    break
                else:
                    x = x[:k] + str(int(x[k]) + b - 1) + x[k + 1:]
        answer[i] = str(int(x[i]) + carry - int(y[i]))

    return "".join(answer)


def helper(n, b, existing):
    n_sorted = sorted(list(n))
    x = "".join(n_sorted[::-1])
    y = "".join(n_sorted)

    z = subtract_in_base(x, y, b)

    existing += z + ","

    match = re.search(r"(.+?,)\1+", existing)

    if match:
        span = match.span()
        if existing[span[0] - 1] == ",":
            return match.group(1).count(",")

    return helper(z, b, existing)


def solution(n, b):
    return helper(n, b, "")
