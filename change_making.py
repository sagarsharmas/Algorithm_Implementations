import sys, datetime as dt

def change_making(denomination,amount):
    no_of_coins = float("inf")

    # If the amount itself is one of the denomination, it doesn't need further change
    if amount in denomination:
        return 1

    else:
        for i in denomination:
            if i <= amount:
                coins_count = 1 + change_making(denomination,amount-i)
                if coins_count < no_of_coins:
                    no_of_coins = coins_count
    return no_of_coins

def main():
    data = sys.argv[1:]  #The first argument holds the filename; starting from second is the input data
    amount = int(data[0])
    no_of_denominations = int(data[1]) #this variable is not used, however, used to match with the required input format
    denomination = map(int, data[2:])
    startTime = dt.datetime.now()
    no_of_coins = change_making(denomination,amount)
    endTime = dt.datetime.now()
    print str(no_of_coins) + ',' + str((endTime - startTime).microseconds)

if __name__ == "__main__":
    main()