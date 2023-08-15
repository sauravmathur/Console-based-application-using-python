from DBHelper import DBHelper

def main():
    db=DBHelper()
    while True:
       print("***WELCOME***")
       print("Press 1 to Insert new User")
       print("Press 2 to Display all User")
       print("Press 3 to Delete User")
       print("Press 4 to Update User")
       print("Press 5 to exit program")
       print()
       try:
           choice=int(input())
           if(choice==1):
               #insert user
               uid=int(input("Enter User ID: "))
               username=input("Enter User Name: ")
               userphone=input("Enter User Phone No.: ")
               db.insert_user(uid,username,userphone)

           elif(choice==2):
               #Display user
               db.fetch_all()
               pass
           elif(choice==3):
               #Delete user
               userid=int(input("Enter User ID to delete that User: "))
               db.delete_user(userid)
               pass
           elif(choice==4):
               #Update user
               uid=int(input("Enter ID of user : "))
               username=input("New Name: ")
               userphone=input("New Phone No.: ")
               db.update_user(uid,username,userphone)
               pass
           elif(choice==5):
               break
           else:
               print("Invalid input ! Try Again")
       except Exception as e:
            print(e)
            print("Invalid Details ! Try Again")

if __name__ == "__main__":
    main()