import time
import redis
from flask import Flask

app = Flask(__name__)
# Connect to the Redis service container by its hostname
cache = redis.Redis(host='redis', port=6379)

def add_numbers(a, b):
    """Helper function for unit testing."""
    return a + b

def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)

@app.route('/')
def hello():
    count = get_hit_count()
    return f'<h1>🚀 Azure DevOps Capstone Stack</h1><p>Visited <strong>{count}</strong> times.</p>'

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)