from flask import Flask
from flask import render_template, jsonify
from flask import request
import bookDB

app = Flask(__name__)
db = bookDB.bookDB("mylib")


@app.route('/Books', methods=['POST', 'GET'])
def listAllbooks():
	if request.method == "GET":
		aux= db.listAllBooks()
		return jsonify([book.__dict__ for book in aux])
	else:
		aux = request.get_json()
		print(aux)
		db.addBook(aux['author'],aux['title'],aux['year'])
		return 'Livro adicionado'


@app.route('/Authors', methods=['GET'])
def listAllAuthors():
	aux = db.listAllBooks()
	return jsonify([author.__dict___ for author in aux])


@app.route("/Books/<id>")
def get_bookId(id):
	book=db.showBook(int(id))
	book_dic=book.__dict__
	return jsonify(book_dic)


if __name__ == '__main__':
	app.run()