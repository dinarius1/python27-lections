students = [
  {'student': 'Jack', 'marks': 43},
  {'student': 'Tom', 'marks': 92}, 
  {'student': 'Helen', 'marks': 85}, 
  {'student': 'Peter', 'marks': 58},
  {'student': 'Jessica', 'marks': 78}
]
def func19(students):
  res = []
  for i in students:
    res.append(i['marks'])
  res.sort(reverse = True)
  dict_ = []
  for number in res:
      for i in students:
          if i['marks'] == number:
              dict_.append(i)
  return dict_
print(func19(students))