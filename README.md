<div align="center">
    <img src=""/>
</div>

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

**<h2>1️⃣ Ferramentas para teste:</h2>**

###

Você pode escolher entre **Postman** ou **Insomnia**:

###

[Download Postman](https://www.postman.com/downloads/ "Baixe o Postman e teste sua API!")

[Download Insomnia](https://insomnia.rest/download "Baixe o Insomnia e teste sua API!")

###

> 💡 Caso prefira, utilize apenas uma das duas ferramentas.

---

**<h2>2️⃣ Instalação do Flask:</h2>**

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

**<h2>📌 Explicação do código:</h2>**

###

1️⃣ **Import:**

###

- `Flask`: cria a aplicação;
- `jsonify`: transforma objetos Python em JSON;
- `request`: permite acessar os dados da requisição.

###

2️⃣ **Rotas:**

###

- `GET /books`: retorna todos os livros;
- `GET /books/<id>`: retorna um livro com o id especificado;
- `PUT /books/<id>`: atualiza um livro com base no seu id;
- `POST /books`: adiciona um novo livro à lista;
- `DELETE /books/<id>`: deleta um livro com o id especificado.

###

3️⃣ **Validações:**

###

- A API analisa se os dados necessários estão presentes nas requisições (por exemplo, ao adicionar um livro novo)<br>
e retorna mensagens de erro apropriadas.

###

4️⃣ **Servidores:**

- O servidor é chamado localmente, na porta 5000, e com o modo debug ativado para facilitar a depuração (correção de bug).

###

**<h2> ⚙ Como usar no Postman/Insomnia:</h2>**

###

✅ `GET /books`: Listar livros;<br>
✅ `URL`: [http://localhost:5000/books](http://localhost:5000/books "Não precisa acessar este link");<br>
✅ Método: `GET`;<br>
✅ Corpo: Nenhum.<br>

###

**<h2>🧪 Resposta esperada:</h2>**

###
```json
[
  {
    "id": 1,
    "title": "Pyhonic Mastery: From Beginner to Pro",
    "actor": "J.R Tolkyen"
  }
]
```

###

✅ `GET /books/<id>`: Obter livro por ID;<br>
✅ `URL`: [http://localhost:5000/books/1](http://localhost:5000/books/1 "Não precisa acessar este link");<br>
✅ Método: `GET`.

###

**<h2>🧪 Resposta esperada, caso ele exista:</h2>**

###
```json
{
  "id": 1,
  "title": "Pyhonic Mastery: From Beginner to Pro",
  "actor": "J.R Tolkyen"
}
```

###

✅ `POST /books`: Adicionar novo livro;<br>
✅ `URL`: [http://localhost:5000/books](http://localhost:5000/books "Não precisa acessar este link");<br>
✅ Método: `POST`;
✅ Body: `JSON`.

###
```json
{
  "id": 4,
  "title": "New Book Title",
  "actor": "New Author"
}
```

###

- Headers

###

    Content-Type: application/json

###

**<h2>🧪 Resposta esperada:</h2>**

###
```json
{
  "id": 4,
  "title": "New Book Title",
  "actor": "New Author"
}
```

###

**<h2>❌ Erros comuns de acontecer:</h2>**

###

- Se os campos estiverem faltando (`id`, `title`, `actor`) - retorna status `400`
- Se o `ID` for duplicado - retorna status `400`

###

✅ `PUT /books/<id>` – Editar um livro existente;<br>
✅ `URL`: [http://localhost:5000/books/2](http://localhost:5000/books/2 "Não precisa acessar este link");<br>
✅ Método: `PUT`;<br>
✅ Body `JSON`.

###
```json
{
  "title": "Updated Book Title"
}
```

###

**<h2>🧪 Resposta esperada:</h2>**

###
```json
{
  "id": 2,
  "title": "Updated Book Title",
  "actor": "J.K Houlyng"
}
```

###

✅ `DELETE /books/<id>` - Deletar um livro;<br>
✅ `URL`: [http://localhost:5000/books/2](http://localhost:5000/books/3 "Não precisa acessar este link");<br>
✅ Método: `DELETE`.

###

**<h2>🧪 Resposta esperada:</h2>**

###
```json
{
  "id": 3,
  "title": "Millionaire Mind",
  "actor": "J.P Mark"
}
```

###

**<h2>🚀 Dicas extras para Insomnia e Postman:</h2>**

###

**📩 Postman**

###

- Abra o Postman, e crie um **Collection**;
- Crie uma **Request** dentro dela;
- Escolha o `HTTP` certo: (`GET`, `POST`...);
- Caso seja `POST` ou `PUT`, vá em `BODY` - `RAW` - `JSON`;
- Insira a URL e teste em `SEND`.

###

**📩 Insomnia**

###

- Clique em New Request;
- Escolha o método entre: (`GET`, `POST`) e nomeie;
- Informe a `URL` e, caso seja necessário, vá em `Body` - `JSON`;
- Adicione `headers` como `Content-Type`: application/json se for necessário;
- Clique em `SEND` para enviar a requisição.

###

**<h2>🗃️ Resumo:</h2>**

###

Resumindo o tema, uma API, é uma **Programação de Aplicações**, (**Application Programming Interface**). Ela baseia-se em um grupo<br>
de regras que capacitam a interação entre softwares diferentes. É como se fosse um contrato que define a forma que um programa pode<br>
solicitar e receber funcionalidades de outro programa.

###

**<h2>⚙️ Como uma API funciona:</h2>**

###

- Um programa faz uma solicitação à API, especificando o que precisa;
- A API processa a solicitação, e retorna uma resposta com os dados solicitados;
- A interação entre os programas são feitas seguindo as regras e protocolos definidos na API. 

###

**<h2>🏆 Exemplos de uso:</h2>**

###

1️⃣- **Pagamentos online</h2>**

###

Uma loja online pode usar uma API de um gateway de pagamento para processar transações, sem a necessidade de precisar desenvolver<br>
todo o sistema de pagamento internamente. 

###

2️⃣- **Serviços meteorológicos</h2>**

###

A aplicação pode consumir a API de um serviço meteorológico para fornecer informações do tempo, em tempo real. 

###

**<h2>🖥️ Tipos de API:</h2>**

###

- API's internas;
- API's públicas;
- API's compostas;
- API's de parceiros.

###

**<h1>Muito obrigado pela visita! Bons estudos!👋</h1>**

###















