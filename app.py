from flask import Flask, render_template, request
import re

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        test_string = request.form['test_string']
        regex_pattern = request.form['regex_pattern']
        matches = find_matches(test_string, regex_pattern)
        return render_template('index.html', test_string=test_string, regex_pattern=regex_pattern, matches=matches)
    return render_template('index.html')

@app.route('/validate_email', methods=['POST'])
def validate_email():
    email = request.form['email']
    is_valid = validate_email_format(email)
    return render_template('index.html', email=email, is_valid=is_valid)

def find_matches(test_string, regex_pattern):
    try:
        regex = re.compile(regex_pattern)
        return regex.findall(test_string)
    except re.error:
        return []

def validate_email_format(email):
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None

if __name__ == '__main__':
    app.run(debug=True , host='0.0.0.0', port=5000)
