from flask import Flask
from lib import numberlib
app = Flask(__name__)


@app.route('/<int:number>')
@app.route('/<int:number>/<arg>')
def print_numbers(number, arg=None):
    out = list(range(1, number+1))

    if arg == "odd":
        out = filter(numberlib.is_odd, out)

    elif arg == "even":
        out = filter(numberlib.is_even, out)

    elif arg == "prime":
        out = filter(numberlib.is_prime, out)

    # Return sequence of numbers joined with commas
    return ','.join([str(x) for x in out])


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
