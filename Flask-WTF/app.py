from flask import Flask, render_template, request,session,flash
from flask_wtf import FlaskForm
from wtforms import TextField, SubmitField, BooleanField, RadioField, SelectField, TextAreaField
from wtforms.validators import DataRequired
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mykey'
Bootstrap(app)

class MyForm(FlaskForm):
    name = TextField("Put Your Name : ",validators=[DataRequired()])
    isAccept = BooleanField("Accept Condition!")
    gender = RadioField('Gender',choices=[('male','ชาย'),('female','หญิง'),('other','อื่นๆ')])
    skill = SelectField('Talent',choices=[('Eng','Eng'),('japan','japan'),('thai','thai'),('other','other')])
    address = TextAreaField("address")
    submit = SubmitField("Save")

# @app.route('/',methods=['GET','POST'])
# def index():
#     name=False
#     isAccept = False
#     gender = False
#     skill = False
#     address = ""
#     form=MyForm()
#     if form.validate_on_submit():
#         name = form.name.data
#         isAccept = form.isAccept.data
#         gender = form.gender.data
#         skill = form.skill.data
#         address = form.address.data
#         # Clear Data
#         form.name.data = ""
#         form.isAccept.data = ""
#         form.gender.data = ""
#         form.skill.data = ""
#         form.address.data = ""
#     return render_template("index.html",form=form,name=name,isAccept=isAccept,gender=gender,skill=skill,address=address)

@app.route('/',methods=['GET','POST'])
def index():
    form=MyForm()
    if form.validate_on_submit():
        flash("บันทึกข้อมูลเรียบร้อย")
        session['name'] = form.name.data
        session['isAccept'] = form.isAccept.data
        session['gender'] = form.gender.data
        session['skill'] = form.skill.data
        session['address'] = form.address.data
        # clear data
        form.name.data = ""
        form.isAccept.data = ""
        form.gender.data = ""
        form.skill.data = ""
        form.address.data = ""
    return render_template("index.html",form=form)

if __name__ == '__main__':
    app.run(debug=True)