# As an example, here is an implementation of
# the first problem "Ryerson Letter Grade":

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

def is_ascending(items):
    for i in range(len(items)-1):
        if items[i] >= items[i+1]: return False
    return True

def riffle(items, out=True):
    halve1 = []
    halve2 = []
    for i in range(len(items)//2):
        halve1.append(items[i])
    for i in range(len(items)//2, len(items)):
        halve2.append(items[i])
    shuffled_items = []
    j = 0
    k = 0
    for i in range(len(items)):
        if (((i % 2 == 0) & (out == True)) | ((i % 2 == 1) & (out == False))):
                shuffled_items.append(halve1[j])
                j = j + 1
        else:
                shuffled_items.append(halve2[k])
                k = k + 1
    return shuffled_items
    
def only_odd_digits(n):
    num = n
    while(num > 10):
        if((num % 10) % 2 == 0):
            return False
        else:
            num = num//10
    return num % 2 == 1

def is_cyclops(n):
    if(n == 0):
        return True
    num = n
    num_lenght = 0
    while(num > 0):
        num = num//10
        num_lenght = num_lenght + 1
    if(num_lenght % 2 == 0):
        return False
    num = n
    for i in range(num_lenght):
        if(i == num_lenght//2):
            if(num % 10 != 0):
                return False
            else:
                num = num//10
        else:
            if(num % 10 == 0):
                return False
            num = num//10
    return True

def domino_cycle(tiles):
    for i in range(len(tiles) - 1):
        if(tiles[i][1] != tiles[i+1][0]):
            return False
    if(tiles[0][0] != tiles[len(tiles)-1][1]):
        return False
    return True

def colour_trio(colours):
    processed_list = colours
    while(len(processed_list) > 1):
        temp_list = []
        for i in range(len(processed_list) - 1):
            if(processed_list[i] == processed_list[i+1]):
                temp_list.append(processed_list[i])
            elif((processed_list[i] != "b") & (processed_list[i+1] != "b")):
                temp_list.append("b")
            elif((processed_list[i] != "y") & (processed_list[i+1] != "y")):
                temp_list.append("y")
            else:
                temp_list.append("r")
        processed_list = temp_list
    return processed_list[0]

def count_dominators(items):
    if(len(items) == 0):
        return 0
    dominators = 1
    max = items[len(items)-1]
    for i in range(len(items)-1, 0, -1):
        if(items[i-1] > max):
            dominators = dominators + 1
            max = items[i-1]
    return dominators