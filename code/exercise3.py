def swap(d):
  keys = d.keys()
  values = d.values()
  swapped_tuples = zip(values, keys)
  value_types = [type(elem) for elem in values]
  
  if type({}) in value_types or type([]) in value_types:
    return 'Cannot swap the keys and values for this dictionary'
  else:
    new_dict = dict(swapped_tuples)
    return new_dict