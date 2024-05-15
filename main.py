from flask import Flask, render_template, request, jsonify
from db.create import createTables, createUser
from db.GetUsers import getAllusers, getSpecificUsers
from db.UserOperation import updateUserAccess

app= Flask(__name__)

@app.route('/',methods=["GET"])
def hello():
    return "hello"


@app.route('/createUser',methods = ['POST'])
def create_user():

    name =  request.form['name']
    password= request.form['password']
    email = request.form['email']
    address= request.form['address']
    phone = request.form['phone']
    pincode  = request.form['pincode']
    dbRes=createUser(name=name, Email=email, Address=address, Phone=phone,password=password,PinCode=pincode)
    if dbRes==True:  
        return jsonify({'success':200,"message":"Successfully created"})
    else:
       return jsonify({'success':400,"message":"unable to create User"}) 
        

@app.route('/getAllUsers', methods=['GET'])
def getAllUser():
    return getAllusers()

@app.route('/getSpecificUser', methods=['GET'])
def getSpecificUser():
    userID = request.form['userID']
    return getSpecificUsers(userId=str(userID))

@app.route('/updateUserAccess', methods=['PATCH'])
def updateUser_Access():
    userId= request.form['userID']
    approved= request.form['approved']
    blocked= request.form['blocked']
    updateUserAccess(id=userId, approved=approved, blocked=blocked)
    return "access updated successfully"


if __name__ == "__main__":
    createTables()
    app.run()


# @app.route('/home',methods= ['GET'])
# def home():
#    data = {'name': 'kundan','class':[1,2,3,4,5,6]}
#    return jsonify(data)

# def DB():
#     conn= sqlite3.connect("Store_Management.db")
#     cursor= conn.cursor()
#     cursor.execute(''' 
# CREATE TABLE User (
#          id INT AUTO_INCREMENT PRIMARY KEY,
#                    User_id VARCHAR(255),
#                    password VARCHAR(255),
#                    Level INT,
#                    DateOfAccountCreation DATE,
#                    Approved BOOLEAN,
#                    Block BOOLEAN,
#                    Name VARCHAR(255),
#                    Address VARCHAR(255),
#                    Email VARCHAR(255),
#                    Phone VARCHAR(255),
#                    PinCode VARCHAR(255)

# );

# ''')
    
#     conn.execute( """
                 
# INSERT INTO User (user_id,Password,Level,DateOfAccountCreation,Approved,Block,Name,Address,Email,Phone,PinCode)
# VALUES
# ('john_sina','pass123',1,'2024-04-04',TRUE,'John sina','123 MainSt','john@sina.com','1234567890','846009'),
# ('john_sina','pass123',1,'2024-04-04',TRUE,'John sina','123 MainSt','john@sina.com','1234567890','846009'),
# ('john_sina','pass123',1,'2024-04-04',TRUE,'John sina','123 MainSt','john@sina.com','1234567890','846009'),
# ('john_sina','pass123',1,'2024-04-04',TRUE,'John sina','123 MainSt','john@sina.com','1234567890','846009');

# """ )
    
#     conn.commit()
#     print(conn.execute("SELECT * FROM User"))
#     conn.close()

# @app.route("/test")
# def test():
#     return render_template("index.html")

 



# if __name__=="__main__":
#    createTables()
#    app.run()



  