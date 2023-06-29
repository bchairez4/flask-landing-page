from flask import Flask, render_template

app = Flask(__name__)

navbarList = ['Home', 'Adopt', 'About']

@app.route('/')
def index():
    return render_template('index.html', navbarList=navbarList)

@app.route('/adopt')
def adopt():
    adoptionList = [{'img_src': 'link', 'animal': 'dog', 'breed': 'doggy', 'name': 'name', 'age': 0},
                    {'img_src': 'link', 'animal': 'dog', 'breed': 'doggy', 'name': 'name', 'age': 0},
                    {'img_src': 'link', 'animal': 'dog', 'breed': 'doggy', 'name': 'name', 'age': 0},
                    {'img_src': 'link', 'animal': 'dog', 'breed': 'doggy', 'name': 'name', 'age': 0},
                    {'img_src': 'link', 'animal': 'dog', 'breed': 'doggy', 'name': 'name', 'age': 0}]
    return render_template('adopt.html', navbarList=navbarList, adoptionList=adoptionList)

@app.route('/about')
def about():
    return render_template('about.html', navbarList=navbarList)

def main():
    app.run()

if __name__ == '__main__':
    main()
