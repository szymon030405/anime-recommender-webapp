from flask import Flask, redirect, request, render_template, session

DATABASE = 'database.db'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.secret_key = "random_string_here"


@app.route('/Home', methods=['GET'])
def homepage():
	if request.method == 'GET':
		return render_template('main.html')


if __name__ == '__main__':
    app.run(debug=True) 