a = 'hello'

# 5) Дан список из имён. Найдите самое длинное имя из списка функцией reduce.
# """
def len_(x,y):
  res = sorted(list1, key = len)
  return res[-1]
print(list(reduce(len_(), ['kate', 'nil', 'a'])))