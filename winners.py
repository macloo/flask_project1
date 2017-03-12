# coding: utf-8
"""
A small Flask app reads from a datasource
"""
from flask import Flask, render_template
from hugo_winners import HUGO_WINNERS

app = Flask(__name__)

# for WSGI
# application = app


# define two functions to be used by the routes

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

@app.route('/')
def home():
    return '<h1>Go to /awards/</h1>'

@app.route('/awards/')
def awards():
    titles = get_titles(HUGO_WINNERS)
    # pass the sorted list of titles to the template
    return render_template('awards.html', titles=titles)

@app.route('/awards/<title>')
def book(title):
    # the URL will have underscores in place of spaces - fix that
    fixed_title = title.replace("_", " ")
    # get variables for the book detail page: pass title with spaces restored
    # to the function that will find that book's record
    title, author, year = get_bookdata(HUGO_WINNERS, fixed_title)
    # pass the data for the selected book to the template
    return render_template('book.html', title=title, author=author,
    year=year)

if __name__ == '__main__':
    app.run(debug=True)
