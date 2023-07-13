from machinetranslation import translator
from flask import Flask, render_template, request
import json
import machinetranslation

app = Flask("Web Translator")

@app.route("/englishToFrench")
def english_to_french():
    #write the code here
    frenchtranslation = language_translator.translate(
        text=request.args.get('textToTranslate'),
        model_id='en-fr'
        ).get_result()

    return frenchtranslation.get("translations")[0].get("translation")

@app.route("/frenchToEnglish")
def french_to_english():
    #write the code here
    englishtranslation = language_translator.translate(
        text=request.args.get('textToTranslate'),
        model_id='fr-en'
        ).get_result()

    return englishtranslation.get("translations")[0].get("translation")

@app.route("/")
def renderIndexPage():
    # Write the code to render template
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)