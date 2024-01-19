from pywebio import start_server
from pywebio.input import *
from pywebio.output import *
from pywebio.session import *
from pywebio.pin import *


def App():
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
    data = input_group(
        "العلامة بالرموز",
        [
            input(
                "العلامة",
                name="mark",
            ),
            input(
                "علامة الامتحان النصفي",
                name="med",
                type=NUMBER,
            ),
            input(
                "علامة اعمال الفصل",
                name="jobs",
                type=NUMBER,
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
    for i in range(marks1[x], marks1[x - 1]):
        f.insert(c, final)
        c += 1
        final += 1

    put_text("\n")
    put_text("علامة الامتحان النهائي هي :<<%r>>" % data["mark"])
    put_text("علامة الامتحان النصفي هي :%r" % data["med"])
    put_text("علامة اعمال الفصل هي  :%r" % data["jobs"])
    put_text(" العلامات المتوقعة للامتحان النهائي هي :  %r" % f)
    put_table(
        [
            ["العلامة بالرموز", data["mark"]],
            ["علامة الميد", data["med"]],
            ["علامة اعمال الفصل", data["jobs"]],
            ["العلامات المتوقعة للامتحان النهائي", f],
        ]
    )
    put_button("go back", onclick=lambda: run_js("location.reload()"))


start_server(App(), port=4567, debug=True)
