def minsortedarray(arr):
    low,high=0,len(arr)-1

    while(low<high):
        mid= low+(high-low)//2
        if (arr[mid]>arr[high]):
            low=mid+1
        else:
            high=mid-1
    return arr[low]

if __name__== "__main__":
    arr= list(map(int,input("Enter elements: ").split()))
    res= minsortedarray(arr)
    print(f"Minimum element: {res}")
                

