import json

def compare(f1, f2):
  with open(f1) as file1, open(f2) as file2:
    data1 = json.load(file1)
    data2 = json.load(file2)
    if data1 == data2:
      return 'The dictionaries are equal'
    else:
      count1 = len(data1)
      count2 = len(data2)
      if count1 > count2:
        return 'Dictionary 1 is longer than dictionary 2'
      elif count2 > count1:
        return 'Dictionary 2 is longer than dictionary 1'
      else:
        return 'Dictionary 1 and dictionary 2 have the same length'