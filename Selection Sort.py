def selectionsort(arr):
    n=len(arr)
    for i in range(n-1):
        mini=i

        for j in range(i+1,n):
            if arr[j]<arr[mini]:
                mini=j

        arr[i],arr[mini]= arr[mini],arr[i]        
    return arr


if __name__ =="__main__":
    arr= list(map(int,input("Enter elements: ").split()))
    sortedl= selectionsort(arr)
    for i in arr:print(i,end=" ")