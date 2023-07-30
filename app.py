from flask import Flask, render_template, request,jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def check_even_odd():
    number = int(request.form['number'])
    if(number < 0):
        return 'Just Cuddle Baby Pleae'
    elif(number == 0):
        return "you are getting those fingers tonight hard"
    elif(number < 10):
        return "I am going down on you tonight and lick you till your water comes"
    elif(number < 20 ):
        return "We are going to grt naked and sleep together doing foreplay and i will make you wet"
    elif(number < 50):
        return "So we are going to do soft sex and i will fuck you softly and give you little pain inserting in you "
    elif(number < 100):
        return "We are going to do different position like cowgirl and doggy style and i will go a little hard on you"
    else:
        return "I will go hard on you and fuck you till you scream and release your water and then you will take it in mouth"

if __name__ == '__main__':
    app.run(debug=True)
