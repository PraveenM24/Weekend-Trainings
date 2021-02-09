def removecolon_space(arr):
    remove = str.maketrans('', '', ':')
    final_arr = [s.translate(remove) for s in arr]
    while '' in final_arr:
        final_arr.remove('')
    while ' ' in final_arr:
        final_arr.remove(' ')
    return final_arr
    
def getUpper(arr):
    arr = removecolon_space(arr)
    upper = [''.join(arr[0:arr.index('M')+1])]
    return upper
    
def getLower(arr):
    arr = removecolon_space(arr)
    lower = [''.join(arr[arr.index('M')+1:])]
    return lower
    
def listToString(arr): 
    str1 = " "   
    return (str1.join(arr))
    
def convertto24hr(string):
    if 'A' in string:
        string = string[:-2]
        integer = int(string)
        if 1200 <= integer <= 1299:
            integer -= 1200
            return integer
        return integer
    else:
        string = string[:-2]
        integer = int(string)
        if 1200 <= integer <= 1299:
            return integer
        integer += 1200
        return integer

for _ in range(int(input())):
    time_avail = list(input())
    time_avail = removecolon_space(time_avail)
    time_avail = getUpper(time_avail)
    time_avail = listToString(time_avail)
    P = convertto24hr(time_avail)
    final = ''
    for _ in range(int(input())):
        listvalue = list(input())
        listvalue = removecolon_space(listvalue)
        upperlistvalue = getUpper(listvalue)
        lowerlistvalue = getLower(listvalue)
        upperlistvalue = listToString(upperlistvalue)
        lowerlistvalue = listToString(lowerlistvalue)
        upperlistvalue = convertto24hr(upperlistvalue)
        lowerlistvalue = convertto24hr(lowerlistvalue)
        L = min(upperlistvalue, lowerlistvalue)
        R = max(upperlistvalue, lowerlistvalue)
        if L <= P <= R:
            final += '1'
        else:
            final += '0'
    print(final)
    