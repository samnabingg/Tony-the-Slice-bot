from flask import Flask, render_template, request, jsonify, session, g, redirect, url_for
import pymysql
import uuid
import random
import string
from random import randint
app = Flask(__name__)
app.secret_key = '123'

def get_db_connection():
    try:
        conn = pymysql.connect(host='127.0.0.1', user='root', password='password', db='restaurant')
        return conn
    except pymysql.MySQLError as e:
        print(f"Database connection error: {e}")
        return None

@app.before_request
def before_request():
    g.db_connection = get_db_connection()
    if not g.db_connection:
        return "Failed to connect to database."

@app.route('/menu')
def menu_page():
    return render_template('menu.html')

@app.route('/points')
def points():
    return render_template('points.html')

@app.route('/orders')
def orders():
    return render_template('orders.html')

@app.route('/timer')
def timer_page():
    return render_template('timer.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/')
def home():
    return render_template('login.html')

def generate_unique_order_id():
    digits = string.digits
    order_id = ''.join(random.choices(digits, k=2))
    return order_id

@app.route('/api/order-summary', methods=['POST'])
def order_summary():
    data = request.get_json()
    app.logger.info("Received data: %s", data)

    # Check if 'orderData' is in the request
    if 'orderData' not in data:
        return jsonify({"message": "No 'orderData' found in the request"}), 400

    # Get the 'orderData' dictionary
    order_data = data.get('orderData')

    # Get the 'selectedItems' array
    selected_items = order_data.get('selectedItems')

    # Check if 'cId' is in the session
    cId = session.get('cId')
    if cId is None:
        return jsonify({"message": "Customer ID (cId) is missing from the session"}), 400

    # Generate a unique order ID
    order_id = generate_unique_order_id()

    # Continue processing the orderData
    conn = g.db_connection
    if not conn:
        app.logger.error("Failed to connect to database.")
        return jsonify({"message": "Failed to connect to database."}), 500

    try:
        with conn.cursor() as cursor:
            for item in selected_items:
                itemId = item.get('itemId')
                itemName = item.get('itemName')
                price = item.get('price')
                quantity = item.get('quantity')  # Get the quantity
                if not itemId or not itemName or not price or not quantity:
                    app.logger.warning("Skipping item with missing information: %s", item)
                    continue
                total_amount = price * quantity  # Calculate total amount
                app.logger.info("Inserting item: %s with order ID: %s", item, order_id)
                cursor.execute("INSERT INTO orders (orderId, cId, itemId, totalAmount, itemName, quantity) VALUES (%s, %s, %s, %s, %s, %s)",
                               (order_id, cId, itemId, total_amount, itemName, quantity))
            conn.commit()
        return jsonify({"message": "Order summary received and processed successfully"}), 200
    except Exception as e:
        conn.rollback()
        app.logger.error("Error processing order summary: %s", str(e))
        return jsonify({"message": "Error processing order summary", "error": str(e)}), 500
    finally:
        conn.close()




@app.route('/submit', methods=['POST'])
def submit_form():
    username = request.form.get('username')
    phone_number = request.form.get('phone_number')

    conn = g.db_connection
    if not conn:
        return "Failed to connect to database."

    try:
        with conn.cursor() as cursor:
            cursor.execute("INSERT INTO customers (username, phone_number) VALUES (%s, %s)", (username, phone_number))
            conn.commit()

            # Get the cId of the customer
            cId = cursor.lastrowid

            # Store the cId in the session
            session['cId'] = cId

        return redirect('/menu')  # Redirect to the menu page after successful submission
    except pymysql.IntegrityError as e:
        if e.args[0] == 1062:  # Duplicate entry error code
            return render_template('web.html', username=username, cId=session.get('cId'))
        else:
            print(f"Error inserting customer data: {e}")
            conn.rollback()
            return f"Failed to insert customer data: {e}"
    finally:
        conn.close()
@app.route('/api/rewards', methods=['GET'])
def get_rewards():
    conn = get_db_connection()
    if not conn:
        return jsonify({"message": "Failed to connect to database."}), 500

    try:
        with conn.cursor() as cursor:
            query = "SELECT * FROM rewards"
            cursor.execute(query)
            rewards = cursor.fetchall()
            rewards_list = [{'rId': r[0], 'cId': r[1], 'amount': r[2]} for r in rewards]
            return jsonify(rewards_list), 200
    except Exception as e:
        app.logger.error("Error fetching rewards: %s", str(e))
        return jsonify({"message": "Error fetching rewards", "error": str(e)}), 500
    finally:
        conn.close()

@app.route('/api/redeem_reward', methods=['POST'])
def redeem_reward():
    points = request.json.get('points', 0)
    if points >= 10:
        
        return redirect(url_for('orders.html'))
    else:
        return jsonify({'message': 'Not enough points to redeem this reward.'}), 400



if __name__ == '__main__':
    app.run(debug=True)
