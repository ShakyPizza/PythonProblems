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
    

# Started 11.02.2025 - BOP
def riffle(items, out=True):

    print(len(items))
    result = []

    if len(items) >= 4:
        h = len(items) // 2
        if out == True:
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
        if out == True:
            return items
        else:
            result.append(items[1])
            result.append(items[0])
            return result

    elif len(items) == 3:
        if out == True:
            result.append(items[0])
            result.append(items[2])
            result.append(items[1])
            return result
        else:
            result.append(items[1])
            result.append(items[0])
            result.append(items[2])
            return result

    elif (len(items)) == 0:
        return items
    
    else:
        return items
    
#print(len(items))
#print(result)
#
#test = [-4,0,1,-1]
#riffle(test, True)