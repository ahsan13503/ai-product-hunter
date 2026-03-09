printf '%s\n' \
"from flask import Flask" \
"app = Flask(__name__)" \
"" \
"@app.route('/')" \
"def home():" \
"    return '<h1>AI Product Hunter - Working!</h1>'" > app.py
