def lastoccurance(arr,key):
    low, high= 0, len(arr)-1
    ans=-1

    while low<=high:
        mid= low + (high-low)//2

        if(arr[mid]==key):
            ans= mid
            low=mid+1

        elif(arr[mid]>key):
            high=mid-1

        else:
            low=mid+1

    return ans

if __name__ == "__main__":
    arr= list(map(int,input("Enter elements: ").split()))
    key= int(input("Enter key: "))
    res= lastoccurance(arr,key)
    print(f"Last occurance of {key} is at {res+1} position")

        
