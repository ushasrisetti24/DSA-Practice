""" Given an array of N integers. 
Every number in the array except one appears twice. 
Find the single number in the array.

Sol: As each Number appears twice- the integer starts at even index 
      and ends at odd index. When an element is inserted this pattern
      gets disturbed- now the element starts at odd and ends at even.
"""

def singleelement(arr):
    n=len(arr)
    low,high=0,n-2

    if(arr[0]!=arr[1]):
        return -1
    if(arr[n-1]!= arr[n-2]):
        return -1

    while low<=high:
        mid=low+(high-low)//2

        if(arr[mid]!=arr[mid-1] and arr[mid]!= arr[mid+1]):
            return mid, arr[mid]

        if(mid%2==1 and arr[mid]==arr[mid-1] or \
           mid%2==0 and arr[mid]==arr[mid+1]):
            low=mid+1

        else:
            high=mid-1
    return -1

if __name__ =="__main__":
    arr=list(map(int, input("Enter elements: ").split()))  
    ind,val= singleelement(arr)
    print(f"The single Element in an array is {val} at {ind+1} position")          
            