from flask import Flask, render_template, request
import unicodedata
import requests

app = Flask(__name__)

def get_unicode_info(char):
    try:
        name = unicodedata.name(char)
        code_point = f"U+{ord(char):04X}"
        return name, code_point
    except ValueError:
        return "Unknown Character", ""

def get_word_meaning(word):
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        try:
            definition = data[0]['meanings'][0]['definitions'][0]['definition']
            return definition
        except (KeyError, IndexError):
            return "No definition found."
    else:
        return "Word not found."

@app.route('/', methods=['GET', 'POST'])
def home():
    result = {}
    if request.method == 'POST':
        search_input = request.form.get('search')
        if search_input:
            if len(search_input) == 1:
                name, code = get_unicode_info(search_input)
                result = {
                    "type": "character",
                    "input": search_input,
                    "name": name,
                    "code_point": code
                }
            else:
                meaning = get_word_meaning(search_input)
                result = {
                    "type": "word",
                    "input": search_input,
                    "meaning": meaning
                }
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
