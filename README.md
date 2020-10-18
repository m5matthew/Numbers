# Numbers

Flask app to display even, odd and prime numbers

# Alternative approach

Another approach would be to define a function for each method
'''Python3
@app.route('/<int:number>')
def print_numbers(number):
...

@app.route('/<int:number>/even')
def print_evens(number):
...

@app.route('/<int:number>/odd>')
def print_odd(number):
...

@app.route('/<int:number>/prime')
def print_primes(number):
...
'''

**Pros**

- Easier to see which endpoints are defined
- Easier to unit test
  **Cons**
- Repetitive
- Code is cluttered
