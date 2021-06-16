import mysql.connector
from numpy.lib.function_base import insert

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "personalityType"
)

mycursor = db.cursor()

def readDb(abrr, num):
    if num == 2:
        query = "SELECT amid, answer, questionNumber FROM `answersMissed` "
        mycursor.execute(query  )
        data = mycursor.fetchall()
        return data
        # answersMissedList = []
        
        # for row in mycursor:
        #     answersMissedList.append(row)
        
        # return answersMissedList

        # number 3 reads feedback table
    if num == 3:
        query = "SELECT feedbackid,name, comments FROM `feedback`"
        mycursor.execute(query  )
        data = mycursor.fetchall()
        return data
    query = "SELECT * FROM `typeTbl`  "
    
    query2 = "SELECT typeTbl.typename ,typeTbl.typeabbr , careersTbl.careername, careersTbl.careerdef, careersTbl.schooloffering, careersTbl.coursename FROM typeTbl INNER JOIN careersTbl ON typeTbl.ttid = careersTbl.ttid WHERE typeTbl.typeabbr = '" + abrr+  "' "
    query3 = "SELECT typeTbl.typeabbr , careersAvoidTbl.careername , careersAvoidTbl.reason FROM typeTbl INNER JOIN careersAvoidTbl ON typeTbl.ttid = careersAvoidTbl.ttid WHERE typeTbl.typeabbr = '" + abrr+  "' "
    
    mycursor.execute(query2  )
    typeTblAndCareersTblList = []
    # mycursor.execute(query3)
    for row in mycursor:
        # print(row)
        typeTblAndCareersTblList.append(row)
    
    mycursor.execute( query3 )
    careersToAvoidList = []
    # mycursor.execute(query3)
    for row in mycursor:
        # print(row)
        careersToAvoidList.append(row)


    # print("\nthis is the list : schools offering this \n" + str(mylist[0][4]))
    # return mylist[0][0],mylist[0][1],mylist[0][2],mylist[0][3],mylist[0][4],mylist[0][5],
    return typeTblAndCareersTblList , careersToAvoidList
        
# typeTblAndCareersTblList , careersToAvoidList = readDb("ISTJ")
# print("schools offereing " + typeTblAndCareersTblList[3][5] + " are " + typeTblAndCareersTblList[3][4] )
# print("schools offereing " + typeTblAndCareersTblList[0][5] + " are " + typeTblAndCareersTblList[0][4] )
# print("schools offering " + typeTblAndCareersTblList[0][6] + " are " + typeTblAndCareersTblList[0][5])

    
# check if user exist in a database 
def checkUser(email, passwd):
    sql = "SELECT * FROM `admin` WHERE email = '" + email + "' AND passwd = '" + passwd + "'"
    mycursor.execute( sql )

    # fetchone returns a tuple
    msg = mycursor.fetchone()
    if not msg :
        print("user not found" )
        print (msg)
        return "user not found" , msg
    else:
        print("user  found"  )
        print (msg[1])
        return "user found" ,msg[1]


def insertAdmin(username, email, passwd):
    sql = "SELECT email FROM `admin` WHERE email = '" + email + "'"
    mycursor.execute( sql )
    
    # fetchone returns a tuple
    msg = mycursor.fetchone()
    msglist = []
    msglist.append(msg)  
    print("this is message list " + str(msglist))
    
    if "None" not in msglist :
        print("user has been found. Don't insert" )
        print (msglist)
    else:
        print("user has not been found , you can insert")
        print(msglist)

    # sql = "INSERT INTO `admin` (`adminid`, `username`, `email`, `passwd`, `datentime`) VALUES (NULL, 'Mary', 'mary@yahoo.com', '5f4dcc3b5aa765d61d8327deb882cf99', current_timestamp()) "


def newAns(answer , queryNumber):
    sql = "INSERT INTO `answersMissed` (`amid`, `answer`, `questionNumber`,`datentime`) VALUES (NULL, '"+answer+"', '"+str(queryNumber)+"', current_timestamp()) "
    print (sql)
    mycursor.execute( sql )
    db.commit()


def insertComment(name, comment):
    # sql = "INSERT INTO `feedback` (`feedbackid`, `name`, `comments`,`datentime`) VALUES (NULL, '"+name+"', '"+str(comment)+"', current_timestamp()) "
    sql = "INSERT INTO `feedback` (`feedbackid`, `name`, `comments`, `datentime`) VALUES (NULL, '"+name+"', '"+str(comment)+"', current_timestamp())" 

    # print (sql)
    
    mycursor.execute( sql )
    db.commit()


def insertLoginLog(username):
    sql = "INSERT INTO `loginlog` (`loginlogid`, `username`, `datentime`) VALUES (NULL, '"+username+"', current_timestamp())"

    #print (sql)
    
    mycursor.execute( sql )
    db.commit()


# insertFeedback("Kelly", "test feeback 2 ")
# insertAdmin("Mary" , "mary@yahoo.com" , "5f4dcc3b5aa765d61d8327deb882cf99")
# abrr = "a"
# a = readDb(abrr, 3) 
# print (a[1][1])
# insertLoginLog('mark')