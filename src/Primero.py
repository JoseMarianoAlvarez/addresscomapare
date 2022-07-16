
#-------------------------------------------------------------

def dice_coefficient(a, b):

    if not len(a) or not len(b): return 0.0
    """ quick case for true duplicates """
    
    if a == b: return 1.0
    """ if a != b, and a or b are single chars, then they can't possibly match """
    
    if len(a) == 1 or len(b) == 1: return 0.0
    
    """ use python list comprehension, preferred over list.append() """
    a_bigram_list = [a[i:i+2] for i in range(len(a)-1)]
    b_bigram_list = [b[i:i+2] for i in range(len(b)-1)]
    
    a_bigram_list.sort()
    b_bigram_list.sort()
    
    # assignments to save function calls
    lena = len(a_bigram_list)
    lenb = len(b_bigram_list)
    # initialize match counters
    matches = i = j = 0
    while (i < lena and j < lenb):
        if a_bigram_list[i] == b_bigram_list[j]:
            matches += 2
            i += 1
            j += 1
        elif a_bigram_list[i] < b_bigram_list[j]:
            i += 1
        else:
            j += 1
    
    score = float(matches)/float(lena + lenb)
    return score

print("Coeficiente de Sørensen–Dice:")
print(dice_coefficient("hotel hilton bs as", "hilton hotel"))
print(dice_coefficient("40 dalton st",	"40 cortes st"))
print(dice_coefficient("street del pontiere 26", "st del pontiere 26"))


#-------------------------------------------------------------

def jaccard_coefficient(a, b):

    if not len(a) or not len(b): return 0.0
    """ quick case for true duplicates """
    
    if a == b: return 1.0
    """ if a != b, and a or b are single chars, then they can't possibly match """
    
    if len(a) == 1 or len(b) == 1: return 0.0
    
    """ use python list comprehension, preferred over list.append() """
    a_bigram_list = [a[i:i+2] for i in range(len(a)-1)]
    b_bigram_list = [b[i:i+2] for i in range(len(b)-1)]
    
    a_bigram_list.sort()
    b_bigram_list.sort()
    
    # assignments to save function calls
    lena = len(a_bigram_list)
    lenb = len(b_bigram_list)
    # initialize match counters
    matches = i = j = 0
    while (i < lena and j < lenb):
        if a_bigram_list[i] == b_bigram_list[j]:
            matches += 1
            i += 1
            j += 1
        elif a_bigram_list[i] < b_bigram_list[j]:
            i += 1
        else:
            j += 1
    
    score = float(matches)/float(lena + lenb - matches)
    print(a_bigram_list)
    print(b_bigram_list)
    return score

print("Coeficiente de Jaccard:")
print(jaccard_coefficient("sheraton bs as", "bs as sheraton hotel"))
print(jaccard_coefficient("40 dalton st",	"40 cortes st"))
print(jaccard_coefficient("street del pontiere 26", "st del pontiere 26"))

#---------------------------------------------------------------------