# Flask project 1

Basic and simple Flask app with one data source (hugo_winners.py) and two routes:

* **/awards/** gets a list of all the book titles in the data source and lists them, as links.

* **/awards/&lt;title&gt;** gets the details for one selected book and shows them on a new page.

The data source is a list of Python dictionaries. Example row:

`{"Title":"Harry Potter and the Goblet of Fire","Author":"J. K. Rowling","Year":2001},`

The .csv file is not used by the app but is in the repo for ease of reading.

After installing all dependencies, run the app by entering its folder and typing:

`$ python winners.py`

## Why is this cool?

With 47 lines of Python (including comments and blank lines!), this app produces 21 web pages. No database, no PHP, no AJAX, etc., etc.
