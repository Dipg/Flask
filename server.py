from notion.client import NotionClient
from flask import Flask,jsonify,render_template, request, redirect, url_for

import json
app = Flask(__name__)




# @app.route('/products')
# def modify():
#     client = NotionClient(token_v2="112f4d349b7fc9a2e1abbe9b8b7b61f8a7c51c32b38fb9852b50e9ef8ef866c17432e27604969625dc2ef0f545630bbb0ecd09f3fb9a9ca0fe8bfb1a6e8eb9703feffc7454b3544340ed9bbbc48c")
#     cv = client.get_collection_view("https://www.notion.so/6079372bb1af43d7abb8f0f7ebb2fc80?v=6a7008cc54b044a0a43942e53acf5cce")
#     promis=[]
#     global products
#     products= promis
#     for row in cv.collection.get_rows():
#       pro={"URL":row.url,"Name":row.Name}
#       promis.append(pro)
#     # @app.route('/products3/products')
#     # def otenerProducs():
#     #   return jsonify({"products":products})

  
#     return #jsonify({"products":products})
# modify()
  
# print("value of x",products) 



# @app.route('/products')
# def otenerProducs():
#   return jsonify({"products":products})

########################################################################################## 


# @app.route('/products/<string:product_name>')
# def getProduct(product_name):
#   client = NotionClient(token_v2="112f4d349b7fc9a2e1abbe9b8b7b61f8a7c51c32b38fb9852b50e9ef8ef866c17432e27604969625dc2ef0f545630bbb0ecd09f3fb9a9ca0fe8bfb1a6e8eb9703feffc7454b3544340ed9bbbc48c")
#   cv = client.get_collection_view("https://www.notion.so/6079372bb1af43d7abb8f0f7ebb2fc80?v=6a7008cc54b044a0a43942e53acf5cce")
#   mad=[]
#   for row in cv.collection.get_rows():
#     print(row.Name)
  
#     if row.Name==product_name:
#         client2 = NotionClient(token_v2="112f4d349b7fc9a2e1abbe9b8b7b61f8a7c51c32b38fb9852b50e9ef8ef866c17432e27604969625dc2ef0f545630bbb0ecd09f3fb9a9ca0fe8bfb1a6e8eb9703feffc7454b3544340ed9bbbc48c")
#         print(row.url)
#         cv2 = client2.get_collection_view(row.url)
#         print(row.url)
#         promis=[]
#         promis2=[]
#         for row in cv2.collection.get_rows():
#           pro=row.Name
#           pro2=row.value
#           promis.append(pro)
#           promis2.append(pro2)

#         return render_template('index.html', promis=promis,promis2=promis2 )
#     else:
#       return render_template('index.html')
#   mad.append(row.Name)
#   print(mad)
      
  
    
    
    
    
    
@app.route('/products/<string:product_name>')
def getProduct(product_name):
  client = NotionClient(token_v2="112f4d349b7fc9a2e1abbe9b8b7b61f8a7c51c32b38fb9852b50e9ef8ef866c17432e27604969625dc2ef0f545630bbb0ecd09f3fb9a9ca0fe8bfb1a6e8eb9703feffc7454b3544340ed9bbbc48c")
  cv = client.get_collection_view("https://www.notion.so/6079372bb1af43d7abb8f0f7ebb2fc80?v=6a7008cc54b044a0a43942e53acf5cce")
  mad=[]
  for row in cv.collection.get_rows():
    print(row.Name)
  
    if row.Name==product_name:
        client2 = NotionClient(token_v2="112f4d349b7fc9a2e1abbe9b8b7b61f8a7c51c32b38fb9852b50e9ef8ef866c17432e27604969625dc2ef0f545630bbb0ecd09f3fb9a9ca0fe8bfb1a6e8eb9703feffc7454b3544340ed9bbbc48c")
        print(row.url)
        cv2 = client2.get_collection_view(row.url)
        print(row.url)
        promis=[]
        promis2=[]
        for row in cv2.collection.get_rows():
          pro=row.Name
          pro2=row.value
          promis.append(pro)
          promis2.append(pro2)
        return render_template('index.html', promis=promis,promis2=promis2 )
        # return 'hello'
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
      # pro={"URL":row.url,"Name":row.Name}
      # promis.append(pro)
#   productsFound = [product for product in products if product['Name']==product_name]
#   print(product_name)
#   return jsonify({"product":productsFound[0]})
  




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
    
        client = NotionClient(token_v2="112f4d349b7fc9a2e1abbe9b8b7b61f8a7c51c32b38fb9852b50e9ef8ef866c17432e27604969625dc2ef0f545630bbb0ecd09f3fb9a9ca0fe8bfb1a6e8eb9703feffc7454b3544340ed9bbbc48c")
      
        cv = client.get_collection_view(name)
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
        user2 = request.form['valor']
        print(user)
        return redirect(url_for('success',name = user2))
    else:
        return render_template('index2.html')
      
      

  
  
if __name__ == "__main__":
    app.run(debug=True)
    
