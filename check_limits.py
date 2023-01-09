from comparison import check_greater, check_lesser

def check_lower_breach(value, limit):
  return check_lesser(value, limit)

def check_higher_breach(value, limit):
  if check_greater(value, limit):
    return 'TOO_HIGH'
  return 'NORMAL'

def infer_breach(value, lowerLimit, upperLimit):
  if check_lower_breach(value, lowerLimit):
    return 'TOO_LOW'
  return check_higher_breach(value, upperLimit)
  
