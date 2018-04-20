
from flask import Flask,render_template,request
import dataset
app=Flask(__name__)
db=dataset.connect("sqlite:///Felstia")
food=db["food"]
folkolre=db["folkolre"]
history=db["history"]
dresses=db["dresses"]
#{%endblock %}
#food.delete( title= "Dolma" )
#table.delete(place=)
#folkolre.drop()
@app.route("/")
def home_page():
	return render_template("index.html")

@app.route("/history")
def historypage():
	return render_template("history.html", history=history.all())

@app.route("/folkolre")
def folkolrePage():
	return render_template("folkolre.html",folkolre=folkolre.all())
@app.route("/food")
def food_cate():
	return render_template("food.html",food=food.all())


#tttt
@app.route("/Adminform", methods=["post","get"] )
def Adminform():
	tableName = ""

	if  (request.method =="POST"):
		section=request.form["section"]
		print(section)
		if(section == "food"):
			tableName = food
		elif(section == "folkolre"):
			tableName = folkolre
		elif(section == "history"):
			tableName = history
		elif(section == "dresses"):
			tableName = dresses

		subject=request.form["subject"]
		title=request.form["title"]
		link=request.form["link"]
		photo_link=request.form["photo_link"]

		#print subject , title , link

		AdminPassword=request.form["password"]
		if (AdminPassword== "123"):
			tableName.insert(dict(subject=subject,title=title,link=link,photo_link=photo_link))
			return render_template("Adminform.html",tableName=tableName)
		else:
			return render_template ("food.html", food=food.all())

	else:
		return render_template("Adminform.html")

if __name__ == '__main__':
		app.run(port=8075)