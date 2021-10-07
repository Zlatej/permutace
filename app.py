import math
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('app.html')


@app.route('/send', methods=['POST'])
def send(sum=sum):
    if request.method == 'POST':
        operace = request.form['operace']

        #form
        if operace == 'permutace':
            n = int(request.form['n'])

        elif operace == 'variace':
            n = int(request.form['n'])
            k = int(request.form['k'])

        elif operace == 'kombinace':
            n = int(request.form['n'])
            k = int(request.form['k'])

        elif operace == 'permutacesop':
            n = int(request.form['n'])

            r1 = int(request.form['r1'])
            r2 = int(request.form['r2'])
            r3 = int(request.form['r3'])
            r4 = int(request.form['r4'])
            r5 = int(request.form['r5'])

        elif operace == 'variacesop':
            n = int(request.form['n'])
            k = int(request.form['k'])

        elif operace == 'kombinacesop':
            n = int(request.form['n'])
            k = int(request.form['k'])

        #vypocty
        if operace == 'permutace':
            sum = float(math.factorial(n))
            return render_template('app.html', sum=sum)

        elif operace == 'variace':
            sum = float(math.factorial(n)/math.factorial(n-k))
            return render_template('app.html', sum=sum)

        elif operace == 'kombinace':
            sum = float(math.factorial(n)/math.factorial(n - k)/math.factorial(k))
            return render_template('app.html', sum=sum)

        elif operace == 'permutacesop':
            sum = float(math.factorial(n)/math.factorial(r1)/math.factorial(r2)/math.factorial(r3)/math.factorial(r4)/math.factorial(r5))
            return render_template('app.html', sum=sum)

        elif operace == 'variacesop':
            sum = float(n ** k)
            return render_template('app.html', sum=sum)

        elif operace == 'kombinacesop':
            sum = float(math.factorial(n + k - 1)/math.factorial(n - 1)/math.factorial(k))
            return render_template('app.html', sum=sum)


        else:
            return render_template('app.html')


if __name__ == ' __main__':
    app.debug = True
    app.run()