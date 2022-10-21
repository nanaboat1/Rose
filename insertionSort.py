## nana boateng amoah
## cs 473-1
## 10/3/2022


f = open('rosalind_ins.txt') 

data = f.readlines()[1].strip().split() 

data = [ int(i) for i in data]


#data = [6,10,4,5,1,2]

def insertionSort(arr : list) -> int: 

    min_swaps = 0

    N = len(arr)

    for i in range(1, N): 

        k = i 
        while k >=1 and arr[k] < arr[k-1]: 

            temp = arr[k-1]
            arr[k-1],arr[k] = arr[k], temp
            min_swaps += 1 

            k -= 1

    return min_swaps 

print(insertionSort(data)) 