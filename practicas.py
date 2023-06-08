# Example 1

print((6*3 >= 18) and (9+9 <= 36/2))

# Example 2

print("Nairobi" < "Milan" and "Nairobi" > "Hanoi")

# True or True returns True
print((15/3 < 2+4) or (0 >= 6-7))


# False or True returns True
country = "New York City"
city = "New York City"
print(country == "New York City" or city == "New York City")


# True or False returns True
print(16 <= 4**2 or 9**(0.5) != 3)


# False or False returns False
print (" B_name" > "C_name" or "B_name" < "A_name")

# Test Example 1:

x = 2*3 > 6
print("EL valor de x es:")
print(x)

print("")  # Prints a blank line

print("El valor inverso de x es:")
print(not x)

def is_positive(number):
  if number > 0:
    return True
  else:
    return False

print(is_positive(5))
