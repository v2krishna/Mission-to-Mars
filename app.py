from flask import Flask, render_template
from flask_pymongo import PyMongo
import scraping_new

app = Flask(__name__)

#connecting to Mongo uusing PyMongo
#Use flask_mongo to setup mongo connection 
app.config["MONGO_URI"] ="mongodb://localhost:27017/mars_app" # saying our will connect to MongoDB  using a URI 
mongo = PyMongo(app)

#Setup the Routes

@app.route("/")     # tells flask what to display when we're looking at the home page
def index():        # default home page
    mars = mongo.db.mars.find_one() # uses PyMongo to find mars collection
    return render_template("index.html", mars=mars) # tells the flask to return HTML template using the index.html file
    #mars = mars 'tells python to use "mars" collection'
    

@app.route("/scrape") #defines the route that flask will be using, "/scrape" will run the funciton that is created beneath
def scrape(): 
    """
        allow us to access the database , scrape new data using our scraping.py script, update the db and return a message when successful.
    """
    mars= mongo.db.mars # points to mongo db 
    mars_data = scraping_new.scrape_all() # scrape_all is a function in scrapin.py
    mars.update({}, mars_data, upsert=True) # 
    return redirect('/',code=302)


if __name__ == "__main__":
    app.run()