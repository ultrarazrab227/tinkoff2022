minim = 999999999
maxim = -99999999
for i in range(-100, 100):
    for j in range(-100, 100):
        for k in range(-100, 100):
            if i ** 2 + j ** 2 + 2 * k ** 2 == 22:
                vir = 2 * i + j - k + 1
                if vir < minim:
                    minim = vir
                if vir > maxim:
                    maxim = vir
print(minim, maxim)
