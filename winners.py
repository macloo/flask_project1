# coding: utf-8
# assignment 10: a small Flask app
from flask import Flask, render_template
from hugo_winners import HUGO_WINNERS

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>This is the home page.</h1><p>Go to /awards/</p>'

# retrieve all the titles from the dataset and put them into a list
def get_titles(source):
    titles = []
    for row in source:
        title = row["Title"]
        titles.append(title)
    return sorted(titles)

# find the row that matches the title in the URL, retrieve author and year
def get_bookdata(source, title):
    for row in source:
        if title == row["Title"]:
            # decode handles accented characters
            author = row["Author"].decode('utf-8')
            year = row["Year"]
    return title, author, year

@app.route('/awards')
def awards():
    titles = get_titles(HUGO_WINNERS)
    return render_template('awards.html', titles=titles)

@app.route('/awards/<title>')
def book(title):
    t, a, y = get_bookdata(HUGO_WINNERS, title)
    return render_template('book.html', title=t, author=a,
    year=y)

if __name__ == '__main__':
    app.run(debug=True)
