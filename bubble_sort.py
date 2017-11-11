def bubble_sort(p):
    for i in range(0,len(p)):
        for j in range(0,len(p)-i-1):
            if p[j]>p[j+1]:
                p[j],p[j+1] = p[j+1],p[j]



def main():
    p = [11,7,56,8,10]
    bubble_sort(p)
    print p


if __name__ == "__main__":
    main()
