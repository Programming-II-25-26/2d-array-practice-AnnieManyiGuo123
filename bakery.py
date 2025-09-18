def bakery():
    # Enter
    num_bread = int(input("Enter the number of bread types: "))
    num_days = int(input("Enter the number of days: "))
    
    # create a list 
    # # make sure input can add into the data 
    # # for: in num_bread range # append data(list) // data should be in a list
    sales = []
    for i in range(num_bread):
        # https://www.w3schools.com/python/ref_string_split.asp [split] 
        # https://www.geeksforgeeks.org/python/python-map-function/ [map]
        data = list(map(int, input(f"Enter sales for bread type {i+1}: ").split()))
        sales.append(data)

    # total sales for each bread type
    # create list; go through; add the sum in the list i created 
    bread_totals = []
    for row in sales:
        bread_totals.append(sum(row))


    # first try
    # reason wrong: calculating the rows and cols
    # solution: use another for to get each day's cols
    #day_avgs = []
    #for col in sales:
      #  avg = sum (col) / num_bread
      #  day_avgs.append(avg)

    day_avgs = []
    for col in range (num_days):
        # remember to initialize the total
        total = 0
        for row in range (num_bread):
            total += sales [row][col] # taking the cols
        avg = total / num_bread
        day_avgs.append (avg)


    print("Total sales for each bread:", bread_totals)
    print("Average daily sales:", day_avgs)

bakery()
