#!flask/bin/python
from flask import Flask, request, jsonify
import uuid
import rocksdb
import sys
import StringIO
import contextlib

app = Flask(__name__)

@app.route('/api/v1/scripts', methods=['POST'])
def upload_files():
    db = rocksdb.DB("assign.db", rocksdb.Options(create_if_missing=True))
    f = request.files['data']
    key = uuid.uuid4().hex
    db.put(key.encode('utf-8') , f.stream.readline().encode('utf-8'))
    return jsonify({'script-id': key })

@contextlib.contextmanager
def stdoutIO(stdout=None):
    old = sys.stdout
    if stdout is None:
        stdout = StringIO.StringIO()
    sys.stdout = stdout
    yield stdout
    sys.stdout = old


@app.route('/api/v1/scripts/<scriptid>', methods=['GET'])
def get_task(scriptid):
    db = rocksdb.DB("assign.db", rocksdb.Options(create_if_missing=True))
    key = scriptid
    with stdoutIO() as x:
         exec db.get(key.encode('utf-8'))
    return x.getvalue()

if __name__ == '__main__':
    app.run(host='localhost',port='8000') 
