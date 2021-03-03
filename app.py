from flask import Flask, request, render_template, redirect, url_for, jsonify, abort, make_response

from models import collection
from forms import MovieForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'abc'

''' Wyświetlenie całej biblioteki filmów(GET)(self.all), oraz możliwość dodania nowej pozycji(POST)(self.create) i zapisania jej (self.save_col).'''

@app.route('/collections/', methods=['GET', 'POST'])
def collections():
    form = MovieForm()
    error = ""
    if request.method == "POST":
        if form.validate_on_submit():
            collection.create(form.data)
            collection.save_col()
        return redirect(url_for("collections"))
    return render_template("collections.html", error=error, form=form, collection=collection.all())


''' Wyświetlenie szczegółów filmu(GET)(self.get), oraz możliwość jego modyfikacji(POST)(self.update). '''

@app.route('/collections/<int:collection_id>/', methods=['GET', 'POST'])
def single_movie(collection_id):
    movie = collection.get(collection_id - 1)
    form = MovieForm(data=movie)

    if request.method == "POST":
        if form.validate_on_submit():
            collection.update(collection_id - 1, form.data)
        return redirect(url_for("collections"))
    return render_template("single.html", form=form, collection_id=collection_id)


'''-------------- CZĘŚĆ 2: API -------------'''

@app.route("/api/v1/collections/", methods=['GET'])
def api_collection():
    return jsonify(collection.all())

@app.route("/api/v1/collections/<int:collection_id>", methods=["GET"])
def get_movie(collection_id):
    movie = collection.get_api(collection_id)
    if not movie:
        abort(404)
    return jsonify({"movie": movie})

@app.route("/api/v1/collections/", methods=["POST"])
def create_movie():
    if not request.json or not 'title' in request.json:
        abort(400)
    movie = {
        'id': collection.all()[-1]['id'] + 1,
        'title': request.json['title'],
        'year': request.json['year'],
        'description': request.json.get('description', ""),
        'done': False
    }
    collection.create_api(movie)
    return jsonify({'movie': movie}), 201

@app.route("/api/v1/collections/<int:collection_id>", methods=['DELETE'])
def delete_movie(collection_id):
    result = collection.delete(collection_id)
    if not result:
        abort(404)
    return jsonify({'result': result})

@app.route("/api/v1/collections/<int:collection_id>", methods=["PUT"])
def update_movie(collection_id):
    movie = collection.get_api(collection_id)
    if not movie:
        abort(404)
    if not request.json:
        abort(400)
    data = request.json
    if any([
        'title' in data and not isinstance(data.get('title'), str),
        'description' in data and not isinstance(data.get('description'), str),
        'done' in data and not isinstance(data.get('done'), bool)
    ]):
        abort(400)
    movie = {
        'title': data.get('title', movie['title']),
        'description': data.get('description', movie['description']),
        'done': data.get('done', movie['done'])
    }
    collections.update_api(collection_id, movie)
    return jsonify({'changed': movie})

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found', 'status_code': 404}), 404)

@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({'error': 'Bad request', 'status_code': 400}), 400)




if __name__ == "__main__":
    app.run(debug=True)