from flask import Flask, render_template
import random

app = Flask(__name__)

images = [
  "https://media.giphy.com/media/o0vwzuFwCGAFO/giphy.gif",
  "https://media.giphy.com/media/Yq1pe2v7nNlwA/giphy.gif",
  "https://media.giphy.com/media/3oEjHP8ELRNNlnlLGM/giphy.gif"
]

@app.route('/')
def index():
  url = random.choice(images)
  return render_template("index.html", url=url)

if __name__ == "__main__":
  app.run(host="0.0.0.0")
