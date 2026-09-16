def insertionsort(arr):
    n=len(arr)
    for i in range(1,n):
        key=arr[i]
        j=i-1

        while j>=0 and key<arr[j]:
            arr[j+1]= arr[j]
            j-=1
        arr[j+1]=key
    return arr
if __name__ == "__main__":
    arr=list(map(int,input("Enter elements: ").split()))

    sorteda= insertionsort(arr)
    for i in arr:
        print(i,end=" ")
