# Brian Chairez
# Flask Pet Adoption Landing Page

import sqlite3
from flask import Flask, render_template, request, redirect, url_for, flash

def get_db_connection():
    connection = sqlite3.connect('database.db')
    connection.row_factory = sqlite3.Row
    return connection

app = Flask(__name__)
app.config['SECRET_KEY'] = ' REPLACE WITH YOUR SECRET KEY '

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/adopt')
def adopt():
    adoptionList = [
        {'img_src': 'static/images/adopt-animal-1.jpg', 'animal': 'dog', 'breed': 'doggy', 'name': 'Fluffy', 'age': 1},
        {'img_src': 'static/images/adopt-animal-2.jpg', 'animal': 'dog', 'breed': 'doggy', 'name': 'Softy', 'age': 2},
        {'img_src': 'static/images/adopt-animal-3.jpg', 'animal': 'dog', 'breed': 'doggy', 'name': 'Bruce', 'age': 4},
        {'img_src': 'static/images/adopt-animal-4.jpg', 'animal': 'cat', 'breed': 'kitty', 'name': 'Nightfall', 'age': 3},
        {'img_src': 'static/images/adopt-animal-5.jpg', 'animal': 'cat', 'breed': 'kitty', 'name': 'Bucky', 'age': 5},
        {'img_src': 'static/images/adopt-animal-6.jpg', 'animal': 'cat', 'breed': 'kitty', 'name': 'Mao-San', 'age': 3}
    ]
    return render_template('adopt.html', adoptionList=adoptionList)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/reviews')
def reviews():
    reviewList = [
        {'img_src': 'static/images/adopt-review-1.jpg', 'name': 'John Doe', 'petName': 'Rodolfo', 'rating': 'Outstanding'},
        {'img_src': 'static/images/adopt-review-2.jpg', 'name': 'Jane Dane', 'petName': 'Stinky', 'rating': 'Great'},
        {'img_src': 'static/images/adopt-review-3.jpg', 'name': 'Sally Sal', 'petName': 'Teacup', 'rating': 'In Love'},
        {'img_src': 'static/images/adopt-review-4.jpg', 'name': 'Billy Bob', 'petName': 'Annihilator', 'rating': 'Amazing'}
    ]
    return render_template('reviews.html', reviewList=reviewList)

@app.route('/community', methods=('GET', 'POST'))
def community():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Post title is required!')
        elif not content:
            flash('Post content is required!')
        else:
            conn = get_db_connection()
            conn.execute('INSERT INTO posts (title, content) VALUES (?, ?)', (title, content))
            conn.commit()
            conn.close()
            return redirect(url_for('community'))
    else:
        conn = get_db_connection()
        posts = conn.execute('SELECT * FROM posts').fetchall()
        conn.close() 
    return render_template('community.html', posts=posts)

def main():
    app.run()

if __name__ == '__main__':
    main()
