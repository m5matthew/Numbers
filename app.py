from flask import Flask
app = Flask(__name__)


@app.route('/<int:number>/<arg>')
def numbers(number, arg):

    def is_prime(x):

        # negative numbers and {0,1} are not prime numbers
        if x < 2:
            return False

        for i in range(2, x):
            if x % i == 0:
                return False
        return True

    if arg == "odd":
        return ','.join([str(x) for x in range(1, number+1) if x % 2 == 1])

    elif arg == "even":
        return ','.join([str(x) for x in range(1, number+1) if x % 2 == 0])

    elif arg == "prime":
        return ','.join([str(x) for x in range(1, number+1) if is_prime(x)])

    return f"Argument {arg} is not supported. Please select from odd, even, or prime"
