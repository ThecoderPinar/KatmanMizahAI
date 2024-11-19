from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Katman Just Hayal Projesine Hoş Geldiniz!"

if __name__ == '__main__':
    app.run(debug=True)
