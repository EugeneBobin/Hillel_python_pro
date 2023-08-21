from flask import Flask, request

from functions import SQLite_db

app = Flask(__name__)

import sqlite3

@app.route('/cart', methods = ['GET', 'PUT'])
def cart_page():
    return []


@app.route('/cart/order', methods = ['POST'])
def order_page():
    return []


@app.route('/cart/add', methods = ['POST', 'PUT'])
def cart_add_page():
    return []


@app.route('/user', methods = ['GET', 'POST', 'DELETE'])
def user_page():
    with SQLite_db("dish.db") as db:
        if request.method == 'POST':
            data = request.json
            db.insert_into('User', data)

        users = db.select_from(table_name='User', columns=['*'])

    return str(users)


@app.route('/user/register', methods = ['POST'])
def user_register_page():
    return []


@app.route('/user/signIn', methods = ['POST'])
def user_sign_in_page():
    return []


@app.route('/user/logout', methods = ['GET', 'POST'])
def user_logout_page():
    return []


@app.route('/user/restore', methods = ['POST'])
def user_restore_page():
    return []


@app.route('/user/orders', methods = ['GET'])
def user_order_history_page():
    return []


@app.route('/user/orders/<id>', methods = ['GET'])
def user_order_page(id : int):
    return []


@app.route('/user/address', methods = ['GET', 'POST'])
def user_adress_list_page():
    with SQLite_db("dish.db") as db:
        if request.method == 'POST':
            data = request.json
            db.insert_into('Address', data)

        address = db.select_from(table_name='Address', columns=['*'])

    return str(address)

@app.route('/user/address/<id>', methods = ['GET', 'POST'])
def user_address_page(id : int):
    return []


@app.route('/menu', methods = ['GET', 'POST'])
def menu_page():
    with SQLite_db('dish.db') as db:
        if request.method == 'POST':
            data = request.form.to_dict()
            data['ID'] = data["Dish_name"].replace(' ', '_')
            data['Availability'] = 1
            db.insert_into('Dishes', data)

        dishes = db.select_from('Dishes', ['*'])
    html_form = f"""
        <form method="POST">
            <input type="text" name="Dish_name" placeholder="Dish_name">
            <input type="text" name="Price" placeholder="Price">
            <input type="text" name="Description" placeholder="Description">
            <input type="text" name="Photo" placeholder="Photo">
            <input type="text" name="Category" placeholder="Category">
            <input type="text" name="Calories" placeholder="Calories">
            <input type="text" name="Protein" placeholder="Protein">
            <input type="text" name="Fat" placeholder="Fat">
            <input type="text" name="Carbs" placeholder="Carbs">
            <input type="submit">
        </form>
        <br>
        {str(dishes)}
        """
    return html_form

@app.route('/menu/<cat_name>', methods = ['GET'])
def menu_category_page():
    return []


@app.route('/menu/<cat_name>/<dish>', methods = ['GET'])
def menu_category_dish_page():
    return []


@app.route('/menu/<cat_name>/<dish>/review', methods = ['POST'])
def menu_category_dish_review_page():
    return []


@app.route('/menu/search', methods = ['GET', 'POST'])
def menu_search_page():
    return []


@app.route('/admin', methods = ['GET'])
def admin_page():
    return []


@app.route('/admin/categories', methods = ['GET', 'POST'])
def admin_categories_page():
    with SQLite_db("dish.db") as db:
        if request.method == 'POST':
            data = request.json
            db.insert_into('Category', data)

        categories = db.select_from(table_name='Category', columns=['*'])

    return str(categories)


@app.route('/admin/categories/<category>', methods = ['GET', 'PUT', 'DELETE'])
def admin_category_page():
    return []


@app.route('/admin/dishes', methods = ['GET', 'POST'])
def admin_dishes_page():
    return []


@app.route('/admin/dishes/<dish>', methods = ['GET', 'PUT', 'DELETE'])
def admin_dish_page():
    return []


@app.route('/admin/orders', methods = ['GET'])
def admin_orders_page():
    return []


@app.route('/admin/orders/<order>', methods = ['GET', 'PUT'])
def admin_order_page():
    return []


@app.route('/admin/search', methods = ['GET'])
def adminSearchPage():
    return []


if __name__ == '__main__':
    app.run()
    