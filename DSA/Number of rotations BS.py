def noofrotations(arr):
    low,high=0,len(arr)-1

    while(low<high):
        mid= low+(high-low)//2
        if (arr[mid]>arr[high]):
            low=mid+1
        else:
            high=mid
    return low

if __name__== "__main__":
    arr= list(map(int,input("Enter elements: ").split()))
    res= noofrotations(arr)
    print(f"Number of rotations: {res}")
                
