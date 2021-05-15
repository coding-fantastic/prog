import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "personalityType"
)

mycursor = db.cursor()

def readDb(abrr):
    query = "SELECT * FROM `typeTbl`  "
    
    query2 = "SELECT typeTbl.typename ,typeTbl.typeabbr , careersTbl.careername, careersTbl.careerdef, careersTbl.schooloffering, careersTbl.coursename FROM typeTbl INNER JOIN careersTbl ON typeTbl.ttid = careersTbl.ttid WHERE typeTbl.typeabbr = '" + abrr+  "' "
    query3 = "SELECT typeTbl.typeabbr , careersAvoidTbl.careername FROM typeTbl INNER JOIN careersAvoidTbl ON typeTbl.ttid = careersAvoidTbl.ttid WHERE typeTbl.typeabbr = '" + abrr+  "' "
    
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
        
typeTblAndCareersTblList , careersToAvoidList = readDb("ISTJ")
print("schools offereing " + typeTblAndCareersTblList[3][5] + " are " + typeTblAndCareersTblList[3][4] )
print("schools offereing " + typeTblAndCareersTblList[0][5] + " are " + typeTblAndCareersTblList[0][4] )
# print("schools offering " + typeTblAndCareersTblList[0][6] + " are " + typeTblAndCareersTblList[0][5])

    
