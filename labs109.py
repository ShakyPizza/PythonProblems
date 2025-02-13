def ryerson_letter_grade(n):
    if n < 50:
        return 'F'
    elif n > 89:
        return 'A+'
    elif n > 84:
        return 'A'
    elif n > 79:
        return 'A-'
    tens = n // 10
    ones = n % 10
    if ones < 3:
        adjust = "-"
    elif ones > 6:
        adjust = "+"
    else:
        adjust = ""
    return "DCB"[tens - 5] + adjust


# Started 11.02.2025 - BOP - SUAI
def is_ascending(items):

    if len(items) < 2:
        return True
    
    for i in range(len(items) - 1):
        if items[i] >= items[i + 1]:
            return False

    return True
    

# Started 11.02.2025 - BOP - solved 13.02.2025 - NUAI
def riffle(items, out=True):

    result = []

    if len(items) >= 4:
        h = len(items) // 2
        if out:
            split_list1 = items[:h]
            split_list2 = items[h:]

        else:
            split_list2 = items[:h]
            split_list1 = items[h:]
            
        for n in range(len(items)//2):
            result.append(split_list1[n])
            result.append(split_list2[n])
        return result
           
    elif len(items) == 2:
        if out:
            return items
        else:
            result.append(items[1])
            result.append(items[0])
            return result

    elif len(items) == 3:
        if out:
            result.append(items[0], items[2], items[1])
            return result
        else:
            result.append(items[1], items[0], items[2])
            return result

    elif (len(items)) == 0:
        return items
    
    else:
        return items
    
def only_odd_digits(n):
    strengur = str(n)
    print("1.", strengur)
    for i in strengur:
        lowest = strengur[:1]
        print("2. Lowest:", lowest)
        if lowest /2 == 0:
            print("3.", False)
            return False
        if lowest /2 != 0:
            print("3.", True)
            return True
        else:
            return Exception
        
    lowest = n%10
    print(lowest)
    #for i in n:



test = 4223
only_odd_digits(test)