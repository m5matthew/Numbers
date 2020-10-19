# Numbers

Flask app to display even, odd and prime numbers

# Running the App

I have written a dockerfile to run the app in development mode.

```bash
docker build -t numbers:latest .
docker run -p 5000:5000 numbers
```

# Alternative approach

Another approach would be to define a function for each method
```python
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
```

**Pros**

- Easier to see which endpoints are defined
- Easier to unit test

**Cons**
- Repetitive
- Code is cluttered
