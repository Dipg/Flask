from notion.client import NotionClient
from flask import Flask,jsonify,render_template, request, redirect, url_for

import json
app = Flask(__name__)




@app.route('/more')
def getProducs():
  client = NotionClient(token_v2="112f4d349b7fc9a2e1abbe9b8b7b61f8a7c51c32b38fb9852b50e9ef8ef866c17432e27604969625dc2ef0f545630bbb0ecd09f3fb9a9ca0fe8bfb1a6e8eb9703feffc7454b3544340ed9bbbc48c")
  cv = client.get_collection_view("https://www.notion.so/575896a3efa444ebbe5a3431f5b7c434?v=221eb059c40849329cf7972614906cc1")
  promis=[]
  promis2=[]
  for row in cv.collection.get_rows():
    pro=row.Name
    pro2=row.value
    promis.append(pro)
    promis2.append(pro2)
  print(promis)
  print(promis2)
  return render_template('index.html', promis=promis,promis2=promis2 )



@app.route('/mas')
def pasar():
    legend = 'Monthly Data'
    labels = ["January", "February", "March", "April", "May", "June", "July", "August"]
    values = [10, 9, 8, 7, 6, 4, 7, 8]
    return render_template('index.html', values=values, labels=labels, legend=legend)
  
  
 
@app.route('/w', methods=['GET','POST'])
def my_view_func(name):
  client = NotionClient(token_v2="112f4d349b7fc9a2e1abbe9b8b7b61f8a7c51c32b38fb9852b50e9ef8ef866c17432e27604969625dc2ef0f545630bbb0ecd09f3fb9a9ca0fe8bfb1a6e8eb9703feffc7454b3544340ed9bbbc48c")
  cv = client.get_collection_view("https://www.notion.so/575896a3efa444ebbe5a3431f5b7c434?v=221eb059c40849329cf7972614906cc1")
  promis=[]
  promis2=[]
  for row in cv.collection.get_rows():
    pro=row.Name
    pro2=row.value
    promis.append(pro)
    promis2.append(pro2)

  
  
  return render_template('index.html', promis=promis,promis2=promis2)

#'welcome %s' % name




@app.route('/success/<name>',methods = ['POST', 'GET'])
def success(name):
  if request.method == 'POST':
        user2 = request.form['valor']
        
  
        client = NotionClient(token_v2="112f4d349b7fc9a2e1abbe9b8b7b61f8a7c51c32b38fb9852b50e9ef8ef866c17432e27604969625dc2ef0f545630bbb0ecd09f3fb9a9ca0fe8bfb1a6e8eb9703feffc7454b3544340ed9bbbc48c")
        cv = client.get_collection_view(user2)
        promis=[]
        promis2=[]
        for row in cv.collection.get_rows():
          pro=row.Name
          pro2=row.value
          promis.append(pro)
          promis2.append(pro2)
        print(promis)
        print(promis2)
        return render_template('index.html', promis=promis,promis2=promis2,name2=user2 )
  return render_template('index.html')

 



@app.route('/login',methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        print(user)
        return redirect(url_for('success',name = user))
    else:
        return render_template('index2.html')
      
      

  
  
if __name__ == "__main__":
    app.run(debug=True)
    
