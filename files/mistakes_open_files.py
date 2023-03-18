# with open('new_file.txt', 'w+') as f:
#     f.writelines('0*1*2*3*4*5*6*7*8*9*')
# print(f.read()) 

#Task 5
# with open('new_file.txt', 'r') as file:
#     print(file.read())
#     file.seek(0)
#     res = [int(i) for i in file.readlines()]
#     res.sort()
#     print(res)
# with open('test.txt', 'w+') as file:
#     file.write(f'{res[0]}-{res[-1]}')
#     file.read()


# with open('task6.txt', 'w+') as file2:
#     file2.write(f'{mn}-{mx}')
#     file2.seek(0)
#     print(file2.read())

#Task 6
# def read_last(lines, filename):
#     with open('article.txt', 'r') as f:
#         filename = f.readlines[-1]
#         lines = len((f.readlines))
#     return filename, lines
# print(read_last(lines, filename))

# def read_last(lines, filename): 
#     with open(filename) as file: 
#         list_ = file.readlines() 
#         if lines < len(list_): 
#             i = 0 
#             reversed_list_ = list_[::-1] 
#             while i<lines: 
#                 print(reversed_list_[i].replace('\n', '')) i+=1 else: list_.reverse() for i in list_: print(i.replace('\n', '')) read_last(9, 'article.txt')

# def read_last(lines, filename): 
#     with open(filename) as file: 
#         list_ = file.readlines() 
#         list_.reverse() 
#         if len(list_) > lines: 
#             i = 0 
#             while i < lines: 
#                 print(list_[i].replace('\n', '')) 
#                 i += 1 else: for i in l

#Task 7
def longest_words(filename):
    with open(filename, 'r') as file:
        res = [i.split() for i in file.readlines()]
        res2 = [inner for i in res for inner in i]
        res2.sort(key = len)
        result = [i for i in res2 if len(i) == len(res2[-1])]
        print(res)
        # if len(result) > 1:
        #     print(result)
        # else:
        #     print(result[0])
longest_words('article.txt')
