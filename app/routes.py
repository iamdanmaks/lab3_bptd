from flask import jsonify
from flask import request
from flask import render_template

from app import app
from app import hashing
from app.collisions import create_collisions


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    return render_template(
        'index.html', 
        user_input='Nothing was entered', 
        user_hash='Nothing was entered'
    )


@app.route('/hash', methods=['POST'])
def hash_object():
    if request.method == 'POST':
        try:
            return jsonify({
                "hashed": str(hashing.check_sum(
                    request.json.get('text')
                ))
            })
        except AttributeError as e:
            return jsonify({
                "hashed": str(hashing.check_sum(
                    request.files.get('file').read()
                ))
            })


@app.route('/compare', methods=['POST'])
def compare_objects():
    if request.method == 'POST':
        obj1_hash = hashing.check_sum(
            request.files.get('first').read()
        )

        obj2_hash = hashing.check_sum(
            request.files.get('second').read()
        )
        
        return jsonify({
            "same": hashing.compare_instances(
                obj1_hash,
                obj2_hash
            ),
            "hash1": str(obj1_hash),
            "hash2": str(obj2_hash)
        })


@app.route('/generate_simple_collisions', methods=['POST'])
def generate_simple_collisions():
    if request.method == 'POST':
        print(request.json)
        result = create_collisions(request.json.get('iters_num'))
        col_num = sum([len(v) for k, v in result.items()])

        return jsonify({
            "results": result,
            "percent": int((col_num / request.json.get('iters_num')) * 100)
        })
