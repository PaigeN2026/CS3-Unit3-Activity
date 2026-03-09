from flask import Flask
from flask import render_template, request

# Create an instance of Flask
app = Flask(__name__)

# Function that returns content
# using the app.route decorator to map the URL
@app.route("/")
def index(): 
    # Pass variables from Python to HTML
    genres = {  'Indie' : 'indie.html', 
                'Pop' : 'pop.html', 
                'Hip Hop': 'hiphop.html', 
                'Soul' : 'soul.html', 
                'R&B' : 'rnb.html', 
                'Latin' : 'latin.html', 
                'Jazz' : 'jazz.html'}

    return render_template("index.html", genres=genres)

@app.route("/submit", methods=['POST'])
def submit():
    selected_genre = request.form.get('genres')
    if selected_genre == "INDIE":
        return render_template("indie.html")
    
    elif selected_genre == "POP":
        return render_template("pop.html")
    
    elif selected_genre == "JAZZ":
        return render_template("jazz.html")
    
    elif selected_genre == "HIPHOP":
        return render_template("hiphop.html")
    
    elif selected_genre == "LATIN":
        return render_template("latin.html")
    
    elif selected_genre == "RNB":
        return render_template("rnb.html")
    
    elif selected_genre == "SOUL":
        return render_template("soul.html")
    
    return render_template("error.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)