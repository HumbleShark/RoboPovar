import os

import requests
from flask import Flask, render_template, request  # import
import analyser as an
from recipe_getter import get_ingr_list

app = Flask(__name__)  # calling


@app.route("/", methods=['GET', 'POST'])  # initialising
def home():  # function call
    return render_template('home.html')  # return and calling HTML page (designed templates)


@app.route("/predict", methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        file = request.files['file']
        filename = file.filename
        file_path = os.path.join(r'static/', filename)  # slashes should be handeled properly
        file.save(file_path)
        product = an.img_analysis(file_path)

        if product:
            return render_template('predict.html', product=product, user_image=file_path,
                                   ingr=get_ingr_list(product).replace('\n', '<br>'))
        else:
            return render_template('predict.html', product='Cant detect', user_image=file_path,
                                   ingr='')
    else:
        return requests.codes.bad_request


if __name__ == "__main__":
    app.run()
