from flask import Flask
from src.welcome import welcome_routes
from src.order import order_routes


app = Flask(__name__)
welcome_routes(app)
order_routes(app)


if __name__ == '__main__':
    app.secret_key = 'secret123'
    app.run(debug=True)

