from datetime import timedelta
from fabric.api import execute, env
from functools import update_wrapper
from flask import make_response, request, current_app, Flask, jsonify

app = Flask(__name__)

env.warn_only = True

package_name = 'scripts'


def crossdomain(origin=None, methods=None, headers=None,
                max_age=21600, attach_to_all=True,
                automatic_options=True):
    if methods is not None:
        methods = ', '.join(sorted(x.upper() for x in methods))
    if headers is not None and not isinstance(headers, basestring):
        headers = ', '.join(x.upper() for x in headers)
    if not isinstance(origin, basestring):
        origin = ', '.join(origin)
    if isinstance(max_age, timedelta):
        max_age = max_age.total_seconds()

    def get_methods():
        if methods is not None:
            return methods

        options_resp = current_app.make_default_options_response()
        return options_resp.headers['allow']

    def decorator(f):
        def wrapped_function(*args, **kwargs):
            if automatic_options and request.method == 'OPTIONS':
                resp = current_app.make_default_options_response()
            else:
                resp = make_response(f(*args, **kwargs))
            if not attach_to_all and request.method != 'OPTIONS':
                return resp

            h = resp.headers

            h['Access-Control-Allow-Origin'] = origin
            h['Access-Control-Allow-Methods'] = get_methods()
            h['Access-Control-Max-Age'] = str(max_age)
            if headers is not None:
                h['Access-Control-Allow-Headers'] = headers
            return resp

        f.provide_automatic_options = False
        return update_wrapper(wrapped_function, f)
    return decorator


@app.route('/run/<host>/<task>', methods=['GET'])
@crossdomain(origin='*')
def run_command(host, task):
    kwargs = {key: request.args.get(key) for key in request.args}
    func = getattr(__import__(package_name), task)
    results = execute(func, hosts=[host], **kwargs)
    return jsonify({'ok': True, 'results': results})


@app.errorhandler(404)
def not_found(_):
    return make_response(jsonify({'error': 'Unable to find resource'}), 404)

if __name__ == '__main__':
    app.run(debug=True)
