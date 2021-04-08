from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/dojo")
def dojo():
    return render_template("dojo.html")

@app.route('/say/<string:name>') 
def say(name):
    print(name)
    return "Hi " + name +"!"
    return render_template("say.html", name=name)

@app.route('/repeat/<int:num>/<string:word>') 
def repeat(num,word):
    newWord = ""
    for i in range(num): newWord += word + "<br/>"
    return newWord
    return render_template("repeat.html", word=newWord)

# @app.route("/say/flask")
# def say_flask():
#     return render_template("say_flask.html")

# @app.route("/say/michael")
# def say_michael():
#     return render_template("say_michael.html")

# @app.route("/say/john")
# def say_john():
#     return render_template("say_john.html")

# @app.route("/others")
# def others():
#     db_others = [
#         {"first_name":"Tom","last_name":"Tom","email":"ttom@python.com"},
#         {"first_name":"Dick","last_name":"Johnson","email":"djohnson@python.com"},
#         {"first_name":"Harry","last_name":"Balderdash","email":"hbalderdash@python.com"},
#         {"first_name":"Jerry","last_name":"Jones","email":"jjones@python.com"}
#     ]
#     return render_template("others.html", users=db_others)

# @app.route("/add/user")
# def add_user():
#     return render_template("add_user.html")

# @app.route("/create/user",methods=['POST'])
# def create_user():
#     print(request.form)
#     print(request.form['first_name'])
#     print(request.form['last_name'])
#     print(request.form['email'])

if __name__=="__main__":
    # Method that starts our flask server
    # We give it an argument to debug
    app.run(debug=True)



