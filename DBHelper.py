import mysql.connector as connector

   
class DBHelper():
    def __init__(self):
        self.con = connector.connect(host='localhost',
                                     port='3306',
                                     user='root',
                                     password='Saurav123@',
                                     database='pythonproject')
        query='create table if not exists user(userId int primary key,userName varchar(200),phone varchar(12))'
        cur=self.con.cursor()
        cur.execute(query)
        print("Created")
    #insert
    def insert_user(self,userId,userName,phone):
        query="insert into user(userId,userName,phone) values({},'{}','{}')".format(userId,userName,phone)
        #print(query)
        cur=self.con.cursor()
        cur.execute(query)
        self.con.commit()      # -> This line is to modify the dataset permanently
        print("user saved to db")
        print()

    #Fetch All
    def fetch_all(self):
        query="select * from user"
        cur=self.con.cursor()
        cur.execute(query)
        for row in cur:
            print("userId: ", row[0])
            print("userName: ", row[1])
            print("phone: ", row[2])
            print()
            print()

    #Delete User
    def delete_user(self,userId):
        query="delete from user where userId={}".format(userId)
        #print(query)
        c=self.con.cursor()
        c.execute(query)
        self.con.commit()  # -> This line is to modify the dataset permanently
        print("Deleted")
        print()
        print()

    #Update User
    def update_user(self,userId,newName,newphone):
        query="update user set userName='{}',phone='{}' where userId={}".format(newName,newphone,userId)
        #print(query)
        uu=self.con.cursor()
        uu.execute(query)
        self.con.commit()  
        print("Updated")
        print()
        print()
