from flask import Flask , render_template , request
import dataset
app = Flask(__name__)

db = dataset.connect("sqlite:///felstia")

@app.route("/")
def home():
	return render_template("index.html")









if __name__=="__main__":
      app.run(port=3455)

