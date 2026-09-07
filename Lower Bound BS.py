def lowerbound(arr,x):
    low=0
    high= len(arr)-1
    ans=len(arr)

    while low<=high:
        mid= (low+high)//2
        if (arr[mid]>=x):
            ans= mid
            high=mid-1

        else:
            low=mid+1
    return ans
if __name__=="__main__":
    arr= list(map(int, input("Enter sorted elements: ").split()))
    key=int(input("Enter key: "))             
    ind= lowerbound(arr,key)
    print(f"lower bound of {key} is at {ind+1} position")