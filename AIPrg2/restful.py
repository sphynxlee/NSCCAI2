from flask import Flask, request, jsonify

app = Flask(__name__)

bookList = [
    {'title': 'The Great Gatsby', 'author': 'F. Scott Fitzgerald', 'year': 1925},
    {'title': 'To Kill a Mockingbird', 'author': 'Harper Lee', 'year': 1960},
    {'title': 'The Catcher in the Rye', 'author': 'J.D. Salinger', 'year': 1951},
]

@app.route('/books')
def get_books():
    return jsonify(bookList)

@app.route('/')
def home():
    return {'message': 'howdy dude!'}

if __name__ == '__main__':
    app.run()
