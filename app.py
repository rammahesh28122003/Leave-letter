from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    roll_no = request.form.get('roll-no')
    Year = request.form.get('Year')
    branch = request.form.get('branch')
    reason = request.form.get('reason')
    from_date=request.form.get('from_date')
    to_date=request.form.get('to_date')

    result= (f"i am {name}, {roll_no}, {Year}, {branch}, {reason}")

    return render_template('result.html', result=result,name=name,roll_no=roll_no,Year=Year,branch=branch,reason=reason,from_date=from_date,to_date=to_date)


if __name__ == '__main__':
    app.run(debug=True)
