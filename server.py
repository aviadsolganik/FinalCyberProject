from flask import Flask, render_template, request

from controller import Controller

app = Flask(__name__)

controller = Controller()


@app.route("/", methods=["GET", "POST"])
def home():
    try:
        return render_template("home.html")
    except Exception as e:
        print(e)


@app.route("/submit", methods=["GET", "POST"])
def submit():
    try:
        if not request.form.get('domain'):
            return render_template("home.html", s="please enter valid domain")
        domain = request.form["domain"]
        platform = request.form["platforms"]
        if not request.form.get('cache'):
            return render_template("home.html", s="please select if you want to use cache or not")
        cache = request.form["cache"]
        if cache == 'no':
            cache = False
        else:
            cache = True
        if platform == 'no':
            solution = controller.check_platform(domain, cache=cache)
        else:
            solution = controller.check_platform(domain, cache=cache, platform=platform)
        if solution is None:
            sol = domain + "\n" + 'could not detect platform' + "\n"
            return render_template("home.html", s=sol)
        elif 'could not detect platform' in solution:
            sol = domain + "\n" + str(solution) + "\n"
            return render_template("home.html", s=sol)
        else:
            domain = solution[0][1]
            platform = solution[0][2]
            version = solution[0][3]
            date = get_date(solution[0][4])
            sol = str(domain) + "\n" + str(platform) + "\n" + str(version) + "\n" + date
            return render_template("home.html", s=sol)
    except Exception as e:
        print(e)


def get_date(date):
    try:
        date = str(date).split(" ")
        date_t = date[0].split("-")
        year = date_t[0]
        month = date_t[1]
        day = date_t[2]
        last_check = "last checked at:" + year + "/" + month + "/" + day + "\n"
        return last_check
    except Exception as e:
        print(e)


if __name__ == "__main__":
    app.run(debug=True)