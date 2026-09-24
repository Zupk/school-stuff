"""""
x = 5
y = 15
z = -10

print(x-z)
print(x*z)
print(x/z)

# deljenje z ostankom
print(10 % 3)
print(11 % 3)

# celostecilsko deljenje
print(10//3)

#potenca
print(123**6)

# decimalna ali float stevila
i = 3.14
j = 10.012

print(0.5+0.5 == 1)
print(0.1+0.2 == 0.3)
"""
# string - niz znakov
ime = "Luka"
print(ime)
print(len(ime))

st = "22"
print(st * 10)
print(int(st)*10)

naslov = "kidriceva 55"
print(naslov.upper())
print(naslov.lower())
naslov = naslov.strip()
print(len(naslov))

ime2 = "Til novak" # T.N.
imeU = ime2.upper() # TIL NOVAK
imespl = imeU.split()
print(imespl)
imeU = imespl[0] # TIL
pri = imespl[1] # NOVAK

print(imeU[0], pri[0])

# Version 2
"""
imeU = imespl[0][0] # TIL izpise T
pri = imespl[1][0] # NOVAK izpise N

print(imeU, pri)
"""
