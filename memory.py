import sqlite3
from internet import checkInternet

def create_connection():
    connection = sqlite3.connect('memory.db')
    return connection

def get_questionsAndanswers():
    con = create_connection()
    cur = con.cursor() #cursor is used to execute a query
    cur.execute("SELECT * FROM QuestionsAndAnswers")

    return cur.fetchall() #To fetch all the data from the database

def get_AnsFromMemory(question):
    rows = get_questionsAndanswers()
    answer = ""
    for row in rows:
        if row[0] in question:
            answer = row[1]
            break
    return answer

# print(get_AnsFromMemory("What is time"))

def insert_QuesAndAns(question, answer):
     con = create_connection()
     cur = con.cursor()
     query = "INSERT INTO QuestionsAndAnswers values('"+question+"','"+answer+"')"
     cur.execute(query)
     con.commit()

def get_name():
     con = create_connection()
     cur = con.cursor()
     query = "Select Value from Memory where Name = 'Assistant_Name'"
     cur.execute(query)
     return cur.fetchall()[0][0]

# print(get_name())

def update_name(new_name):
     con = create_connection()
     cur = con.cursor()
     query = "update Memory set Value = '"+new_name+"' where Name = 'Assistant_Name'"
     cur.execute(query)
     con.commit()
# update_name("Alexa")

def update_last_seen(Last_seen):
     con = create_connection()
     cur = con.cursor()
     query = "update Memory set Value = '"+str(Last_seen)+"' where Name = 'last_seen'"
     cur.execute(query)
     con.commit()
# update_last_seen("10-10-1010")


def get_last_seen():
     con = create_connection()
     cur = con.cursor()
     query = "Select Value from Memory where Name = 'last_seen'"
     cur.execute(query)
     return str(cur.fetchall()[0][0])   


def turn_on_speech():
     if (checkInternet()):
          con = create_connection()
          cur = con.cursor()
          query = "update Memory set Value = 'on' where Name = 'speech'";
          cur.execute(query)
          con.commit()
          return "Ok i will speak now"
     else:
          return "Please check your internet connection" 

def turn_off_speech():
     con = create_connection() 
     cur = con.cursor()
     query = "update Memory set Value = 'off' where Name = 'speech'";
     cur.execute(query)
     con.commit()
     return "Ok i won't speak"

def speak_is_on():
     con = create_connection()
     cur = con.cursor()
     query = "Select Value from Memory where Name = 'speech'";
     cur.execute(query)
     ans = str(cur.fetchall()[0][0])   

     if ans == "on":
          return True
     else:
          return False