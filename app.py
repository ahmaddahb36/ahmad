from pywebio.platform.flask import webio_view
from pywebio import STATIC_PATH
from flask import Flask, send_from_directory
from pywebio.input import *
from pywebio.output import *
import argparse
from pywebio import start_server

import pickle
import numpy as np
model = pickle.load(open('regression_rf.pkl', 'rb'))
app = Flask(__name__)


def predict():
    def chek_mark(data):
        marks = ["A+", "A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D+", "D", "F"]
        for i in range(12):
            if data["mark"] not in marks:
                return ("mark", "يرجى ادخال الرمز بالانجليزية وكبير ")

    def checkMed(data):
        if data["med"] > 30 or data["med"] < 0:
            return ("med", "تأكد من العلامة المدخلة")

    popup(
        "موقع لحساب علامة الامتحان النهائي",
        put_text("اهلا بكم").onclick(lambda: toast("welcome")),
    )
    put_html(
        '<center><h3>حساب علامة الامتحان النهائي</h3><img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQqqp6Ets9gGG59SYbQqA4lhx6QNwzERnjj7A&usqp=CAU" width=200></center>'
    )
    put_html("<marquee>---------  حساب علامة الامتحان النهائي   --------</marquee>")
    data = input_group(
        "ادخل البيانات التالية ",
        [
            input(
                " العلامة بالرمــوز",
                name="mark",
                required=True,
            ),
            input(
                "علامة الامتحان النصفي",
                name="med",
                type=NUMBER,
                required=True,
            ),
            input(
                "علامة اعمال الفصل",
                name="jobs",
                type=NUMBER,
                required=True,
            ),
            radio(
                "طبيعة المادة",
                name="chek",
                options=["واجهي", "مدمج"],
                required=True,
                inline=True,
                help_text="اذا كانت علامة اعمال الفصل من 20 ادخل وجاهي اما اذا كانت من 30ادخل مدمج",
            ),
        ],
        validate=chek_mark,
    )
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
    final = marks[data["mark"]] - data["jobs"] - data["med"]
    x = marks1.index(marks[data["mark"]])
    c = 0
    if data["chek"] == "مدمج":
        for i in range(marks1[x], marks1[x - 1]):
            if final <= 40:
                f.insert(c, final)
                c += 1
                final += 1
    else:
        for i in range(marks1[x], marks1[x - 1]):
            if final <= 50:
                f.insert(c, final)
                c += 1
                final += 1
    put_text("\n")
    put_table(
        [
            [data["mark"], "العلامة بالرموز"],
            [data["med"], "علامة الميد"],
            [data["jobs"], "علامة اعمال الفصل"],
            [data["chek"], "طبيعة المادة"],
            [f, "العلامات المتوقعة للامتحان النهائي"],
        ],
    )
    put_button("go back", onclick=lambda: run_js("location.reload()"))

app.add_url_rule('/tool', 'webio_view', webio_view(predict),
            methods=['GET', 'POST', 'OPTIONS'])


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--port", type=int, default=8080)
    args = parser.parse_args()

    start_server(predict, port=args.port)
#if __name__ == '__main__':
    #predict()

#app.run(host='localhost', port=80)

#visit http://localhost/tool to open the PyWebIO application.
