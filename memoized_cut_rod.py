def memoized_cut_rod(p, n):
    r = [0] * n
    for i in range(0, n):
        r[i] = -float("inf")
    return memoized_cut_rod_aux(p, n, r)


def memoized_cut_rod_aux(p, n, r):
    if r[n-1] >= 0:
        return r[n-1]
    if n == 0:
        q = 0
    else:
        q = -float("inf")
        for i in range(0, n):
            q = max(q, p[i] + memoized_cut_rod_aux(p, n - 1- i, r))
    r[n-1] = q
    return q


def main():
    p = [1,7,5,8,10]
    print memoized_cut_rod(p,5)


if __name__ == "__main__":
    main()
