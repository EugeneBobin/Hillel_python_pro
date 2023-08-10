from flask import Flask

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
    return []


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
    con = sqlite3.connect("dish.db")
    new_cur = con.cursor()
    res = new_cur.execute('SELECT * FROM Address')
    result = res.fetchall()
    return result

@app.route('/user/address/<id>', methods = ['GET', 'POST'])
def user_address_page(id : int):
    return []


@app.route('/menu', methods = ['GET'])
def menu_page():
    con = sqlite3.connect("dish.db")
    new_cur = con.cursor()
    res = new_cur.execute('SELECT * FROM Dishes')
    result = res.fetchall()
    return result


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
    con = sqlite3.connect("dish.db")
    new_cur = con.cursor()
    res = new_cur.execute('SELECT * FROM Category')
    result = res.fetchall()
    return result


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