# this is thr bubble sort alogorithm
def bubble_sort(n):
    l= len(n)
    for i in range(l-1,0,-1):
        
        for j in range(i):
            if n[j]>n[j+1]:
                n[j],n[j+1]=n[j+1],n[j]
                
nums = [6,3,8,1,3,9,4,7,3,6,2,6,6]
print("This is the Array Before Sorting...")
print(nums)
bubble_sort(nums)
print("This is the Array After Sorting...")
print(nums)
