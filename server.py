from notion.client import NotionClient
from flask import Flask,jsonify,render_template,request


app = Flask(__name__)





@app.route('/')
def abrir():

  
  return "hello"









if __name__ == "__main__":
    app.run(debug=True)