from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    """Renders the home page with link to Fortune page."""
    return render_template('index.html')

@app.route('/fortune')
def fortune_form():
    """Renders the Allergy information form"""
    return render_template('fortune_form.html')

@app.route('/fortune_results')
def fortune_results():
    """Displays the user's fortune."""
   
    allergy = request.args.get('allergylist')
    print(allergy)
    if allergy == 'trees':
        fortune = "You will be good if you don't bother to go in the woods!"
        print(allergy)
    elif allergy == 'nuts':
        fortune = "You will think PB&J is disgusting!"
        print(allergy)
    elif allergy == 'dairy':
        fortune = "Your bone strength might decline"
        print(fortune)
    elif allergy == 'fish':
        fortune = "Your eyes might fail you"
        print(fortune)
    elif allergy == 'soy':
        fortune = "Menopause might be hard for you"
        print(fortune)
    elif allergy == 'eggs':
        fortune = "Your body may be missing important vitamins and minerals. Make up for them!"
        print(fortune)
    elif allergy == 'wheat':
        fortune = "You might have a hard time on the toilet seat"
        print(fortune)
    else:
        fortune = "Couldn't get a fortune, but hopefully you aren't bummed!"
    return fortune

def get_fortune():
    for fortune in "allergylist":
        results= []
        result = fortune
        results.append(result)
        print ("firstname")
        print (fortune_results)
        print (get_fortune(fortune))

    return render_template ('fortune_results.html', fortune=fortune)


if __name__ == "__main__":
    app.run(debug=True)