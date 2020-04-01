from api.python_test.total import Total
from flask import Flask, request, jsonify


app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.config["DEBUG"] = True


@app.route('/v1.1.0/total', methods = ['POST'])
def sum_of_develop():
    total_dict = request.get_json(force = True)
    return jsonify(Total(total_dict).sum())

@app.route('/v1.0.0/total', methods = ['POST'])
def sum_of_production():
    total_dict = request.get_json(force = True)
    return jsonify(Total(total_dict).sum())


if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 5000)
