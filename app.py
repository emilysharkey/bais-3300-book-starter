from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

all_books_dict = [
    {"Title": "The Hobbit", "Author": "J.R.R. Tolkien", "Pages": 295, 
     "Classification": "fiction", "Details": "read, recommend", "Acquisition": "library",},
]


@app.route("/", methods=["GET", "POST"])
def index():
    return render_template(
        "index.html", pageTitle="Add a book to my library", books=all_books_dict)


@app.route("/", methods=["POST"])
def homepage():
    print("inside add function")
    if request.method == "POST":

        form = request.form

        Title = form["Title"]
        Author = form["Author"]
        Pages = form["Pages"]
        Classification = form["Classification"]
        Details = form.getlist["Details"]
        Acquistion = form["Acquistion"] #this is a Python list 

        print(Title)
        print(Author)
        print(Pages)
        print(Classification)
        print (Details)
        print(Acquistion)


        details_string = ", ".join(Details)  # make the Python list into a string

        book_dict = {
            "Title": Title,
            "Author": Author,
            "Pages": Pages,
            "Classification": Classification,
            "Details": details_string,
            "Acqusition": Acquistion,
        }

        print(book_dict)
        all_books_dict.append(
            book_dict
        )  # append this dictionary entry to the larger friends dictionary
        print(all_books_dict)
        return redirect(url_for("index"))
    else:
        return redirect(url_for("index"))
    
@app.route("/", methods=["GET", "POST"])
def about():
    return render_template(
        "about.html", pageTitle="About Us", books=all_books_dict)


if __name__ == "__main__":
    app.run(debug=True)
