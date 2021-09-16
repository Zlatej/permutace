import math

while 1:
    print("Zvol si operaci\nPro operaci stiskni číslo\n\nPermutace\t1\nVariace\t\t2\nKombinace\t3\n(Pro ukončení napiš: konec)\n")
    try:
            o = int(input("Číslo operace: "))
            try:
                if o == 1:                             
                    n = int(input("Zadej n: "))
                    print(math.factorial(n))
                elif o == 2:
                    n = int(input("Zadej n: "))
                    k = int(input("Zadej počet prvků: "))
                    j = n - k
                    print(math.factorial(n)/math.factorial(j))
                elif o == 3:
                    n = int(input("Zadej n: "))
                    k = int(input("Zadej počet prvků: "))
                    j = n - k
                    print("\nKombinace ",k," tic z ",n," prvků je: \t", math.factorial(n)/math.factorial(j)/math.factorial(k))
                elif o == "konec":
                    print("konec")
                else:
                    print("Cyba ve zadání operace")
            except:
                print("Chyba v zadání n nebo k")
                input()
    except:
        print("Chyba v zadání operace")
    input("\nPro pokračování stiskni ENTER\n")