import MySQLdb
# PythonAnywhere requires this, not PyMySQL
from flask import Flask, render_template, session, redirect, url_for, flash
from flask.ext.bootstrap import Bootstrap
from flask.ext.sqlalchemy import SQLAlchemy

# location of my MySQL databases at PythonAnywhere, used below
basedir = 'macloo.mysql.pythonanywhere-services.com'

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
app.config['SQLALCHEMY_DATABASE_URI'] =\
    'mysql://macloo:paTGIL2277@' + basedir + '/macloo$sockmarket'
#   'mysql://username:password@localhost/db_name'

# app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

bootstrap = Bootstrap(app)
db = SQLAlchemy(app)

# this is a test just to see if the database can connect
@app.route('/')
def testdb():
    if db.session.query('1').from_statement('SELECT 1').all():
        return 'It works.'
    else:
        return 'Something is broken.'

'''
class Sock(db.Model):
    __tablename__ = 'socks'
    __table_args__ = {'autoload':True}
    def __repr__(self):
        # return '<Sock %r>' % self.name
        return '<Sock %r>' % self.id
'''

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

'''
@app.route('/', methods=['GET', 'POST'])
def index():
    given_id = "16"
    id = Sock.query.filter_by(id=given_id)
    if id is None:
        session['known'] = False
    else:
        session['known'] = True
        session['id'] = id
    return render_template('index.html', name=session.get('name'),
                           known=session.get('known', False))
'''

# if __name__ == '__main__':
#     manager.run()
# if __name__ == '__main__':
#    app.run(debug=True)
