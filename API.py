from flask import Flask, jsonify, request

api = Flask(__name__)

books = [
    {
        'id': 1,
        'title': 'Pyhonic Mastery: From Beginner to Pro',
        'actor': 'J.R Tolkyen',
    },
    {
        'id': 2,
        'title': 'Understand The Logic Of Programming',
        'actor': 'J.K Houlyng',
    },
    {
        'id': 3,
        'title': 'Millionaire Mind',
        'actor': 'J.P Mark',
    }
]

@api.route('/books', methods = ['GET'])
def get_book():

    return jsonify(books), 200

@api.route('/books/<int:id>', methods = ['GET'])
def get_book_for_id(id):

    for book in books:
        if book.get('id') == id:
            return jsonify(book), 200

    return jsonify({"error": "Book not found"}), 404

@api.route('/books/<int:id>', methods = ['PUT'])
def edit_book_for_id(id):

    changed_book = request.get_json()
    for indice, book in enumerate(books):

        if book.get('id') == id:
            books[indice].update(changed_book)
            return jsonify(books[indice]), 200
        
    return jsonify({"error": "Book not found"}), 404

@api.route('/books', methods = ['POST'])
def include_new_book():

    new_book = request.get_json()

    if not new_book.get('id') or not new_book.get('title') or not new_book.get('actor'):
        return jsonify({"error": "Missing fields: id, actor and title"}), 400

    for book in books:
        if book.get('id') == new_book.get('id'):
            return jsonify({"error": "ID already exists!"}), 400

    books.append(new_book)
    return jsonify(new_book), 201
    
@api.route('/books/<int:id>', methods = ['DELETE'])
def delete_book(id):

    for indice, book in enumerate(books):
        if book.get('id') == id:

            deleted = books.pop(indice)
            return jsonify(deleted), 200
        
    return jsonify({"error": "Book not found"}), 404
    

if __name__ == '__main__':
    api.run(port=5000, host='localhost', debug=True)