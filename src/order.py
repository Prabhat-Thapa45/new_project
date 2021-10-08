from flask import flash, render_template, request
from src.order_backend import validate_entry
from src.constants import STOCK, BQ_SIZE, YOUR_CART
from src.order_backend import flower_out_of_stock, bq_size_exceeded, adding_to_cart, \
    update_stock, check_order_criteria, proceed_to_buy


def order_routes(app):
    @app.route('/menu/bouquet_size', methods=['GET', 'POST'])
    def bouquet_size():
        if request.method == 'POST':
            size = request.form['bouquet_size']
            valid_size = validate_entry(size)
            if not valid_size:
                flash('Invalid entry', 'danger')
                return render_template('bouquet_size.html'), 422
            BQ_SIZE[0] = valid_size
            return render_template("show_flower.html", items=STOCK)
        return render_template('bouquet_size.html')

    @app.route('/menu/bouquet_size/add', methods=['POST'])
    def add_to_cart():
        if request.method == 'POST':
            order_quantity = request.form['number']
            flower_name = request.form['flower_name']
            in_stock = int(request.form['in_stock'])
            price = float(request.form['price'])

            # validates order_quantity and returns None if invalid i.e. -ve or string
            valid_order_quantity = validate_entry(order_quantity)
            # runs if order_quantity is invalid
            if not valid_order_quantity:
                flash('Invalid entry', 'danger')
                return render_template('show_flower.html', items=STOCK), 422
            if flower_out_of_stock(valid_order_quantity, in_stock):
                flash('We are out of stock. You may order something else or cancel order', 'danger')
                return render_template('show_flower.html', items=STOCK), 422
            if bq_size_exceeded(valid_order_quantity):
                flash(f'you have exceeded your bouquet size. You have {BQ_SIZE[0]} flowers left to add', 'danger')
                return render_template('show_flower.html', items=STOCK), 422

            # adds items to your cart and reduces bq_size by valid_order_quantity
            adding_to_cart(valid_order_quantity, flower_name, price)
            update_stock(flower_name, valid_order_quantity)
            flash(f'Flower added to cart. You have {BQ_SIZE[0]} flowers left to add', 'success')
            return render_template('show_flower.html', items=STOCK)

    @app.route('/menu/bouquet_size/go_to_cart', methods=['POST'])
    def go_to_cart():
        if request.method == 'POST':
            if not check_order_criteria():
                flash(f'You still have {BQ_SIZE[0]} flowers left to order', 'danger')
                return render_template('show_flower.html', items=STOCK)
            return render_template('go_to_cart.html', items=YOUR_CART)

    @app.route('/menu/bouquet_size/go_to_cart/buy', methods=['POST'])
    def buy():
        if request.method == 'POST':
            flash(proceed_to_buy(), 'success')
            return render_template('order_placed.html')
