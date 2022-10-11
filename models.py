from sqlite3 import Cursor
import sqllite3

ROOT = path.dirname(path.relpath((__file__)))

def create_post(name, content):
    #this function will connect to the db and create a new post
    con = sql.connect(path.join(ROOT, 'database.db'))
    cur = con.cursor()
    cur.execute('insert into posts (name, content) values (?, ?)', (name, content))
    con.commit()
    con.close()

def get_posts():
    #this will connect to the db and get the posts
    con = sql.connect(path.join(ROOT, 'database.db'))
    cur = con.cursor()
    cur.execute('select * from posts')
    posts = cur.fetchall()
    return posts