def check_fermat(a, b, c, n):
  if n > 2 and a^n + b^n == c^n:
    print("Holy smokes, Fermat was wrong!")
  else:
    print("No, that doesn't work")

def get_user_input():
  a = int(input("a: "))
  b = int(input("b: "))
  c = int(input("c: "))
  n = int(input("n: "))
  return a, b, c, n

a, b, c, n = get_user_input()
print(f"a: {a}, b: {b}, c: {c}, n: {n}")
check_fermat(a, b, c, n);
