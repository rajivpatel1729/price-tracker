from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
import time
from model import db, ProductData, ProductInfo, TrackingProduct
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from scripts.send_mail import send_email

def get_info(url):
    result = list()
    my_url = url
    uClient = uReq(my_url)
    page_html = uClient.read()
    uClient.close()
    page_soup = soup(page_html, "html.parser")

    containers = page_soup.find_all("div", {"class": "_1YokD2 _3Mn1Gg col-8-12"})
    container = containers[0]
    price = container.findAll("div", {"class": "CEmiEU"})
    product_name = container.findAll("span", {"class": "B_NuCI"})
    result.append(str(time.ctime(time.time())))
    result.append(str(product_name[0].text))
    result.append(str("Rs." + price[0].text.split("₹")[1]))
    return result


def check_price(url, curr_price, product_name):
    check_product = list(ProductInfo.query.filter(ProductInfo.link == url).all())[-1]
    if curr_price <= check_product.price:
        clients = list(client.email for client in TrackingProduct.query.filter(TrackingProduct.link == url).all())
        print(clients)
        send_email(clients, product_name, curr_price)
        print("notification send to all clients")


def manage_data(url):
    result = get_info(url)
    info = ProductInfo(link=str(url), time=result[0], price=result[2])
    check_price(url, result[2], result[1])
    db.session.add(info)
    db.session.commit()


def add_data(url):
    result = get_info(url)
    data = ProductData(link=str(url), name=result[1])
    info = ProductInfo(link=str(url), time=result[0], price=result[2])
    db.session.add(data)
    db.session.add(info)
    db.session.commit()


def add_client(url, mail):
    client = TrackingProduct(email=str(mail), link=str(url))
    db.session.add(client)
    db.session.commit()


def get_data(url):
    arr = []
    data = ProductData.query.filter(ProductData.link == url).first()
    temp = {"Name": data.name}
    arr.append(temp)
    info = ProductInfo.query.filter(ProductData.link == url).all()
    for product in info:
        temp = {"Time": product.time, "Price": product.price}
        arr.append(temp)
    return arr


def update_data():
    data = list(set([product.link for product in ProductData.query.all()]))
    for url in data:
        manage_data(url)
    print("All product prices are updated in db")


if __name__ == "__main__":
    from app import *

    with app.app_context():
        db.create_all()
        update_data()
