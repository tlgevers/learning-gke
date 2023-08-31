import requests
from flask import Flask, jsonify

app = Flask(__name__)

USER_SERVICE_URL = "http://user-service:8080/user/"
ORDER_SERVICE_URL = "http://order-service:8080/order/"


@app.route('/data/<int:user_id>', methods=['GET'])
def get_data(user_id):
    user = requests.get(USER_SERVICE_URL + str(user_id)).json()
    order = requests.get(ORDER_SERVICE_URL + str(user_id)).json()

    return jsonify({
        "user": user,
        "order": order
    })


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
