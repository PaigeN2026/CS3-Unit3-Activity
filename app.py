from flask import Flask
from flask import render_template, request

# Create an instance of Flask
app = Flask(__name__)

# Function that returns content
# using the app.route decorator to map the URL
@app.route("/")
def index(): 
    # Pass variables from Python to HTML
    genres_list = ['Indie', 'Pop', 'Hip Hop', 'Soul', 'R&B', 'Latin', 'Jazz']

    return render_template("index.html", genres=genres_list)


    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)