# def accounting(n):
#     size = 1
#     icost = 0
#     dcost = 0
#     total = 0
#     bank = 0
#     print("Elements\tDoubling Cost\t Insertion cost\t Total cost\t Bank")
#     for i in range(1, n+1):
#         icost = 1
#         if i>size:
#             size *= 2
#             dcost = i-1
#         total = icost + dcost
#         bank += 3-total
#         print(i,"\t\t\t",dcost,"\t\t",icost,"\t\t",total,"\t",bank)
#         icost = 0
#         dcost = 0

# n = int(input("enter number of elements"))
# print("accounting method")
# accounting(n)

pop = 0
def multipop(s,k):
    global pop
    for i in range(k):
        s.pop()
        pop += i 
    print('pop=', pop)
 
def cost(push,pop,arr):
    avg = (push+pop)/len(arr)
    print("amortized cost is: ",avg)
    print("asymptotic cost is: ",(push+pop))
    
def stack():
    s = []
    arr = [5,7,9,2,8,6,3]
    push = 0
    for i in range(len(arr)):
        if(arr[i]<len(s)):
            multipop(s,arr[i])
        s.append(arr[i])
        push += 1 
        print(s)
        print("push = ",push)
    cost(push,pop,arr)
    
stack()
        

