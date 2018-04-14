from flask import Flask,render_template,request
import dataset
app=Flask(__name__)
db=dataset.connect("sqlite:///Felstia")
food=db["food"]
folkolre=db["folkolre"]
history=db["history"]
dresses=db["dresses"]

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
		tableName.insert(dict(subject=subject,title=title,link=link,photo_link=photo_link))
		return render_template("Adminform.html",tableName=tableName)
	else:
		return render_template("Adminform.html")


if __name__ == '__main__':
	app.run(port=8080)

