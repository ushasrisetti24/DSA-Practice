def floor(arr,x):
    low,high= 0, len(arr)-1
    ans=len(arr)
    while low<=high:
        mid=(low + high)//2
        if (arr[mid]<=x):
            ans=mid
            low=mid+1
        else:
            high=mid-1
    return arr[ans]        

def ceil(arr,x):
    low,high=0,len(arr)-1
    ans=len(arr)

    while(low<=high):
        mid= (low + high )//2
        while arr[mid]>=x:
            ans=mid
            high=mid=1

        else:
            low=mid+1  
    return arr[ans]         

if __name__=="__main__":
    arr= list(map(int, input("Enter sorted elements: ").split()))
    key=int(input("Enter key: "))             
    floorval= floor(arr,key)
    ceilval= ceil(arr,key)
    print(f"Floor value of sorted array: {floorval}")
    print(f"Ceil value of sorted array: {ceilval}")


