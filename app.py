from flask import Flask, render_template

app = Flask(__name__)

#Dummy data
#This is a list of dictionaries and each dictionaries will represt a single blogPost
posts = [
    {
        'author': 'Parthip MP',
        'title': 'Goat',
        'content': 'Yeah I commited after few months on Git Hub',
        'date_posted': 'Feb 1, 2026'

    },
    {
        'author': 'Prithvi MP',
        'title': 'Bot',
        'content': 'Finally you commited in Git Hub',
        'date_posted': 'Feb 2, 2026'
    }
        ]

@app.route("/")
@app.route("/home")

def home():
    return render_template('home.html', posts=posts)

#In the url bar after the local host link type the name of the function
#example http://127.0.0.1:5000\about. This pops up the about page
@app.route("/about")
def about():
    return render_template('about.html')


#This part is important for the local server to activate
if __name__ == "__main__":
    app.run(debug=True)