from flask import Flask, render_template, redirect
import pymongo
import mission_to_mars

app = Flask(__name__)

conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)

db = client.mars

@app.route("/")
def index():
    mars = db.mars.find_one()
    return render_template("index.html" , mars = mars)

@app.route("/scrape")
def scrape():
    mars = db.mars
    mars_web = mission_to_mars.scrape_news()
    # mars_web = mission_to_mars.scrape_news()
    mars_web = mission_to_mars.mars_facts_scrape()
    mars_web = mission_to_mars.hemishpere_scrape()

    mars.update({}, mars_web, upsert = True)
    return redirect("/", code=302)

if __name__ == "__main__":
    app.run(debug=False)