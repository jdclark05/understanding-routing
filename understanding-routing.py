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

if __name__=="__main__":
    # Method that starts our flask server
    # We give it an argument to debug
    app.run(debug=True)



