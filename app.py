from flask import Flask,render_template,request,redirect,flash
from models import db,user
from datetime import datetime
import os


app=Flask(__name__)
 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///userdata.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db.init_app(app)
 
@app.before_first_request
def create_table():
    db.create_all()
 



@app.route('/login')
def login_form():
    return render_template('login.html')




@app.route('/',methods=["GET","POST"])
def registration_form():
    if request.method=="GET":
        return render_template('index.html')

    if request.method=="POST":
        print(request.form)
        print(request.files)
        username=request.form.get('username')
        email=request.form.get("email")
        password=request.form.get('password')
        birthday=request.form.get('birthday')
        profilepicture =request.files.get("filename")
        print("********************************************************************8")
        print(type(birthday))
        print(birthday)
        birthdayobject=datetime.strptime(birthday, '%Y-%m-%d')

        user_queryset=user(
            username=username,
            email=email,
            password=password,
            bday=birthdayobject
            
            ) 

        db.session.add(user_queryset)
        db.session.commit()pip -V



        profilepicturename=str(user_queryset.id)+".png"
        profilepicture.save(os.path.join("/home/apptrinity07/Flask/project/static/images/",profilepicturename))
        savedprofilepicture="/home/apptrinity07/Flask/project/static/images/"+str(profilepicturename)

        user_queryset.profilepicture=savedprofilepicture
        db.session.commit()

        return "Hi"

@app.route('/users/<int:id>')
def retriveuser(id):
    users=user.query.filter_by(id=id).first()
    if users:
        return render_template('details.html',user=users)
    return "user with {} No data info".format(id)


@app.route('/all_users')
def view_users():
    userslist=user.query.all()
    # for each_user in userlist:

    # print(each_user.username)
    print("******************************************")
    return  render_template('details.html',user=userslist)


@app.route('/update/<int:id>',methods=["GET","POST"])
def update(id):
    users=user.query.filter_by(id=id).first()
    if request.method=='POST':
         if users:
            username=request.form.get('username')
         
            # email=request.form.get("email")
            # password=request.form.get('password')
            # # birthday=request.form.get('birthday')
            # profilepicture =request.files.get("filename")
            #birthdayobject=datetime.strptime(birthday, '%Y-%m-%d')
           
            users.username=username
            #users.email=email
           
            # users.profilepicture=profilepicture
            db.session.commit()

            # profilepicturename=str(users.id)+".png"
            # profilepicture.save(os.path.join("/home/apptrinity07/Flask/project/static/images/",profilepicturename))
            # savedprofilepicture="/home/apptrinity07/Flask/project/static/images/"+str(profilepicturename)

            # users.profilepicture=savedprofilepicture
            # db.session.commit()

            return redirect('/users/'+str(id))
    return render_template('update.html',user=users)




             
           
             

@app.route('/user/<int:id>')
def view_one_user(id):
    userlist=user.query.filter_by(id=id).first()
    return  render_template('details.html',user=userlist)

@app.route('/prashanth',methods=["GET","POST"])
def prashanth():
    return "Hehehe"

if __name__=="__main__":
    app.run(debug=True,port=8000)
