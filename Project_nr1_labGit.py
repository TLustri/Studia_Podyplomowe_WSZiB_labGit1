a = 14_000.  # zł
b = .4  # 40%
c = 1_500.  # zł strata
d = .12  # 12%

k0 = "kwota inwestycji:"
k = "Kwota inwestycji w pierwszym roku:"
k1 = "Kwota inwestycji w drugim roku:"
k2 = "Kwota inwestycji w trzecim roku:"
z = "zł"

print(k0, a, z, sep=" ")
print()
a = a + a * b
print(k, a, z, sep=" ")
print()
a = a - c
print(k1, a, z, sep=" ")
print()
a = a + a * d
print(k2, round(a, 2), z, sep=" ")
print()

# the end
