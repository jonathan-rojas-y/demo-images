from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def user_list():
    users = [
        {'name': 'Alice', 'email': 'alice@example.com'},
        {'name': 'Bob', 'email': 'bob@example.com'},
        {'name': 'Charlie', 'email': 'charlie@example.com'}
    ]
    return render_template('users.html', users=users)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=4000)