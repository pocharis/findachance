from datetime import datetime
from flask import Flask, jsonify, request, flash, url_for, redirect,render_template, send_from_directory
from flask_pymongo import PyMongo
from bson.json_util import dumps





app = Flask(__name__,static_url_path='', static_folder='./static',template_folder='./templates')
# app.config["MONGO_URI"] = "mongodb://localhost:27017/findachance"
app.config["MONGO_URI"] = "mongodb://findachance:pocha419@ds161183.mlab.com:61183/findachance"

mongo = PyMongo(app)





@app.route('/')
def home():
    date = datetime.utcnow().strftime('%B %d %Y')
    mongo.db.findachance.insert({"img_src":"news_thumbnail3.jpg", "alt":"My Sixth News Item", "title":"My inserted News Item"})
    finder = mongo.db.findachance.find({})
    
    new_finder = [item for item in finder]

    print(type(new_finder))
    # return render_template("show_all.html", finder=new_finder, date=date)
    return render_template('index.html', date=date, finder=new_finder)


if __name__ =="__main__":
    app.run(debug=True,port=8081)

    # CREATE TABLE account(user_id serial PRIMARY KEY,username VARCHAR (50) UNIQUE NOT NULL,password VARCHAR (50) NOT NULL,email VARCHAR (355) UNIQUE NOT NULL,created_on TIMESTAMP NOT NULL,last_login TIMESTAMP);