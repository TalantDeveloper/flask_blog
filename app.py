from flask import Flask, render_template

app = Flask(__name__)

posts = [
    {
        'author': 'Corey Schafer',
        'title': "Blog Post 1",
        'content': 'First post content',
        'date_posted': 'April 21, 2018',
    },
{
        'author': 'Botirjon Ergashov',
        'title': "Blog Post 2",
        'content': 'Second post content',
        'date_posted': 'April 22, 2018',
    }
]


@app.route('/home')
@app.route('/')
def hello_world():  # put application's code here
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html', title="About")


if __name__ == '__main__':
    app.run(debug=True)