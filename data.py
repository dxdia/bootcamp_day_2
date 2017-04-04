def data_type(a):
    if type(a) == int:
        if a < 100:
            return 'less than 100'
        elif a > 100:
            return 'more than 100'
        else:
            return 'equal to 100'

    elif type(a) == str:
      
      
      return len(a)

    elif type(a) == list:
        if len(a) < 3:
          
          return None
        else:
          
          return a[2]

    elif type(a) == bool:
      
      return a

    else:
      
      return 'no value'
