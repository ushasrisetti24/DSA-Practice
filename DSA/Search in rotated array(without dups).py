def searchinrotatearray(arr,x):
    low,high=0,len(arr)-1
    ans=-1

    while(low<=high):
        mid= low + (high-low)//2

        if(arr[mid]==x):
            return mid

        if(arr[mid]>=arr[low]):

            if(arr[low]<=x<arr[mid]):
                high=mid-1
            else:
                low=mid+1

        else:

            if(arr[mid]<x<=arr[high]):
                low=mid+1
            else:
                high=mid-1                
    return ans

if __name__ == "__main__":
    arr= list(map(int,input("Enter elements: ").split()))
    key= int(input("Enter key: "))
    res= searchinrotatearray(arr,key)
    print(f"Position of element is at {res+1} index")
