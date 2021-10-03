import math

while 1:
    print("Zvol si operaci\nPro operaci stiskni číslo:\n\nPermutace\t\t1\nVariace\t\t\t2\nKombinace\t\t3\nSvetry ve výloze\t4\nVariace s opakováním\t5\n") #Pro ukončení napiš: konec\n
    try:
            o = int(input("Číslo operace: "))
            try:
                if o == 1:                             
                    n = int(input("Zadej n: "))
                    print("\nVýsledek je: \t", math.factorial(n))
                elif o == 2:
                    n = int(input("Zadej n: "))
                    k = int(input("Zadej počet prvků: "))
                    j = n - k
                    print("\nVýsledek je: \t", math.factorial(n)/math.factorial(j))
                elif o == 3:
                    n = int(input("Zadej n: "))
                    k = int(input("Zadej počet prvků: "))
                    j = n - k
                    print("\nVýsledek je: \t", math.factorial(n)/math.factorial(j)/math.factorial(k))
                elif o == 4:
                    n = int(input("Zadej n: "))
                    rk = 1
                    rp = 1
                    print("Zadej r (pro vypočítání napiš 0): ")
                    while 1:
                        r = int(input("r"))
                        if r != 0:
                            rk = rk * math.factorial(r)
                            rp = rp + 1
                        else:
                            print("Výsledek je: ", math.factorial(n)/rk)
                            break
                elif o == 5:
                    n = int(input("Zadej n: "))
                    k = int(input("Zadej počet prvků: "))
                    print("\nVýsledek je: \t", n ** k)
                elif o == "konec":
                    print("konec")
                    break
                else:
                    print("Cyba ve zadání operace")
            except:
                print("Chyba v zadání n nebo k")
    except:
        print("Chyba v zadání operace")
    input("\nPro pokračování stiskni ENTER\n")