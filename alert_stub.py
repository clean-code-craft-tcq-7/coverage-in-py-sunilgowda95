def send_to_controller_stub(breachType):
  header = 0xfeed
  print(f'{header}, {breachType}')
  return 2

def send_to_email_stub(breachType):
  recepient = "a.b@c.com"
  if breachType == 'TOO_LOW':
    print(f'To: {recepient}')
    print('Hi, the temperature is too low')
  elif breachType == 'TOO_HIGH':
    print(f'To: {recepient}')
    print('Hi, the temperature is too high')
  return 1
    
def send_breach_to_target_stub(alertTarget, breachType):
  ret = 0
  if alertTarget == 'TO_CONTROLLER':
    ret = send_to_controller_stub(breachType)
  elif alertTarget == 'TO_EMAIL':
    ret = send_to_email_stub(breachType)
  return ret