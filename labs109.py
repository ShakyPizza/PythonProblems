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


# Started 14.02.2025 - BOP - solved 16.02.2025 - USOF
def only_odd_digits(n):
    if set(str(n)).issubset(set("13579")):
        return True
    else:
        return False


# Started 16.02.2025 - BOP - solved 16.02.2025 - SUAI
def is_cyclops(n):
    s = str(n)
    
    if len(s) % 2 == 0:
        return False
    
    mid_index = len(s) // 2
    
    if s[mid_index] != '0':
        return False
    
    for i, digit in enumerate(s):
        if i != mid_index and digit == '0':
            return False
    
    return True


# Started 16.02.2025 - BOP - 

def domino_cycle(tiles):

    print("Uphafleg  tiles:", tiles)
    print("Upphafleg lengd:", len(tiles))

    if len(tiles) == 1:
        print("lengd <= 1")
        fyrri, seinni = zip(*tiles)
        for item in fyrri:
            if fyrri == seinni:
                print("debug 2: True")
                return True
            else:
                print("debug 3: False")
                return False
    if len(tiles) == 0:
        print("Lengd == 0")
        return True
    if len(tiles) == 2:
        fyrri, seinni = zip(*tiles)
        if fyrri[1] == seinni[0] and fyrri[0] == seinni[1]:
            return True
        else:
            return False
    if len(tiles) > 2:
        fyrri, seinni = zip(*tiles)
        fyrsta_sett = tiles[0]
        seinna_sett = tiles[-1]
        for f in fyrri:
            for s in seinni:
                print("fyrri:", f, "Seinni:", s)
            #if fyrri[n] == seinni[n-1] and fyrsta_sett[0] == seinna_sett[-1]:
            #    return True
            #else:
            #    print("Debug 4: False")
            #    return False
        
    

test = [(5, 2), (2, 3), (3, 6), (6, 5), (5, 5)]

domino_cycle(test)