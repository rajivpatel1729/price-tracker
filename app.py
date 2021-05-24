from flask import Flask, request, jsonify
from config.database import PRICETRACKER_DB_SQLITE_PATH
from model import db, ProductData, ProductInfo, TrackingProduct
from scripts.update_product_data import manage_data, get_info, add_data, get_data, add_client


app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = PRICETRACKER_DB_SQLITE_PATH

db.init_app(app)

with app.app_context():
    db.create_all()


@app.route("/link", methods=["GET"])
def display_data():
    url = request.form.get("url")
    if ProductData.query.filter(ProductData.link == url).first():
        temp = get_data(url)
        return jsonify(temp)
    else:
        add_data(url)
        result = get_data(url)
        return jsonify(result)

@app.route("/trackproduct", methods=["GET"])
def track_data():
    url = request.form.get("url")
    email = request.form.get("email")
    if ProductData.query.filter(ProductData.link == url).first():
        pass

    else:
        add_data(url)

    trackers = list(TrackingProduct.query.filter(TrackingProduct.link == url).all())

    if email in [tracker.email for tracker in trackers]:
        return jsonify("you are already tracking this order")

    else:
        add_client(url, email)
        product = get_info(url)
        product_name = product[1]
        return jsonify("Tracking your product " + product_name)


if __name__ == "__main__":
    app.run(debug=True)
    # input_url = "https://www.flipkart.com/apple-iphone-11-white-64-gb/p/itmfc6a7091eb20b?pid=MOBFWQ6BVWVEH3XE&lid=LSTMOBFWQ6BVWVEH3XESAHPTP&marketplace=FLIPKART&srno=s_1_1&otracker=search&otracker1=search&fm=SEARCH&iid=ab1d4183-fd6f-46de-9b79-988cbdd84986.MOBFWQ6BVWVEH3XE.SEARCH&ppt=sp&ppn=sp&ssid=egw6rfs41c0000001614545570799&qH=0b3f45b266a97d70"
