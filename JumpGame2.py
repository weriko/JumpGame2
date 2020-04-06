#well.... it works

def revIndex(arr, x):
    return len(arr) - arr[::-1].index(x) -1

def relMax(arr):
    maxi = 0
    temp = 0
    for i ,num in enumerate(arr):
        if i +num>maxi:
            maxi = i+num
            temp = i
    return maxi-temp
        
def jumpGame(arr):
    indx = 0
    for i in range(len(arr)):
        maximum = relMax(arr[indx+1:indx+arr[indx]+1])
        indx = revIndex(arr[:indx+arr[indx]+1], maximum)
        if indx>= len(arr)-1:
            return i+1
        
print(jumpGame([2,3,1,1,4,1,1]))
print(jumpGame([2,3,1,1,4,1,1,1,5]))
print(jumpGame([7,5,4,7,3,2,1,1,1,1,1,1,1,5,3,6,7,5,2,3,1,1,5,6,4,1,5,6,7,9]))
