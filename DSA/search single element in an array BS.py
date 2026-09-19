def firstoccurance(arr,k):
    low,high=0,len(arr)-1
    ans=0

    while low<=high:
        mid=low+ (high-low)//2

        if (arr[mid]==k):
            ans=mid
            high=mid-1

        elif(arr[mid]<k):
            low=mid+1
        else:
            high=mid-1    
    return ans

def lastoccurance(arr,k):
    low,high=0,len(arr)-1
    ans=0
    
    while low<=high:
        mid=low+(high-low)//2
    
        if (arr[mid]==k):
            ans=mid
            low=mid+1
    
        elif(arr[mid]>k):
            high=mid-1
        else:
            low=mid+1    
    return ans

def Singleelement(arr):
    for i in arr:
        count=lastoccurance(arr,i)- firstoccurance(arr,i)+1
        if count==1:
            return i


    

if __name__ == "__main__":
    arr=list(map(int,input("Enter elements: ").split()))
    res= Singleelement(arr)
    print(f"Single element is: {res}")