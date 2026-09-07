#input must be sorted

def BinarySearch(arr,x):
    low=0
    high= len(arr)-1
    mid= low + (high-low)//2

    while(high!=low):
        mid= low + (high-low)//2
        if(arr[mid]==x):
            return mid
        elif(arr[mid]>x):
            high=mid-1
        elif(arr[mid]<x):
            low= mid+1
        else:
            return -1

if __name__=="__main__":
    n=int(input())
        
    arr= list(map(int,input("Enter sorted elements: ").split()))
    print("enter key: ")
    k= int(input())
    res= BinarySearch(arr,k)
    print(f"Element is found at {res+1} index")

