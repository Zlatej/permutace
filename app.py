import math

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('app.html')

@app.route('/send', methods=['POST'])

def send(sum=sum):
    if request.method == 'POST':
        #pulling data
        n = request.form['n']
        k = request.form['l']
        operation = request.form['operation']
        
        #calculating if statements
        if operation == 'permutace':
            sum =n
            return render_template('app.html', sum=sum)

        elif operation == 'variace':
            sum =n
            return render_template('app.html', sum=sum)

        elif operation == 'kombinace':
            sum =n
            return render_template('app.html', sum=sum)

        elif operation == 'permutacesop':
            sum =n
            return render_template('app.html', sum=sum)

        elif operation == 'variacesop':
            sum =n
            return render_template('app.html', sum=sum)

        elif operation == 'kombinacesop':
            sum = n
            return render_template('app.html', sum=sum)

        else:
            sum = "Chyba"
            return render_template('app.html')
