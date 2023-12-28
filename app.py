from flask import Flask,render_template,request
import mysql.connector

conn=mysql.connector.connect(host='localhost',user='root',password='root',database='taskmanagementsystem')
mycursor=conn.cursor()
#create the flask application
app = Flask(__name__)

@app.route('/') #home page
def hello():
    #return "Hello World!!!"

    # Call our html Page

    return render_template('index.html')

#create a dictionary for login
user_dict={'admin':'1234','sruthy':'abcd'}
@app.route('/login')

def login():

    return render_template('login.html')

@app.route('/newaccount')
def newaccount():

    return render_template('newaccount.html')

@app.route('/new_user', methods=['POST'])
def new_user():
    user=request.form['username']
    pw=request.form['password']
    user_dict[user]=pw
    print("DONE!!")
    return render_template('login.html')

@app.route('/home', methods=['POST'])
def emp_home():

    username=request.form['username']

    pwd=request.form['password']

    if username not in user_dict:

        return render_template('login.html', msg='Invalid Username')

    elif user_dict[username]!=pwd:

        return render_template('login.html', msg='Invalid Password')

    else:
               
        return render_template('home.html',user=username)
    
@app.route('/create')
def create():
    return render_template('create.html')

@app.route('/addtask',methods=['POST'])
def addtask():
    taskid=request.form.get('task_id')
    taskname=request.form.get('task_name')
    taskdescription=request.form.get('task_description')
    taskduedate=request.form.get('task_duedate')
    taskstatus=request.form.get('task_status')
    query="INSERT INTO tasks VALUES (%s,%s,%s,%s,%s)"
    data=(taskid,taskname,taskdescription,taskduedate,taskstatus)
    mycursor.execute(query,data)
    conn.commit()
    return render_template('create.html')

@app.route('/view')
def view():    
    query="SELECT * FROM tasks"
    mycursor.execute(query)
    data=mycursor.fetchall()
    return render_template('view.html',sqldata=data)
    
@app.route('/viewtodo')
def viewtodo():
    query="SELECT * FROM tasks WHERE TASK_STATUS = 'TO DO'"
    mycursor.execute(query)
    data=mycursor.fetchall()
    return render_template('view.html',sqldata=data)

@app.route('/viewinprogress')
def viewinprogress():
    query="SELECT * FROM tasks WHERE TASK_STATUS = 'IN PROGRESS'"
    mycursor.execute(query)
    data=mycursor.fetchall()
    return render_template('view.html',sqldata=data)

@app.route('/viewcompleted')
def viewcompleted():
    query="SELECT * FROM tasks WHERE TASK_STATUS = 'COMPLETED'"
    mycursor.execute(query)
    data=mycursor.fetchall()
    return render_template('view.html',sqldata=data)

@app.route('/back')
def back():

    return render_template('home.html')
@app.route('/backhome')
def backhome():

    return render_template('login.html')

@app.route('/backtohome')
def backtohome():

    return render_template('home.html')

@app.route('/backtomain')
def backtomain():

    return render_template('index.html')


@app.route('/update')
def update():


    return render_template('update.html')

@app.route('/updatetask',methods=['POST'])
def updatetask():
    taskid=request.form.get('task_id')
    taskstatus=request.form.get('task_status')
    query="UPDATE tasks SET TASK_STATUS=%s WHERE TASKID =%s"
    data=(taskstatus,taskid)
    mycursor.execute(query,data)
    conn.commit()
    return render_template('view.html')

@app.route('/delete')
def delete():
    
    return render_template('delete.html')

@app.route('/deletetask',methods=['POST'])
def deletetask():
    taskid=request.form.get('task_id')
    query="DELETE FROM tasks WHERE TASKID =(%s)"
    data=[(taskid)]
    mycursor.execute(query,data)
    conn.commit()
    return render_template('view.html')


#run flask application
if __name__=='__main__':
    app.run(debug=True)