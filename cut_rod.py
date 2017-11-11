# A straight forward recursive solution of cut-rod algorithm. This takes the running time complexity of order 2^n.
def cut_rod(p, n):
    if n==0:
        return 0
    q = -float("inf")
    for i in range (0,n):
        q = max(q,p[i]+cut_rod(p,n-i-1))
    return q

def main():
    p = [1,7,5,8,10]
    print cut_rod(p,5)


if __name__ == "__main__":
    main()
