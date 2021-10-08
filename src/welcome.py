from flask import render_template


def welcome_routes(app):
    @app.route('/')
    @app.route('/home')
    def index():
        return render_template('index.html')

    @app.route('/about')
    def about():
        return render_template('about.html')

    @app.route('/contact')
    def contact():
        return render_template('contact.html')

    @app.route('/menu')
    def menu():
        return render_template('menu.html')
