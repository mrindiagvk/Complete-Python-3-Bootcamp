N=int(input("enter value"))
M=input()
M=M.split()
#covnvert_str_to_int
lists=[]
for i in M:
    i=int(i)
    lists+=[i]

#create dictionary to store the count
count_dict={}
maximum_count=0
for number in M:
    if number not in count_dict:
        count_dict[number]=1
    else:
        count_dict[number]+=1
    maximum_count=max(maximum_count,count_dict[number])
min_size=float('inf')
count=0
left=0
for right in range(N):
    if count_dict[M[right]]==maximum_count:
        count+=1
    
    while count==maximum_count:
        min_size=min(min_size,right-left+1)
        if count_dict[M[left]]==maximum_count:
            count-=1
        left+=1
print(min_size)
