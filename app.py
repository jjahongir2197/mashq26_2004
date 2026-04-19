@app.route("/grade18", methods=["GET", "POST"])
def grade18():

    if request.method == "POST":

        subject = request.form.get("subject")
        grade = request.form.get("grade")

        return render_template(
            "result18.html",
            subject=subject,
            grade=grade
        )

    return render_template("index18.html")
