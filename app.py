from flask import (
    Flask,
    redirect,
    request,
    render_template)
from script import results

app = Flask(__name__)


@app.route('/')
def start():
    return render_template(template_name_or_list="index.html")


@app.route('/get-result', methods=['POST', 'GET'])
def get_result():
    if request.method == 'POST':
        res_form = results(form=request.form)
        return render_template(template_name_or_list="result.html", res_forearm=res_form['res_forearm'], res_shoulder=res_form['res_shoulder'], res_back=res_form['res_back'], res_hip=res_form['res_hip'], res_shin=res_form['res_shin'], res_foot=res_form['res_foot'])
    else:
        return redirect('/')


if __name__ == '__main__':
    app.run()
