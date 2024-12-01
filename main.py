from flask import Flask

app = Flask(__name__)

@app.route("/")
def main():
    return ("<!DOCTYPE html>"
            "<html>"
            "<head>"
            "<title>My portfolio</title>"
            "</head>"
            "<body>"
            "<h1>My Python Library Skills</h1>"
            "<ol>"
            "<li>datetime</li>"
            "<li>turtle</li>"
            "<li>tkinter</li>"
            "<li>smtplib</li>"
            "<li>Flask</li>"
            "<li>requests</li>"
            "</ol>"
            "<hr>"
            "<h1>My Projects - <a href='https://github.com/AtishayCoder'>GitHub</a></h1>"
            "</body>"
            "</html>")


if __name__ == "__main__":
    app.run(port=3000)
