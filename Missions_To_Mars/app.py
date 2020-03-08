from flask import Flask, render_template, redirect
from flask_pymongo import Pymongo
import mission_to_mars

app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/mars"
mongo = PyMongo(app)

@app.route("/")
def index():
    mars = mongo.db.mars.
    return render_template("index.html" , mars = mars)

@app.route("/scrape")
def scrape():
    mars = mongo.db.mars
    mars_web = mission_to_mars.scrape_news()
    # mars_web = mission_to_mars.scrape_news()
    mars_web = mission_to_mars.mars_facts_scrape()
    mars_web = mission_to_mars.hemishpere_scrape()

    mars.update({}, mars_web, upsert = True)
    return redirect("/", code=302)

if __name__ == "__main__":
    app.run(debug=False)