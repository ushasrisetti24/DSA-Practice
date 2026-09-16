
def mergesort(arr):
    
    print(f"Initial at merge sort: {arr}")
    if(len(arr))<=1:
        return arr
    
    mid= len(arr)//2
    left= mergesort(arr[:mid])
    print(f"left: {left}")
    right= mergesort(arr[mid:])
    print(f"right: {right}")

    return merge(left,right)

def merge(l,r):
    i=j=0
    res=[]
    print(f"left initial: {l}")
    print(f"right initial: {r}")
    while i<len(l) and j<len(r):
        if(l[i]<=r[j]):
            res.append(l[i])
            print(f"{l[i]} < {r[j]}")
            print(f"appending left: {res}")
            i+=1
        else:
            res.append(r[j])
            print(f"{l[i]} > {r[j]}")
            print(f"appending right: {res}")
            print(res)
            j+=1    
    res.extend(l[i:])
    res.extend(r[j:])
    print(f"after rest elements added: {res}")
    return res


if __name__ == "__main__":
    arr= [23, 1, 56, 34, 98, 539, 55]
    print(mergesort(arr))