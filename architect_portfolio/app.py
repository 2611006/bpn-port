from flask import Flask, render_template, request, redirect, url_for
if __name__ == "__main__":
    app.run(debug=True)

app = Flask(__name__)

projects = [
    {
        "title": "Residential Apartment Block",
        "category": "Civil",
        "desc": "RCC structural design for multi-storey flats",
        "image": "flat1.jpg"
    },
    {
        "title": "G+5 Residential Flats",
        "category": "Architecture",
        "desc": "Planning and elevation for apartment building",
        "image": "flat2.jpg"
    },
    {
        "title": "Urban Housing Project",
        "category": "Civil",
        "desc": "Structural layout and site execution",
        "image": "flat3.jpg"
    },
    {
        "title": "2BHK Flat Interior",
        "category": "Interior",
        "desc": "Functional interior layout for residential flat",
        "image": "flat4.jpg"
    }
]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/projects")
def project_page():
    return render_template("projects.html", projects=projects)

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        message = request.form["message"]
        print(name, email, message)
        return redirect(url_for("home"))
    return render_template("contact.html")

# IMPORTANT for Vercel
app = app
