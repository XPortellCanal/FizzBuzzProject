def fizz_buzz(max_num):
  multiple=3*5
  for num in range(1,max_num+1):
    if num%multiple==0:
      print("FizzBuzz")
    elif num%3==0:
      print("Fizz")
    elif num%5==0:
      print("Buzz")
    else:
      print(num)

fizz_buzz(100)
