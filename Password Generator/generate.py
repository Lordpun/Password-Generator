import random
character_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','!','@','#','$','%','^','&','*','(',')','1','2','3','4','5','6','7','8','9','0']
lowercase_list, uppercase_list, symbols, numbers = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'], ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'], ['!','@','#','$','%','^','&','*','(',')'], ['1','2','3','4','5','6','7','8','9','0']
def generate(size, website, name):
  global character_list, lowercase_list, uppercase_list, symbols, numbers
  password = ''
  lowercheck, uppercheck, numbercheck, specialcheck = False, False, False, False
  try:
    size = int(size)
    if size >= 4:
      for number in range(size):
        password += random.choice(character_list)
      while lowercheck and uppercheck and numbercheck and specialcheck != True:
        password = ''
        lowercheck, uppercheck, numbercheck, specialcheck = False, False, False, False
        for char in password:
          if char in lowercase_list:
            lowercheck = True
          elif char in uppercase_list:
            uppercheck = True
          elif char in symbols:
            specialcheck = True
          elif char in numbers:
            numbercheck = True
      return password
    elif size < 4 and size > 0:
      return 'ERROR: Size too small.'
    elif size == 0:
      return 'ERROR: Password must exist.'
    elif size < 0:
      return 'ERROR: You can not have a password of negative length.'
    if website == '' or ' ':
      return 'ERROR: Please enter a website.'
    if name == '' or ' ':
      return 'ERROR: Please enter a username.'
  except:
    return 'ERROR: Enter a number for the size please.'