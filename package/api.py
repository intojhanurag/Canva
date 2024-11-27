from flask import Flask,jsonify,request


ap=Flask(__name__)

items=[
    {"id=1","name":"Item 1","description":"This is item 1"}
    {"id=2","name":"Item 2","description":"This is item 2"}
]

@app.rout('/')

def home():
    return "Welcome to the sample to do list app"
@app.rout('/items',methods=['GET'])
def get_items():
    return jsonify(items)

@app.route('/items/<int:item_id')
def get_item(item_id):
    item=next((for item in items if item["id"]==item_id),None)

    if item is None:
        return jsonify({"error":"items not found"})
    
    return jsonify(item)

@app.route('/items'.methods['POST'])
def create_item():
    if not request.json or not 'name' in request.json:
        return jsonify("error":"items not found")
    new_item={
        "id":items[-1]["id"]+1 if items else 1
        "name":request.json['name']
        "description":request.json["description"]
    }
    items.append(new_item)
    return jsonify(new_item)

@app.route('/items/<int:item_id>',methods=['PUT'])

def update_item(item_id):
    item=next((item for item in items if item["id"]==item_id),None)

    if item is None:
        return jsonify({"error":"Item not found"})
    item['name']=request.json.get('name',item['name'])
    item['description']=request.json.get('description',item['description'])

    return jsonify(item)

@app.route('/items/<int:item_id>',methods=['DELETE'])

def delete_item(item_id):
    global items
    items=next((item for item in items if item["id"]==item_id))

    item['name']=request.json.get('name',item['name'])
    item['description']=request.json.get('description',item['description'])

    return jsonify(item)

if __name__=='__main__':
    app.run(debug=True)