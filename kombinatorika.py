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
                    print("\nVýsledek je: \t", math.factorial(n)/math.factorial(n-k))
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
                elif o == 6:
                    n = int(input("Zadej n: "))
                    k = int(input("Zadej počet prvků: "))
                    print("\nVýsledek je: \t", math.factorial(n + k - 1)/math.factorial(n - 1)/math.factorial(k))
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



import math

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('app.html')

@app.route('/send', methods=['POST'])

def send(sum=sum):
    if request.method == 'POST':
        n = request.form['n']
        k = request.form['k']
        r1 = request.form['r1']
        r2 = request.form['r2']
        r3 = request.form['r3']
        r4 = request.form['r4']
        r5 = request.form['r5']
        operation = request.form['operation']
        
        #calculating if statements
        r1 = 1
        r2 = 1
        r3 = 1
        r4 = 1
        r5 = 1
        
        if operation == 'permutace':
            sum =float(math.factorial(n))
            return render_template('app.html', sum=sum)

        elif operation == 'variace':
            sum = int(math.factorial(n)/math.factorial(n-k))
            return render_template('app.html', sum=sum)

        elif operation == 'kombinace':
            sum = int(math.factorial(n)/math.factorial(n - k)/math.factorial(k))
            return render_template('app.html', sum=sum)

        elif operation == 'permutacesop':
            sum = int(math.factorial(n)/math.factorial(r1)/math.factorial(r2)/math.factorial(r3)/math.factorial(r4)/math.factorial(r5))
            return render_template('app.html', sum=sum)

        elif operation == 'variacesop':
            sum = int(n ** k)
            return render_template('app.html', sum=sum)

        elif operation == 'kombinacesop':
            sum = int(math.factorial(n + k - 1)/math.factorial(n - 1)/math.factorial(k))
            return render_template('app.html', sum=sum)

        else:
            sum = "Chyba"
            return render_template('app.html')

if __name__ == ' __main__':
    app.debug = True
    app.run()