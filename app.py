from flask import Flask
from flask import render_template, request

# Create an instance of Flask
app = Flask(__name__)

# Function that returns content
# using the app.route decorator to map the URL
@app.route("/")
def index(): 
    # Pass variables from Python to HTML
    genres = {'Indie' : 'indie.html', 
                'Pop' : 'pop.html', 
                   'Hip Hop': 'hiphop.html', 
                   'Soul' : 'soul.html', 
                   'R&B' : 'rnb.html', 
                   'Latin' : 'latin.html', 
                   'Jazz' : 'jazz.html'}

    return render_template("index.html", genres=genres)


    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)