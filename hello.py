from flask import Flask

app = Flask(__name__)

@app.route("/")
@app.route("/home")

def home():
    return "<h1>Hello Home,Page</h1>"

#In the url bar after the local host link type the name of the function
#example http://127.0.0.1:5000\about. This pops up the about page
@app.route("/about")
def about():
    return "<h1>Hello About,Page</h1>"


#This part is important for the local server to activate
if __name__ == "__main__":
    app.run(debug=True)