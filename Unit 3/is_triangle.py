def is_triangle(a, b, c):
  if a > b + c or b > a + c or c > a + b:
    print("No")
  else:
    print("Yes")

def get_user_input():
  a = int(input("a: "))
  b = int(input("b: "))
  c = int(input("c: "))
  return a, b, c

a, b, c = get_user_input()
is_triangle(a, b, c)
