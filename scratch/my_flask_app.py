from flask import Flask, url_for, render_template, request, make_response, abort, redirect
from markupsafe import escape, Markup

app = Flask(__name__)


@app.route('/')
def index():
    return redirect(url_for('login'))


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)


@app.route('/login/', methods=['GET', 'POST'])
def login():
    try:
        print(request.form['username'])
    except Exception as e:
        print(f"Error: {e}")

    for cookie in request.cookies:
        print(cookie)

    response = make_response(render_template('hello.html', name=None))
    response.set_cookie('test', '123', httponly=True)
    return response


@app.route('/user/<username>', methods=['GET', 'POST'])
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % escape(username)


@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id


@app.route('/account/<uuid:acc_id>', methods=['GET', 'PUT', 'DELETE'])
def get_account(acc_id):
    print(f'method = {request.method}')
    return 'Account %s' % acc_id


@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return 'Subpath %s' % escape(subpath)


with app.test_request_context():

    print('test request')

    print(url_for('get_account', acc_id='f6d69500-d41c-4bab-9fa1-52afc95befd8'))
#     print(url_for('index'))
#     # print(url_for('login'))
#     print(url_for('show_user_profile', username='bob'))
#     # print(url_for('profile', username='John Doe'))


# with app.test_request_context('/hello/', method='GET'):
#
#     print('test request /hello')
#
#     # now you can do something with the request until the
#     # end of the with block, such as basic assertions:
#     assert request.path == '/hello/'
#     assert request.method == 'GET'


if __name__ == "__main__":

    # markup
    print(str(Markup('<strong>Hello %s!</strong>') % '<blink>hacker</blink>'))
    print(str(Markup('<em>Marked up</em> &raquo; HTML').striptags()))

    # app.run(host='0.0.0.0')
    app.run(debug=True)
