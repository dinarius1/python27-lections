arr = []
with open("27-B_demo.txt") as file:
    for f in file.readlines():
        arr.append(f.strip().split())
arr = list(map(lambda i: [int(i[0]), int(i[1])], arr[1:]))
# arr[:10]

res = []
for i in arr[:]:
    res.append(max(i))
    # if i[0] > i[1]:
    #     res.append(i[0])
    # else:
    #     res.append(i[1])

summary = sum(res)
if summary % 3 != 0:
    print(summary)
else:
    while summary  % 3 != 0 and summary == max(summary):
        for i in arr[:]:
            




# print(list(enumerate(arr[:10])))
# all_list =
# for ind, el in enumerate(arr[:10]):
#     if 
    
# list_1 = [i[0] for i in arr[:10]]
# list_2 = [i[1] for i in arr[:10]]
# print(list_2)


    
