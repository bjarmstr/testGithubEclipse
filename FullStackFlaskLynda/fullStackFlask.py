'''
Created on Jan. 26, 2021

@author: bjarm
'''
'''
Created on Jan. 26, 2021
Full Stack Web Development with Flask
@author: bjarm
'''

from flask import Flask, render_template

app = Flask(__name__)

#"SECRET_KY = os.environ.get

def main():
    print("hello")

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

if __name__ == '__main__':  # Script executed directly?
    app.run(debug=True)  # Enable reloader and debugger



