from flask import Flask
from numberlib import is_odd, is_even, is_prime
app = Flask(__name__)


@app.route('/<int:number>')
@app.route('/<int:number>/<arg>')
def numbers(number, arg=None):

    out = list(range(1, number+1))

    if arg == "odd":
        out = filter(is_odd, out)

    elif arg == "even":
        out = filter(is_even, out)

    elif arg == "prime":
        out = filter(is_prime, out)

    # Return sequence of numbers joined with commas
    return ','.join([str(x) for x in out])
