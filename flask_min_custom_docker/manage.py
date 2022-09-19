from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')



"""
- Build image

`docker image build -t flask_gunicorn_docker .`

- Run the container

`docker run -p 8080:8080 flask_gunicorn_docker`

or

`docker run -p 8080:8080 flask_gunicorn_docker`

"""