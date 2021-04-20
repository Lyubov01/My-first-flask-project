from app import app


# we use the route() decorator to tell Flask what URL should trigger our function.
@app.route('/')
def index():
    return 'Hello world'
