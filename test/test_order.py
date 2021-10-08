from flask import Flask
from src.order import order_routes
from src.constants import BQ_SIZE


class TestGet:
    def test_get_bouquet_size(self):
        app = Flask(__name__, template_folder='../templates')
        order_routes(app)
        client = app.test_client()

        url = '/menu/bouquet_size'

        response = client.get(url)
        assert response.status_code == 200
        assert response.request.path == url


class TestPost:
    def test_post_bouquet_size(self):
        app = Flask(__name__, template_folder='../templates')
        order_routes(app)
        client = app.test_client()
        app.secret_key = 'secret123'
        url = '/menu/bouquet_size'

        for i in [1, 3, 6]:
            response = client.post(url, data={'bouquet_size': i})
            assert response.status_code == 200
            assert response.request.path == '/menu/bouquet_size'
            assert BQ_SIZE == [i]

    def test_post_bouquet_size_negative(self):
        app = Flask(__name__, template_folder='../templates')
        order_routes(app)
        client = app.test_client()
        app.secret_key = 'secret123'
        url = '/menu/bouquet_size'
        for i in [0, -1, 'w']:
            response = client.post(url, data={'bouquet_size': i})
            assert response.status_code == 422
            assert response.request.path == '/menu/bouquet_size'

    def test_post_add_to_cart(self):
        app = Flask(__name__, template_folder='../templates')
        app.secret_key = 'secret123'
        order_routes(app)
        client = app.test_client()

        url = '/menu/bouquet_size'
        # giving bouquet size of 4
        client.post(url, data={'bouquet_size': 4})
        response = client.post(url + '/add', data={'number': 2, 'flower_name': 'Rose', 'price': 2.20, 'in_stock': 10})
        assert response.status_code == 200
        assert response.request.path == '/menu/bouquet_size/add'

    def test_post_add_to_cart_negative(self):
        app = Flask(__name__, template_folder='../templates')
        app.secret_key = 'secret123'
        order_routes(app)
        client = app.test_client()

        url = '/menu/bouquet_size'
        # giving bouquet size of 4
        client.post(url, data={'bouquet_size': 4})
        for i in ['h', 6, -2]:
            response = client.post(url + '/add', data={'number': i, 'flower_name': 'Rose', 'price': 2.20, 'in_stock':10}
                                   )
            assert response.status_code == 422
            assert response.request.path == '/menu/bouquet_size/add'

    def test_go_to_cart(self):
        app = Flask(__name__, template_folder='../templates')
        app.secret_key = 'secret123'
        order_routes(app)
        client = app.test_client()

        url = '/menu/bouquet_size/go_to_cart'

        response = client.post(url)
        assert response.status_code == 200
        assert response.request.path == url

    def test_buy(self):
        app = Flask(__name__, template_folder='../templates')
        app.secret_key = 'secret123'
        order_routes(app)
        client = app.test_client()

        url = '/menu/bouquet_size/go_to_cart/buy'
        response = client.post(url)
        assert response.status_code == 200
        assert response.request.path == url
