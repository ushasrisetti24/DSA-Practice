def firstoccurance(arr,key):
    low, high= 0, len(arr)-1
    ans=-1

    while low<=high:
        mid= low + (high-low)//2

        if(arr[mid]==key):
            ans= mid
            high=mid-1

        elif(arr[mid]<key):
            low=mid+1

        else:
            high=mid-1

    return ans

if __name__ == "__main__":
    arr= list(map(int,input("Enter elements: ").split()))
    key= int(input("Enter key: "))
    res= firstoccurance(arr,key)
    print(f"First occurance of {key} is at {res+1} position")