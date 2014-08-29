import db
import devops
from flask import Flask, jsonify, abort, make_response, request
from datetime import datetime, timedelta

app = Flask(__name__)


@app.route('/api/hosts', methods=['GET'])
def get_hosts():
    hosts = db.get_hosts()
    if request.args.get('nocache', False):
        hosts_to_update = []
        now = datetime.now()
        for host in hosts:
            if now - host["cache_time"] > timedelta(minutes=1):
                hosts_to_update.append(host["host_name"])
        updated_hosts = devops.fetch_hosts_info(hosts_to_update)
        db.update_hosts(updated_hosts)

    return jsonify({"hosts": db.get_hosts()})


@app.route('/api/hosts/<int:host_id>', methods=['GET'])
def get_host(host_id):
    hosts = db.get_hosts()
    host = next((h for h in hosts if h['id'] == host_id), None)
    if not host:
        abort(404)

    if (request.args.get('nocache', False) and
       datetime.now() - host["cache_time"] > timedelta(minutes=1)):
        updated_hosts = devops.fetch_hosts_info([host["host_name"]])
        db.update_hosts(updated_hosts)
        host = next((h for h in db.get_hosts() if h['id'] == host_id), None)

    return jsonify({'host': host})


@app.route('/')
def index():
    return "<img src=\"static/ham.jpg\"></img>"



@app.errorhandler(404)
def not_found(_):
    return make_response(jsonify({'error': 'Unable to find resource'}), 404)


if __name__ == '__main__':
    app.run(debug=True)
