romen_numbers = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
input = input("Enter Romen Number: ")
sonuc = 0
büyüklük = 5000
for num in input:
    if romen_numbers[num] <= büyüklük:
        büyüklük = romen_numbers[num]
        sonuc += romen_numbers[num]
    else:
        sonuc += romen_numbers[num] - büyüklük
        sonuc -= büyüklük
print(sonuc)
