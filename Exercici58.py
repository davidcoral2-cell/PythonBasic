r = []
for num in range(1, 101):
    if num > 1 and all(num % i for i in range(2, int(num**0.5) + 1)):
        r.append(num)
print("Números primers entre 1 i 100: {}".format(r))
print("Total de números primers: {}".format(len(r)))
