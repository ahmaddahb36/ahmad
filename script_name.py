from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        mark = request.form['mark']
        med = request.form['med']
        jobs = request.form['jobs']
        chek = request.form['chek']

        marks = {
            "A+": 94,
            "A": 88,
            "A-": 84,
            "B+": 77,
            "B": 76,
            "B-": 70,
            "C+": 68,
            "C": 63,
            "C-": 60,
            "D+": 56,
            "D": 50,
            "F": 35,
        }
        marks1 = [94, 88, 84, 77, 76, 70, 68, 63, 60, 56, 50, 35]
        f = []
        final = marks[mark] - jobs - med
        x = marks1.index(marks[mark])
        c = 0
        if chek == "مدمج":
            for i in range(marks1[x], marks1[x - 1]):
                if final <= 40:
                    f.append(final)
                    c += 1
                    final += 1
        else:
            for i in range(marks1[x], marks1[x - 1]):
                if final <= 50:
                    f.append(final)
                    c += 1
                    final += 1

        return render_template('index.html', mark=mark, med=med, jobs=jobs, chek=chek, f=f)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)