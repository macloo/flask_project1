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

With about 30 lines of Python (not including comments and blank lines!), this app produces 21 web pages. No database, no PHP, no AJAX, etc., etc. And the same code could produce 1,000 web pages! All I'd need is a bigger dataset!

## Why was this hard?

I had this app working perfectly in no time on my MacBook, but when I put it on an Apache server, I discovered I could not have *spaces* in the URLS produced by my Flask route. The spaces were converted to `%20`, but Apache choked on those.

Specifically, my dataset includes book titles, which include spaces. Originally, I wanted the Flask-generated URL for a book detail page to look like this:

`awards/Harry Potter and the Goblet of Fire`

Or this:

`awards/Harry%20Potter%20and%20the%20Goblet%20of%20Fire`

But neither one will work on Apache! So the solution was to add code that will produce this instead, using my untouched dataset:

`awards/Harry_Potter_and_the_Goblet_of_Fire`

Sure, I could have added a unique identifier to each book record in my dataset, but I was determined to make it work without touching the data.

## The solution to URLs that include spaces

I wrote a long comment about this in *awards.html*; the short version is that within the [Jinja2 templating code](http://jinja.pocoo.org/docs/2.9/templates/#builtin-filters), I can apply a filter:

`title|replace(" ", "_")`

So I'm building the URL for each title like this, to replace all the spaces with underscores:

`href="{{ url_for('book', title=title|replace(" ", "_")) }}"`

Instead of the original, simpler version:

`href="{{ url_for('book', title=title) }}"`

Now I have both a link and a URL in the browser that have underscores and no spaces (yay), but I'm going to need to switch the underscores back to spaces when I search the dataset to get that exact book from it.

I handled that in the route function, in *winners.py*. The function starts `def book(title):` and that title comes in with underscores. To swap them out for spaces:

`fixed_title = title.replace("_", " ")`

Then I passed `fixed_title` to my *book.html* template, and all is well!
