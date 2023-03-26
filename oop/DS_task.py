
all = 24

t = [i for i in range(1,all + 1)]
# t_end = 
# dict_ = {}
res = []
# s = 1000000000

# print(list(enumerate(t,1)))
for ind , i in enumerate(t, 1):
    s1 = 4 * i **2
    s2 = (all - i)**2
    s = s1 + s2
    res.append((s, ind))
    # dict_[ind] = s

end_res = min(res)
min_s = end_res[0]
boat1 = end_res[1]
boat2 = all - boat1

print(min_s)
print(boat1)
print(boat2)



# for k,v in dict_.items():
#     for v 





    
# print(min(res))

# s1 = 4 * t **2
# boat1 = s1

# boat2 = 24 - t
# s2 = (24 - t)**2

# s = s1 + s2

# # print(t)
# # print()
# # print(boat1)
# # print(boat2)

# # print(s1)
# # print(s2)
# # print(s)


# if t
# print(t)


