from flask import (
    Flask,
    redirect,
    url_for,
    render_template_string,
    request,
    render_template)
import jinja2
from script import results

app = Flask(__name__)


# env = jinja2.Environment()
# template = env.from_string(source="/templates/index.html")


@app.route('/')
def start():
    return render_template(template_name_or_list="index.html")


@app.route('/get-result', methods=['POST', 'GET'])
def get_result():
    if request.method == 'POST':
        # try:
        res_form = results(form=request.form)
        return render_template(template_name_or_list="result.html", res_forearm=res_form['res_forearm'], res_shoulder=res_form['res_shoulder'], res_back=res_form['res_back'], res_hip=res_form['res_hip'], res_shin=res_form['res_shin'], res_foot=res_form['res_foot'])
        # except:
        #     print("ХУЕТА")
        #     return redirect('/')
    else:
        return redirect('/')


if __name__ == '__main__':
    app.run()
