from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/order/<int:user_id>', methods=['GET'])
def get_order(user_id):
    return jsonify({
        "order_id": 12345,
        "user_id": user_id,
        "items": ["item1", "item2"]
    })


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
