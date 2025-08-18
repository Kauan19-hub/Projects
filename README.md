**<h5>README em desenvolvimento... 🛠️<h5>**

###

**<h2>🚀 Tutorial da API 🚀</h2>**

###

Neste repositório, estarei compartilhando e explicando sobre minha nova API desenvolvida em **Python!**<br>
Podemos criar uma API sobre qualquer coisa, ela envolve um código bem simples, além de ser muito legal<br>
para aprender e se divertir programando! Essa API funciona da seguinte forma:

###

✅ Ela possui 3 Livros com 1 ID cada; <br>
✅ Ela possui também, um link do localhost; <br>
✅ no software de teste, é possível **adicionar**, **editar**, e **excluir** um livro!

###

**<h2>📂 Este projeto mostra:</h2>**

###

- Desenvolver uma API em Python;
- Utilizar a biblioteca `Flask` ou `FastAPI`, depende de sua escolha;
- Fazer requisições usando Insomnia ou Postman;
- Compreender cada parte do código com comentários.

###

**<h2>🛠 Passos para utilizar a API</h2>**

###

Siga o passo a passo sobre como utilizar uma API. 

**<h2>1️⃣ Ferramentas para teste</h2>**

###

Você pode escolher entre **Postman** ou **Insomnia**:

###

[Download Postman](https://www.postman.com/downloads/ "Baixe o Postman e teste sua API!")

[Download Insomnia](https://insomnia.rest/download "Baixe o Insomnia e teste sua API!")

###

> 💡 Caso prefira, utilize apenas uma das duas ferramentas.

---

**<h2>2️⃣ Instalação do Flask</h2>**

###

Se estiver no Windows, no terminal, execute:

###
```bash
pip install flask
```
###

Se estiver no Linux ou MacOS, no terminal, execute:

###
```bash
pip3 install flask
```

###

**<h2>🖥 Código fonte - (`Arquivo PY`)</h2>**

###
```python
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
```

###

**<h2>📑Passo a passo explicado:</h2>**

###
```python
from flask import Flask, jsonify, request
````

###

Importa o Flask e métodos necessários para a criação da API

###
```python
api = Flask(__name__)
```

###

Cria uma instância da aplicação Flask

###
```python
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
```

###

Lista de livros inicial (serve como "banco de dados" fake para este exemplo)

###
```python
@api.route('/books', methods=['GET'])
```

###

Rota para listar todos os livros

###
```python
def get_book():
```

###

