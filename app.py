from flask import Flask, render_template, request
import xmlrpc.client

app = Flask(__name__)

proxy = xmlrpc.client.ServerProxy("http://localhost:8000/")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check', methods=['POST'])
def check():
    book_id = request.form['book']
    result = proxy.check_book(book_id)
    return render_template('index.html', result=result)

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
