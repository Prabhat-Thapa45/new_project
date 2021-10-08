from flask import Flask
from src.welcome import welcome_routes


def test_index():
    app = Flask(__name__, template_folder='../templates')
    welcome_routes(app)
    client = app.test_client()

    url = '/'
    response = client.get(url)
    assert response.status_code == 200
    assert response.request.path == url


def test_about():
    app = Flask(__name__, template_folder='../templates')
    welcome_routes(app)
    client = app.test_client()

    url = '/about'
    response = client.get(url)
    assert response.status_code == 200
    assert response.request.path == url


def test_contact():
    app = Flask(__name__, template_folder='../templates')
    welcome_routes(app)
    client = app.test_client()

    url = '/contact'
    response = client.get(url)
    assert response.status_code == 200
    assert response.request.path == url


def test_menu():
    app = Flask(__name__, template_folder='../templates')
    welcome_routes(app)
    client = app.test_client()

    url = '/menu'
    response = client.get(url)
    assert response.status_code == 200
    assert response.request.path == url
