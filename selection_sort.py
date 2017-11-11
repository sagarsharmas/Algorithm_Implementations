def selection_sort(p):
    for i in range(0,len(p)):
        min_index = i
        for j in range(i+1,len(p)):
            if p[min_index]>p[j]:
                min_index = j
        p[i], p[min_index] = p[min_index], p[i]

def main():
    p = [3,5,4,2,7,6,1,9,8,10]
    selection_sort(p)
    print p


if __name__ == "__main__":
    main()
