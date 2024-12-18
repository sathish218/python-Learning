def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        swap = False
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                swap = True
        if not swap:
            break
        
        
    return (arr)
            
arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = bubble_sort(arr)
print(sorted_arr)


def bubble_sort_string(string):
    n = len(string)
    for i in range(n-1):
        swap = False
        for j in range(n-i-1):
            if string[j] > string[j+1]:
                string[j],string[j+1] = string[j+1],string[j]
                swap = True
                
        if not swap:
            break
                
    return (string)
    
arr = ["Mohamed","Brindha","Sathish"]
print(bubble_sort_string(arr))

def bubble_sort_object(stringObj):
    n = len(stringObj)
    for i in range(n-1):
        swap = False
        for j in range(n-i-1):
            if stringObj[j]['name'] > stringObj[j+1]['name']:
             stringObj[j],stringObj[j+1] = stringObj[j+1],stringObj[j]
             swap =True
             
        if not swap:
            break
        
        return(stringObj)
 
stringObj = [{'name': 'Mohamed'}, {'name': 'Brindha'}, {'name': 'Sathish'}]
print(bubble_sort_object(stringObj))

    
txt = ",,,,,rrttgg.....banana....rrr"

x = txt.strip(",.grt")

print(x)
