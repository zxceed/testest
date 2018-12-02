from flask import Flask, request, jsonify, render_template
import os
import dialogflow
import requests
import json
import pusher
import re


app = Flask(__name__)


# initialize Pusher
#pusher_client = pusher.Pusher(
 #   app_id=os.getenv('PUSHER_APP_ID'),
  #  key=os.getenv('PUSHER_KEY'),
   # secret=os.getenv('PUSHER_SECRET'),
    #cluster=os.getenv('PUSHER_CLUSTER'),
    # ssl=True)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/webhook', methods=['POST'])
def webhook():
	data = request.get_json(silent=True)
	action = data['queryResult']['action']
  

	
	if (action == 'checkeligibility'):
	 return check_eligibility(data)
	
	if (action == 'checkintregistration'):
	 return check_intregistration(data)
	 
	if (action == 'checkiprep'):
	 return check_iprep(data)
	 
	if (action == 'findfaci'):
	 return find_faci(data)
	 
	if (action == 'userrating'):
	 return user_rating(data)
	 
	if (action == 'normadmin'):
	 return norm_admin(data)
	 
	if (action == 'masteradmin'):
	 return master_admin(data)
	 
	if (action == 'Noiprep'):
	 return No_iprep(data)
	 
	if (action == 'Yesiprep'):
	 return Yes_iprep(data)
	 
	if (action == 'testing1'):
	 return testing_1(data)
	 
	if (action == 'userid'):
	 return user_id(data)
	 

   #Define the function names you have stated in the if statement 
	
#ALL OF THE CODES BELOW ARE THE ONES TO BE CONSOLIDATED INTO THE MAIN FILE	
	
def check_eligibility(data):
	details = data['queryResult']['parameters']['number']
	
	import mysql.connector
	mydb = mysql.connector.connect(
	host="fyp-jab.cgizee1wopsu.ap-southeast-1.rds.amazonaws.com",
	user="fypchatbot",
	passwd="goldenpan123",
	port ="3306",
	database ="chatbot"
	)
	
	mycursor =mydb.cursor()
	
	#Validating if user exist in the table
	sql = "SELECT student_id FROM student WHERE student_id = %s"
	
	exe = (details,)
	
	mycursor.execute(sql,exe)
	
	myresult = mycursor.fetchall()
	
	
	#Count the number of rows returned
	mycursor.execute(sql,exe)
	
	counting = len(mycursor.fetchall())
	
	if counting >= 1:
	
	#Eligibility perfect

		sql = "SELECT student_id FROM student WHERE gpa >= 3 AND discipline_records = 'n' AND student_id = %s"
		
		mycursor.execute(sql,exe)
		
		perfect = len(mycursor.fetchall())
		
	#Eligibility semi-perfect 1	
		sql = "SELECT student_id FROM student WHERE gpa >=3 AND discipline_records = 'y' AND student_id = %s"
		
		mycursor.execute(sql,exe)
		
		semiperfect1 = len(mycursor.fetchall())
		
	#Eligibility semi-perfect 2	
		sql = "SELECT student_id FROM student WHERE gpa <= 3 AND discipline_records = 'n' AND student_id = %s"
		
		mycursor.execute(sql,exe)
		
		semiperfect2 = len(mycursor.fetchall())
		
	#Eligibility notperfect	
		sql = "SELECT student_id FROM student WHERE gpa <= 3 AND discipline_records = 'y' AND student_id = %s"
		
		mycursor.execute(sql,exe)
		
		notperfect = len(mycursor.fetchall())
		
		
		if perfect == 1:
		
			response = "Congrats! You are eligible for the overseas internship"
			reply = {
				"fulfillmentText": response,
				"fulfillmentMessages": [
			{
				"payload": {
				"telegram": {
				"text": response + "\n \n" + "What would you like to do next?",
				"reply_markup": {
				"inline_keyboard": [
				[
					{
                    "callback_data": "registereli",
                    "text": "I want to register for overseas internship"
					}
				],
                [
					{
                    "callback_data": "Overseas internship",
                    "text": "I still have questions about Overseas internship"
					}
				],
                [
                  {
                    "text": "I have questions about Study Trips now",
                    "callback_data": "Study trip"
                  }
                ],
                [
                  {
                    "text": "I have no other questions",
                    "callback_data": "no questions"
                  }
                ],
              ]
            }
          }
        }
			}
			]
				}
		elif semiperfect1 == 1:
		
			response = "You might be eligible for the overseas internship"
			reply = {
				"fulfillmentText": response,
				"fulfillmentMessages": [
			{
				"payload": {
				"telegram": {
				"text": response + "\n \n" + "What would you like to do next?",
				"reply_markup": {
				"inline_keyboard": [
				[
					{
                    "callback_data": "registereli",
                    "text": "I want to register for overseas internship"
					}
				],
                [
					{
                    "callback_data": "Overseas internship",
                    "text": "I still have questions about Overseas internship"
					}
				],
                [
                  {
                    "text": "I have questions about Study Trips now",
                    "callback_data": "Study trip"
                  }
                ],
                [
                  {
                    "text": "I have no other questions",
                    "callback_data": "no questions"
                  }
                ],
              ]
            }
          }
        }
			}
			]
				}
				
		elif semiperfect2 == 1:
		
			response = "You might be eligible for the overseas internship"
			reply = {
				"fulfillmentText": response,
				"fulfillmentMessages": [
			{
				"payload": {
				"telegram": {
				"text": response + "\n \n" + "What would you like to do next?",
				"reply_markup": {
				"inline_keyboard": [
				[
					{
                    "callback_data": "registereli",
                    "text": "I want to register for overseas internship"
					}
				],
                [
					{
                    "callback_data": "Overseas internship",
                    "text": "I still have questions about Overseas internship"
					}
				],
                [
                  {
                    "text": "I have questions about Study Trips now",
                    "callback_data": "Study trip"
                  }
                ],
                [
                  {
                    "text": "I have no other questions",
                    "callback_data": "no questions"
                  }
                ],
              ]
            }
          }
        }
			}
			]
				}
		elif notperfect == 1:
		
			response = "I am sorry but you do not meet the overseas internship requirement but you can still try to apply for it as it is situational"
			reply = {
				"fulfillmentText": response,
				"fulfillmentMessages": [
			{
				"payload": {
				"telegram": {
				"text": response + "\n \n" + "What would you like to do next?",
				"reply_markup": {
				"inline_keyboard": [
				[
					{
                    "callback_data": "registereli",
                    "text": "I want to register for overseas internship"
					}
				],
                [
					{
                    "callback_data": "Overseas internship",
                    "text": "I still have questions about Overseas internship"
					}
				],
                [
                  {
                    "text": "I have questions about Study Trips now",
                    "callback_data": "Study trip"
                  }
                ],
                [
                  {
                    "text": "I have no other questions",
                    "callback_data": "no questions"
                  }
                ],
              ]
            }
          }
        }
			}
			]
				}
				
		else:
			response = "Sorry, an error has occured!"
			reply = {
				"fulfillmentText": response,
				"fulfillmentMessages": [
			{
				"payload": {
				"telegram": {
				"text": response + "\n \n" + "What would you like to do next?",
				"reply_markup": {
				"inline_keyboard": [
                [
					{
                    "callback_data": "Overseas internship",
                    "text": "I still have questions about Overseas internship"
					}
				],
                [
                  {
                    "text": "I have questions about Study Trips now",
                    "callback_data": "Study trip"
                  }
                ],
                [
                  {
                    "text": "I have no other questions",
                    "callback_data": "no questions"
                  }
                ],
              ]
            }
          }
        }
			}
			]
				}
	else:
			response = "that's not right...you have given me an invalid id =/"
			reply = {
				"fulfillmentText": response,
				"fulfillmentMessages": [
			{
				"payload": {
				"telegram": {
				"text": response + "\n \n" + "What would you like to do next?",
				"reply_markup": {
				"inline_keyboard": [
				[
					{
                    "callback_data": "Overseas internship",
                    "text": "I still have questions about Overseas internship"
					}
				],
                [
                  {
                    "text": "I have questions about Study Trips now",
                    "callback_data": "Study trip"
                  }
                ],
                [
                  {
                    "text": "I have no other questions",
                    "callback_data": "feedback"
                  }
                ],
              ]
            }
          }
        }
			}
			]
			}
		
	return jsonify(reply)


		
def check_intregistration(data):

	details = data['queryResult']['parameters']['number']
	
	import mysql.connector
	mydb = mysql.connector.connect(
	host="fyp-jab.cgizee1wopsu.ap-southeast-1.rds.amazonaws.com",
	user="fypchatbot",
	passwd="goldenpan123",
	port ="3306",
	database ="chatbot"
	)
	
	mycursor =mydb.cursor()
	
	#validate if user exist in the table
	
	sql = "SELECT student_id FROM student WHERE student_id = %s"
	
	exe = (details,)
	
	mycursor.execute(sql,exe)
	
	myresult = mycursor.fetchall()
	
	#Count the number of rows returned
	
	mycursor.execute(sql,exe)
	
	counting = len(mycursor.fetchall())
	
	if counting >= 1:
	
		#Find if students have registered
	
		sql = "select student_id from internship_registration where student_id = %s"
		
		mycursor.execute(sql,exe)
		
		have = len(mycursor.fetchall())
		
		
		
		#Find student's name for response
	
		sql = "SELECT student_name from student where student_id = %s"
		
		mycursor.execute(sql,exe)
		
		name = mycursor.fetchall()
		
		#Find student's registration id if they have registered
		
		sql = "SELECT internship_registration_id from internship_registration where student_id = %s"
		
		mycursor.execute(sql,exe)
		
		regid = mycursor.fetchall()
		
		if have >= 1:
			response = "You have already registered! " + re.sub(r'[^\w\s]','',str(name)) + " your registration id is " + re.sub(r'[^\w\s]','',str(regid)) + " do not lose it as you will need it if you want to delete your registration!☺️"
			reply = {
				"fulfillmentText": response,
				"fulfillmentMessages": [
			{
				"payload": {
				"telegram": {
				"text": response + "\n \n" + "What would you like to do next?",
				"reply_markup": {
				"inline_keyboard": [
                [
					{
                    "callback_data": "Overseas internship",
                    "text": "I still have questions about Overseas internship"
					}
				],
                [
                  {
                    "text": "I have questions about Study Trips now",
                    "callback_data": "Study trip"
                  }
                ],
                [
                  {
                    "text": "I have no other questions",
                    "callback_data": "no questions"
                  }
                ],
              ]
            }
          }
        }
			}
			]
			}
		else:
			response = "You have yet to register " + re.sub(r'[^\w\s]','',str(name)) +"!" + "😁"
			reply = {
				"fulfillmentText": response,
				"fulfillmentMessages": [
			{
				"payload": {
				"telegram": {
				"text": response + "\n \n" + "What would you like to do next?",
				"reply_markup": {
				"inline_keyboard": [
				[
					{
                    "callback_data": "regicheck",
                    "text": "I want to register for overseas internship"
					}
				],
                [
					{
                    "callback_data": "Overseas internship",
                    "text": "I still have questions about Overseas internship"
					}
				],
                [
                  {
                    "text": "I have questions about Study Trips now",
                    "callback_data": "Study trip"
                  }
                ],
                [
                  {
                    "text": "I have no other questions",
                    "callback_data": "no questions"
                  }
                ],
              ]
            }
          }
        }
			}
			]
			}
	else:
			response = "that's not right...you have given me an invalid id =/"
			reply = {
				"fulfillmentText": response,
				"fulfillmentMessages": [
			{
				"payload": {
				"telegram": {
				"text": response + "\n \n" + "What would you like to do next?",
				"reply_markup": {
				"inline_keyboard": [
				[
					{
                    "callback_data": "Overseas internship",
                    "text": "I still have questions about Overseas internship"
					}
				],
                [
                  {
                    "text": "I have questions about Study Trips now",
                    "callback_data": "Study trip"
                  }
                ],
                [
                  {
                    "text": "I have no other questions",
                    "callback_data": "feedback"
                  }
                ],
              ]
            }
          }
        }
			}
			]
			}
	return jsonify(reply)	

		
		
		
def check_iprep(data):

	details = data['queryResult']['parameters']['number']
	
	import mysql.connector
	mydb = mysql.connector.connect(
	host="fyp-jab.cgizee1wopsu.ap-southeast-1.rds.amazonaws.com",
	user="fypchatbot",
	passwd="goldenpan123",
	port ="3306",
	database ="chatbot"
	)
	
	mycursor =mydb.cursor()
	
	#validate if user exist in the table
	
	sql = "SELECT student_id FROM student WHERE student_id = %s"
	
	exe = (details,)
	
	mycursor.execute(sql,exe)
	
	myresult = mycursor.fetchall()
#______________________________________________________________________________________________________________________________________________________________	
	#Count the number of rows returned
	
	mycursor.execute(sql,exe)
	
	counting = len(mycursor.fetchall())
	
	#Find student's name for response
	
	sql = "SELECT student_name from student where student_id = %s"
	
	mycursor.execute(sql,exe)
	
	name = mycursor.fetchall()
#______________________________________________________________________________________________________________________________________________________________	
	if counting >= 1:
	#For students who are in iprep
		sql = "select student_id from student where student_iprep = 'y' and student_id = %s"
		
		mycursor.execute(sql,exe)
		
		haveiprep = len(mycursor.fetchall())
		
	#For students who are not in iprep
		sql = "select student_id from student where student_iprep = 'n' and student_id = %s"
		
		mycursor.execute(sql,exe)
		
		donthaveiprep = len(mycursor.fetchall())
		#If in iprep
		if haveiprep >= 1:
			response = "You ARE in iprep " + re.sub(r'[^\w\s]','',str(name)) + " 👻"
			reply = {
				"fulfillmentText": response,
				"fulfillmentMessages": [
			{
				"payload": {
				"telegram": {
				"text": response + "\n \n" + "What would you like to do next?",
				"reply_markup": {
				"inline_keyboard": [
				[
					{
                    "callback_data": "gotoyregister",
                    "text": "Press this button to register for Overseas internship registration"
					}
				],
                [
					{
                    "callback_data": "Overseas internship",
                    "text": "I still have questions about Overseas internship"
					}
				],
                [
                  {
                    "text": "I have questions about Study Trips now",
                    "callback_data": "Study trip"
                  }
                ],
                [
                  {
                    "text": "I have no other questions",
                    "callback_data": "no questions"
                  }
                ],
              ]
            }
          }
        }
			}
			]
			}
		#If not in iprep
		elif donthaveiprep >= 1:
			response = "You are NOT in iprep " + re.sub(r'[^\w\s]','',str(name)) + " 👻"
			reply = {
				"fulfillmentText": response,
				"fulfillmentMessages": [
			{
				"payload": {
				"telegram": {
				"text": response + "\n \n" + "What would you like to do next?",
				"reply_markup": {
				"inline_keyboard": [
				[
					{
                    "callback_data": "gotonregister",
                    "text": "Press this button to register Overseas for internship registration"
					}
				],
                [
					{
                    "callback_data": "Overseas internship",
                    "text": "I still have questions about Overseas internship"
					}
				],
                [
                  {
                    "text": "I have questions about Study Trips now",
                    "callback_data": "Study trip"
                  }
                ],
                [
                  {
                    "text": "I have no other questions",
                    "callback_data": "no questions"
                  }
                ],
              ]
            }
          }
        }
			}
			]
			}

	else:
			response = "that's not right...you have given me an invalid id 😅"
			reply = {
				"fulfillmentText": response,
				"fulfillmentMessages": [
			{
				"payload": {
				"telegram": {
				"text": response + "\n \n" + "What would you like to do next?",
				"reply_markup": {
				"inline_keyboard": [
				[
					{
                    "callback_data": "Overseas internship",
                    "text": "I still have questions about Overseas internship"
					}
				],
                [
                  {
                    "text": "I have questions regarding Study Trips now",
                    "callback_data": "Study trip"
                  }
                ],
                [
                  {
                    "text": "I have no other questions",
                    "callback_data": "feedback"
                  }
                ],
              ]
            }
          }
        }
			}
			]
			}
	return jsonify(reply)
		
	


	
def find_faci(data):

	details = data['queryResult']['parameters']['number']
	
	import mysql.connector
	mydb = mysql.connector.connect(
	host="fyp-jab.cgizee1wopsu.ap-southeast-1.rds.amazonaws.com",
	user="fypchatbot",
	passwd="goldenpan123",
	port ="3306",
	database ="chatbot"
	)
	
	mycursor =mydb.cursor()
	
	#validate if user exist in the table
	
	sql = "SELECT student_id FROM student WHERE student_id = %s"
	
	exe = (details,)
	
	mycursor.execute(sql,exe)
	
	myresult = mycursor.fetchall()
	
	#Count the number of rows returned
	
	mycursor.execute(sql,exe)
	
	counting = len(mycursor.fetchall())
	
	if counting >= 1:
	
		sql = "select faci_name from faci inner join internship_registration on internship_registration.faci_id = faci.faci_id where student_id = %s"
		
		mycursor.execute(sql,exe)
		
		name = mycursor.fetchall()
		
		mycursor.execute(sql,exe)
		
		faci = len(mycursor.fetchall())
		
		if faci == 1:
			response = "The facilitator assigned to you is " + re.sub(r'[^\w\s]','',str(name))
			reply = {
				"fulfillmentText": response,
				"fulfillmentMessages": [
			{
				"payload": {
				"telegram": {
				"text": response + "\n \n" + "What would you like to do next?",
				"reply_markup": {
				"inline_keyboard": [
                [
					{
                    "callback_data": "Overseas internship",
                    "text": "I still have questions about Overseas internship"
					}
				],
                [
                  {
                    "text": "I have questions regarding Study Trips now",
                    "callback_data": "study trip"
                  }
                ],
                [
                  {
                    "text": "I have no other questions",
                    "callback_data": "no questions"
                  }
                ],
              ]
            }
          }
        }
			}
			]
			}
		else:
			response = "You have not registered for overseas internship!"
			reply = {
				"fulfillmentText": response,
				"fulfillmentMessages": [
			{
				"payload": {
				"telegram": {
				"text": response + "\n \n" + "What would you like to do next?",
				"reply_markup": {
				"inline_keyboard": [
				[
					{
                    "callback_data": "regifindfaci",
                    "text": "I want to register for overseas internship"
					}
				],
                [
					{
                    "callback_data": "Overseas internship",
                    "text": "I still have questions about Overseas internship"
					}
				],
                [
                  {
                    "text": "I have questions regarding Study Trips now",
                    "callback_data": "Study trip"
                  }
                ],
                [
                  {
                    "text": "I have no other questions",
                    "callback_data": "no questions"
                  }
                ],
              ]
            }
          }
        }
			}
			]
			}
	else:
		response = "that's not right...you have given me an invalid id =/"
		reply = {
				"fulfillmentText": response,
				"fulfillmentMessages": [
			{
				"payload": {
				"telegram": {
				"text": response + "\n \n" + "What would you like to do next?",
				"reply_markup": {
				"inline_keyboard": [
				[
					{
                    "callback_data": "Overseas internship",
                    "text": "I still have questions about Overseas internship"
					}
				],
                [
                  {
                    "text": "I have questions regarding Study Trips now",
                    "callback_data": "Study trip"
                  }
                ],
                [
                  {
                    "text": "I have no other questions",
                    "callback_data": "feedback"
                  }
                ],
              ]
            }
          }
        }
			}
			]
			}
	return jsonify(reply)

		
		
		
		
def user_rating(data):
	
	details = data['queryResult']['parameters']['Ratings']
	
	import mysql.connector
	mydb = mysql.connector.connect(
	host="fyp-jab.cgizee1wopsu.ap-southeast-1.rds.amazonaws.com",
	user="fypchatbot",
	passwd="goldenpan123",
	port ="3306",
	database ="chatbot"
	)
	
	mycursor =mydb.cursor()
	
	#Insert user's feedback into the feedback table given 
	
	sql = "INSERT INTO user_feedback (rating) VALUES (%s)"
	
	exe = (details,)
		
	mycursor.execute(sql,exe)
		
	mydb.commit()
	
	response = "Thank You for your feedback! p.s. i'm just joking about the reward, don't take it to heart =)"
	reply = {
		"fulfillmentText": response
		}
	return jsonify(reply)

	
	
	
	
	
def norm_admin(data):
	details = data['queryResult']['parameters']['number']
	
	import mysql.connector
	mydb = mysql.connector.connect(
	host="fyp-jab.cgizee1wopsu.ap-southeast-1.rds.amazonaws.com",
	user="fypchatbot",
	passwd="goldenpan123",
	port ="3306",
	database ="chatbot"
	)
	
	mycursor =mydb.cursor()
	
	#Find students who are under the specific facilitator
	
	sql = "SELECT student_id from internship_registration where faci_id = %s"
	
	exe = (details,)
	
	mycursor.execute(sql,exe)
	
	myresult = mycursor.fetchall() 
	
	
	#Count the numbers of rows returned for the students 
	
	mycursor.execute(sql,exe)
	
	counting = len(mycursor.fetchall())
	
	
	
	if counting >= 1:
	
		response = "This is the list of student who have indicated their interest" + re.sub(r'[^\w\s]','',str(myresult)) + "\n \n" + "The number of students who have registered: " + counting
		reply = {
        "fulfillmentText": response,
		"fulfillmentMessages": [
			{
				"payload": {
				"telegram": {
				"text": response + "\n \n" + "What would you like to do next?",
				"reply_markup": {
				"inline_keyboard": [
				[
					{
                    "callback_data": "Overseas internship",
                    "text": "I still have questions about Overseas internship"
					}
				],
                [
                  {
                    "text": "I have questions regarding Study Trips now",
                    "callback_data": "Study trip"
                  }
                ],
                [
                  {
                    "text": "I have no other questions",
                    "callback_data": "feedback"
                  }
                ],
              ]
            }
          }
        }
			}
			]
		
		}
		
	else:
			response = "No students have indicated their interest yet"
			reply = {
			"fulfillmentText": response,
			"fulfillmentMessages": [
			{
				"payload": {
				"telegram": {
				"text": response + "\n \n" + "What would you like to do next?",
				"reply_markup": {
				"inline_keyboard": [
				[
					{
                    "callback_data": "Overseas internship",
                    "text": "I still have questions about Overseas internship"
					}
				],
                [
                  {
                    "text": "I have questions regarding Study Trips now",
                    "callback_data": "Study trip"
                  }
                ],
                [
                  {
                    "text": "I have no other questions",
                    "callback_data": "feedback"
                  }
                ],
              ]
            }
          }
        }
			}
			]
			}
	return jsonify(reply)
	
	
	
	
	
def master_admin(data):

	details = data['queryResult']['parameters']['number']
	
	import mysql.connector
	mydb = mysql.connector.connect(
	host="fyp-jab.cgizee1wopsu.ap-southeast-1.rds.amazonaws.com",
	user="fypchatbot",
	passwd="goldenpan123",
	port ="3306",
	database ="chatbot"
	)
	
	mycursor =mydb.cursor()
	
	
def testing_1(data):

	details = data['queryResult']['parameters']['number']
	
	import mysql.connector
	mydb = mysql.connector.connect(
	host="fyp-jab.cgizee1wopsu.ap-southeast-1.rds.amazonaws.com",
	user="fypchatbot",
	passwd="goldenpan123",
	port ="3306",
	database ="chatbot"
	)
	
	mycursor =mydb.cursor()
	
	
	
	#validate if user exist in the table
	
	sql = "SELECT student_id FROM student WHERE student_id = %s and student_iprep = 'y'"
	
	exe = (details,)
	
	mycursor.execute(sql,exe)
	
	studentid = mycursor.fetchall()
	
	
	
	#Count the number of rows returned
	
	mycursor.execute(sql,exe)
	
	counting = len(mycursor.fetchall())
	
	sql = "SELECT student_name from student where student_id = %s"
		
	mycursor.execute(sql,exe)
		
	name = mycursor.fetchall()
	
	
	if counting >= 1:
		response = "You have successfully registered! " + re.sub(r'[^\w\s]','',str(name))
		reply = {
        "fulfillmentText": response
		}
	return jsonify(reply)
	
	
def Yes_iprep(data):

	details = data['queryResult']['parameters']['number']
	
	import mysql.connector
	mydb = mysql.connector.connect(
	host="fyp-jab.cgizee1wopsu.ap-southeast-1.rds.amazonaws.com",
	user="fypchatbot",
	passwd="goldenpan123",
	port ="3306",
	database ="chatbot"
	)
	
	mycursor =mydb.cursor()
	
	
	
	#validate if user exist in the table
	
	sql = "SELECT student_id FROM student WHERE student_id = %s"
	
	exe = (details,)
	
	mycursor.execute(sql,exe)
	
	studentid = mycursor.fetchall()
	
	
	
	
	
	#Count the number of rows returned
	
	mycursor.execute(sql,exe)
	
	counting = len(mycursor.fetchall())
	
	
	
	
	if counting >= 1:
	
		#Validate if user belongs in iprep
	
		sql = "SELECT student_id FROM student WHERE student_id = %s and student_iprep = 'y'"
	
		mycursor.execute(sql,exe)
	
		studentid = mycursor.fetchall()
		
		#Count the number of rows returned 
		
		mycursor.execute(sql,exe)
		
		counter = len(mycursor.fetchall())
		
		if counter >= 1:
		
	#For students that are under Iprep for SEG - Label (SEG)
	
			sql = "INSERT INTO internship_registration(student_id,faci_id) SELECT student.student_id,faci.faci_id FROM student inner join faci on faci.school_code = student.school_code WHERE student.student_id = %s and student.student_iprep = 'y' and faci.faci_iprep = 'y' and faci.faci_incharge_intern ='y' and student.school_code = 'SEG' and student.student_year = 2"
	
			mycursor.execute(sql,exe)
	
			mydb.commit()
	
	
	
	#To check if the student id is for student in (SEG) - Label (SEG)
	
			sql = "SELECT internship_registration.internship_registration_id FROM internship_registration inner join faci on faci.faci_id = internship_registration.faci_id WHERE  internship_registration.student_id = %s and faci.faci_iprep = 'y' and faci.faci_incharge_intern ='y' and faci.school_code = 'SEG'"
	
			mycursor.execute(sql,exe)
	
			YESSEG = mycursor.fetchall()
	
	
		#Counting number of rows returned for (SEG)
	
			mycursor.execute(sql,exe)
	
			CountYSEG = len(mycursor.fetchall())
	
#____________________________________________________________________________________________________________________________________________________________________________________
	
	#For students that are under Iprep for STA - Label (STA)
	
			sql = "INSERT INTO internship_registration(student_id,faci_id) SELECT student.student_id,faci.faci_id FROM student inner join faci on faci.school_code = student.school_code WHERE student.student_id = %s and student.student_iprep = 'y' and faci.faci_iprep = 'y' and faci.faci_incharge_intern ='y' and student.school_code = 'STA' and student.student_year = 2"
	
			mycursor.execute(sql,exe)
	
			mydb.commit()
	
	
	
	#To check if the student id is for student in (STA) and also to insert into response statement
	
			sql = "SELECT internship_registration.internship_registration_id FROM internship_registration inner join faci on faci.faci_id = internship_registration.faci_id WHERE  internship_registration.student_id = %s and faci.faci_iprep = 'y' and faci.faci_incharge_intern ='y' and faci.school_code = 'STA'"
	
			mycursor.execute(sql,exe)
	
			YESSTA = mycursor.fetchall()
	
	
		#Counting number of rows returned for (STA)
	
			mycursor.execute(sql,exe)
	
			CountYSTA = len(mycursor.fetchall())
		
#___________________________________________________________________________________________________________________________________________________________________________________
	
	#For students that are under Iprep for SOI - Label (SOI)
			sql = "INSERT INTO internship_registration(student_id,faci_id) SELECT student.student_id,faci.faci_id FROM student inner join faci on faci.school_code = student.school_code WHERE student.student_id = %s and student.student_iprep = 'y' and faci.faci_iprep = 'y' and faci.faci_incharge_intern ='y' and student.school_code = 'SOI' and student.student_year = 2"
	
			mycursor.execute(sql,exe)
	
			mydb.commit()
	
	
	
	#To check if the student id is for student in (SOI) and also to insert into response statement
	
			sql = "SELECT internship_registration.internship_registration_id FROM internship_registration inner join faci on faci.faci_id = internship_registration.faci_id WHERE  internship_registration.student_id = %s and faci.faci_iprep = 'y' and faci.faci_incharge_intern ='y' and faci.school_code = 'SOI'"
	
			mycursor.execute(sql,exe)
	
			YESSOI = mycursor.fetchall()
	
	
		#Counting number of rows returned for (SOI)
	
			mycursor.execute(sql,exe)
	
			CountYSOI = len(mycursor.fetchall())
		
	#___________________________________________________________________________________________________________________________________________________________________________________	
	
	#Finding facilitator name for students
	
			sql = "SELECT faci_name from faci inner join internship_registration on faci.faci_id = internship_registration.faci_id where student_id = %s"

			mycursor.execute(sql,exe)

			faci = mycursor.fetchall()
		
		
	#Find student's name for response
	
			sql = "SELECT student_name from student where student_id = %s"
		
			mycursor.execute(sql,exe)
		
			name = mycursor.fetchall()
#______________________________________________________________________________________________________________________________________________________________	
	#To generate user response that contains registration id and the facilitator in charge 
			if CountYSEG >= 1:
				response = "You have successfully registered! " + re.sub(r'[^\w\s]','',str(name)) + "=)" + "\n \n" +"Your registration id is " + re.sub(r'[^\w\s]','',str(YESSEG)) + " don't lose it! you will need this id in the event if you want to cancel your registration!" + "\n \n" + re.sub(r'[^\w\s]','',str(faci)) + " will contact you soon"
			
				reply = {
				"fulfillmentText": response,
				"fulfillmentMessages": [
				{
					"payload": {
					"telegram": {
					"text": response + "\n \n" + "What would you like to do next?",
					"reply_markup": {
					"inline_keyboard": [
					[
						{
						"callback_data": "Overseas internship",
						"text": "I still have questions regarding Overseas internship"
						}
					],
					[
						{
						"text": "I have questions regarding Study Trips now",
						"callback_data": "Study trip"
						}
					],
					[
						{
						"text": "I have no other questions",
						"callback_data": "no questions"
						}
					],
				]
				}
				}
			}
				}
				]
				}
		
		
		
			elif CountYSTA >= 1:
				response = "You have successfully registered! " + re.sub(r'[^\w\s]','',str(name)) + "=)" + "\n \n" +"Your registration id is " + re.sub(r'[^\w\s]','',str(YESSTA)) + " don't lose it! you will need this id in the event if you want to cancel your registration!" + "\n \n" + re.sub(r'[^\w\s]','',str(faci)) + " will contact you soon"
			
				reply = {
				"fulfillmentText": response,
				"fulfillmentMessages": [
				{
					"payload": {
					"telegram": {
					"text": response + "\n \n" + "What would you like to do next?",
					"reply_markup": {
					"inline_keyboard": [
					[
						{
						"callback_data": "Overseas internship",
						"text": "I still have questions regarding Overseas internship"
						}
					],
					[
						{
						"text": "I have questions regarding Study Trips now",
						"callback_data": "Study trip"
						}
					],
					[
						{
						"text": "I have no other questions",
						"callback_data": "no questions"
						}
					],
				]
            }
          }
        }
			}
			]
			}
			
			elif CountYSOI >= 1:
				response = "You have successfully registered! " + re.sub(r'[^\w\s]','',str(name)) + "=)" + "\n \n" +"Your registration id is " + re.sub(r'[^\w\s]','',str(YESSOI)) + " don't lose it! you will need this id in the event if you want to cancel your registration!" + "\n \n" + re.sub(r'[^\w\s]','',str(faci)) + " will contact you soon"
			
				reply = {
				"fulfillmentText": response,
				"fulfillmentMessages": [
				{
					"payload": {
					"telegram": {
					"text": response + "\n \n" + "What would you like to do next?",
					"reply_markup": {
					"inline_keyboard": [
					[
						{
						"callback_data": "Overseas internship",
						"text": "I still have questions regarding Overseas internship"
						}
					],
					[
						{
						"text": "I have questions regarding Study Trips now",
						"callback_data": "Study trip"
					}
					],
					[
						{
						"text": "I have no other questions",
						"callback_data": "no questions"
						}
					],
				]
            }
          }
        }
			}
			]
			}
			
			else:
				response = "that's not right...you are messing with me aren't you? the id you have given shows that either you are not year 2 yet or you are already year 3 (Year 1 and 3 can't register for iprep)"
				reply = {
				"fulfillmentText": response,
				"fulfillmentMessages": [
				{
					"payload": {
					"telegram": {
					"text": response + "\n \n" + "What would you like to do next?",
					"reply_markup": {
					"inline_keyboard": [
					[
						{
						"callback_data": "Overseas internship",
						"text": "I still have questions regarding Overseas internship"
						}
					],
					[
						{
						"text": "I have questions regarding Study Trips now",
						"callback_data": "Study trip"
						}
					],
					[
						{
						"text": "I have no other questions",
						"callback_data": "feedback"
						}
					],
				]
            }
          }
        }
			}
			]
			}

		
		else:
			response = "that's not right...it says here you do not belong in iprep"
			reply = {
			"fulfillmentText": response,
			"fulfillmentMessages": [
			{
				"payload": {
				"telegram": {
				"text": response + "\n \n" + "What would you like to do next?",
				"reply_markup": {
				"inline_keyboard": [
				[
					{
                    "callback_data": "gotonoiprep",
                    "text": "Please re-route me to Non-IPREP registration"
					}
				],
				[
					{
                    "callback_data": "Overseas internship",
                    "text": "I still have questions about Overseas internship"
					}
				],
                [
                  {
                    "text": "I have questions regarding Study Trips now",
                    "callback_data": "Study trip"
                  }
                ],
                [
                  {
                    "text": "I have no other questions",
                    "callback_data": "feedback"
                  }
                ],
              ]
            }
          }
        }
			}
			]
			}

	
	else:
			response = "that's not right...you have given me an invalid id =( Please try again!"
			reply = {
			"fulfillmentText": response,
			
			}
	return jsonify(reply)
	
	
def No_iprep(data):

	details = data['queryResult']['parameters']['number']
	
	import mysql.connector
	mydb = mysql.connector.connect(
	host="fyp-jab.cgizee1wopsu.ap-southeast-1.rds.amazonaws.com",
	user="fypchatbot",
	passwd="goldenpan123",
	port ="3306",
	database ="chatbot"
	)
	
	mycursor =mydb.cursor()
	
	
	
	#validate if user exist in the table
	
	sql = "SELECT student_id FROM student WHERE student_id = %s"
	
	exe = (details,)
	
	mycursor.execute(sql,exe)
	
	studentid = mycursor.fetchall()
	
	
	
	
	
	#Count the number of rows returned
	
	mycursor.execute(sql,exe)
	
	counting = len(mycursor.fetchall())
	
	
	
	
	if counting >= 1:
	
	#Check to make sure user do not belong in iprep
		sql = "SELECT student_id FROM student WHERE student_id = %s and student_iprep = 'n'"
	
		mycursor.execute(sql,exe)
	
		studentid = mycursor.fetchall()
	
	
	
	
	
		#Count the number of rows returned
	
		mycursor.execute(sql,exe)
	
		counter = len(mycursor.fetchall())
	
	
	
	
		if counter >= 1:
		
		#For students that are NOT in iprep for SEG - Label (SEG)
	
			sql = "INSERT INTO internship_registration(student_id,faci_id) SELECT student.student_id,faci.faci_id FROM student inner join faci on faci.school_code = student.school_code WHERE student.student_id = %s and student.student_iprep = 'n' and faci.faci_iprep = 'n' and faci.faci_incharge_intern ='y' and student.school_code = 'seg' and student.student_year = 2"
	
			mycursor.execute(sql,exe)
	
			mydb.commit()
	
	
	
	#To check if the student id is for student in (SEG) and also to insert into response statement
	
			sql = "SELECT internship_registration.internship_registration_id FROM internship_registration inner join faci on faci.faci_id = internship_registration.faci_id WHERE  internship_registration.student_id = %s and faci.faci_iprep = 'n' and faci.faci_incharge_intern ='y' and faci.school_code = 'SEG'"
	
			mycursor.execute(sql,exe)
	
			NOSEG = mycursor.fetchall()
	
	
		#Counting number of rows returned for (SEG)
	
			mycursor.execute(sql,exe)
	
			CountSEG = len(mycursor.fetchall())
	
#______________________________________________________________________________________________________________________________________________________________
	
	#For students that are NOT in iprep for STA - Label (STA)
	
			sql = "INSERT INTO internship_registration(student_id,faci_id) SELECT student.student_id,faci.faci_id FROM student inner join faci on faci.school_code = student.school_code WHERE student.student_id = %s and student.student_iprep = 'n' and faci.faci_iprep = 'n' and faci.faci_incharge_intern ='y' and student.school_code = 'STA' and student.student_year = 2"
	
			mycursor.execute(sql,exe)
	
			mydb.commit()
	
	
	#To check if the student id is for student in (STA) and also to insert into response statement
	
			sql = "SELECT internship_registration.internship_registration_id FROM internship_registration inner join faci on faci.faci_id = internship_registration.faci_id WHERE  internship_registration.student_id = %s and faci.faci_iprep = 'n' and faci.faci_incharge_intern ='y' and faci.school_code = 'STA'"
	
			mycursor.execute(sql,exe)
	
			NOSTA = mycursor.fetchall()
	
	
	#Counting number of rows returned for (STA)
	
			mycursor.execute(sql,exe)
	
			CountSTA = len(mycursor.fetchall())
	
	
#______________________________________________________________________________________________________________________________________________________________	
	
	#For students that are NOT in iprep for SOI - Label (SOI)
	
			sql = "INSERT INTO internship_registration(student_id,faci_id) SELECT student.student_id,faci.faci_id FROM student inner join faci on faci.school_code = student.school_code WHERE student.student_id = %s and student.student_iprep = 'n' and faci.faci_iprep = 'n' and faci.faci_incharge_intern ='y' and student.school_code = 'SOI' and student.student_year = 2"
	
			mycursor.execute(sql,exe)
	
			mydb.commit()
	
	
	#To check if the student id is for student in (SOI) and also to insert into response statement
	
			sql = "SELECT internship_registration.internship_registration_id FROM internship_registration inner join faci on faci.faci_id = internship_registration.faci_id WHERE  internship_registration.student_id = %s and faci.faci_iprep = 'n' and faci.faci_incharge_intern ='y' and faci.faci_incharge_intern ='y' and faci.school_code = 'SOI'"
	
			mycursor.execute(sql,exe)
	
			NOSOI = mycursor.fetchall()
	
	#Counting number of rows returned for (SOI)
	
			mycursor.execute(sql,exe)
	
			CountSOI = len(mycursor.fetchall())
		
#______________________________________________________________________________________________________________________________________________________________		
		
	#For students that are NOT in iprep for SOH - Label (SOH)
	
			sql = "INSERT INTO internship_registration(student_id,faci_id) SELECT student.student_id,faci.faci_id FROM student inner join faci on faci.school_code = student.school_code WHERE student.student_id = %s and student.student_iprep = 'n' and faci.faci_iprep = 'n' and faci.faci_incharge_intern ='y' and student.school_code = 'SOH' and student.student_year = 2"
	
			mycursor.execute(sql,exe)
	
			mydb.commit()
	
	
	#To check if the student id is for student in (SOH) and also to insert into response statement
	
			sql = "SELECT internship_registration.internship_registration_id FROM internship_registration inner join faci on faci.faci_id = internship_registration.faci_id WHERE  internship_registration.student_id = %s and faci.faci_iprep = 'n' and faci.faci_incharge_intern ='y' and faci.faci_incharge_intern ='y' and faci.school_code = 'SOH'"
	
			mycursor.execute(sql,exe)
	
			NOSOH = mycursor.fetchall()
	
	#Counting number of rows returned for (SOH)
	
			mycursor.execute(sql,exe)
	
			CountSOH = len(mycursor.fetchall())
		
#_________________________________________________________________________________________________________________________________________________________________________________________________________________________

		
	#For students that are NOT in iprep for SMC - Label (SMC)
	
			sql = "INSERT INTO internship_registration(student_id,faci_id) SELECT student.student_id,faci.faci_id FROM student inner join faci on faci.school_code = student.school_code WHERE student.student_id = %s and student.student_iprep = 'n' and faci.faci_iprep = 'n' and faci.faci_incharge_intern ='y' and student.school_code = 'SMC' and student.student_year = 2"
	
			mycursor.execute(sql,exe)
	
			mydb.commit()
	
	
	#To check if the student id is for student in (SMC) and also to insert into response statement
	
			sql = "SELECT internship_registration.internship_registration_id FROM internship_registration inner join faci on faci.faci_id = internship_registration.faci_id WHERE  internship_registration.student_id = %s and faci.faci_iprep = 'n' and faci.faci_incharge_intern ='y' and faci.faci_incharge_intern ='y' and faci.school_code = 'SMC'"
	
			mycursor.execute(sql,exe)
	
			NOSMC = mycursor.fetchall()
	
	#Counting number of rows returned for (SMC)
	
			mycursor.execute(sql,exe)
	
			CountSMC = len(mycursor.fetchall())	
		
		
#_____________________________________________________________________________________________________________________________________________________________________________________________________________________		
		
	#For students that are NOT in iprep for SHL - Label (SHL)
	
			sql = "INSERT INTO internship_registration(student_id,faci_id) SELECT student.student_id,faci.faci_id FROM student inner join faci on faci.school_code = student.school_code WHERE student.student_id = %s and student.student_iprep = 'n' and faci.faci_iprep = 'n' and faci.faci_incharge_intern ='y' and student.school_code = 'SHL' and student.student_year = 2"
	
			mycursor.execute(sql,exe)
	
			mydb.commit()
	
	
	#To check if the student id is for student in (SHL) and also to insert into response statement
	
			sql = "SELECT internship_registration.internship_registration_id FROM internship_registration inner join faci on faci.faci_id = internship_registration.faci_id WHERE  internship_registration.student_id = %s and faci.faci_iprep = 'n' and faci.faci_incharge_intern ='y' and faci.faci_incharge_intern ='y' and faci.school_code = 'SHL'"
	
			mycursor.execute(sql,exe)
	
			NOSHL = mycursor.fetchall()
	
	#Counting number of rows returned for (SHL)
	
			mycursor.execute(sql,exe)
	
			CountSHL = len(mycursor.fetchall())
	
	
#___________________________________________________________________________________________________________________________________________________________________________________________________________________________
	
	#For students that are NOT in iprep for SAS - Label (SAS)
	
			sql = "INSERT INTO internship_registration(student_id,faci_id) SELECT student.student_id,faci.faci_id FROM student inner join faci on faci.school_code = student.school_code WHERE student.student_id = %s and student.student_iprep = 'n' and faci.faci_iprep = 'n' and faci.faci_incharge_intern ='y' and student.school_code = 'SAS' and student.student_year = 2"
	
			mycursor.execute(sql,exe)
	
			mydb.commit()
	
	
	#To check if the student id is for student in (SAS) and also to insert into response statement
	
			sql = "SELECT internship_registration.internship_registration_id FROM internship_registration inner join faci on faci.faci_id = internship_registration.faci_id WHERE  internship_registration.student_id = %s and faci.faci_iprep = 'n' and faci.faci_incharge_intern ='y' and faci.faci_incharge_intern ='y' and faci.school_code = 'SAS'"
	
			mycursor.execute(sql,exe)
	
			NOSAS = mycursor.fetchall()
	
	#Counting number of rows returned for (SAS)
	
			mycursor.execute(sql,exe)
	
			CountSAS = len(mycursor.fetchall())
#____________________________________________________________________________________________________________________________________________________________________________________________________________________________

	
	#Finding facilitator name for students 
		
			sql = "SELECT faci_name from faci inner join internship_registration on faci.faci_id = internship_registration.faci_id where student_id = %s"

			mycursor.execute(sql,exe)

			faci = mycursor.fetchall()
		
		
	#Find student name for the response
	
			sql = "select student_name from student where student_id = %s"
		
			mycursor.execute(sql,exe)
		
			name = mycursor.fetchall()
	
#______________________________________________________________________________________________________________________________________________________________________________________________________________________________	
	#To generate user response that contains registration id and the facilitator in charge 
	
	
			#If there are rows returned for the statements execute code below
			if CountSEG >= 1:
				response = "You have successfully registered! " + re.sub(r'[^\w\s]','',str(name)) + "=)" + "\n \n" +"Your registration id is " + re.sub(r'[^\w\s]','',str(NOSEG)) + " don't lose it! you will need this id in the event if you want to cancel your registration!" + "\n \n" + re.sub(r'[^\w\s]','',str(faci)) + " will contact you soon"
			
				reply = {
				"fulfillmentText": response,
				"fulfillmentMessages": [
				{
					"payload": {
					"telegram": {
					"text": response + "\n \n" + "What would you like to do next?",
					"reply_markup": {
					"inline_keyboard": [
					[
						{
						"callback_data": "Overseas internship",
						"text": "I still have questions regarding Overseas internship"
						}
					],
					[
						{
						"text": "I have questions regarding Study Trips now",
						"callback_data": "Study trip"
						}
					],
					[
						{
						"text": "I have no other questions",
						"callback_data": "no questions"
						}
					],
				]
            }
          }
        }
			}
			]
			}
			
			elif CountSTA >= 1:
				response = "You have successfully registered! " + re.sub(r'[^\w\s]','',str(name)) + "=)" + "\n \n" +"Your registration id is " + re.sub(r'[^\w\s]','',str(NOSTA)) + " don't lose it! you will need this id in the event if you want to cancel your registration!" + "\n \n" + re.sub(r'[^\w\s]','',str(faci)) + " will contact you soon"
			
				reply = {
				"fulfillmentText": response,
				"fulfillmentMessages": [
				{
					"payload": {
					"telegram": {
					"text": response + "\n \n" + "What would you like to do next?",
					"reply_markup": {
					"inline_keyboard": [
					[
						{
						"callback_data": "Overseas internship",
						"text": "I still have questions regarding Overseas internship"
						}
					],
					[
						{
						"text": "I have questions regarding Study Trips now",
						"callback_data": "Study trip"
						}
					],
					[
						{
						"text": "I have no other questions",
						"callback_data": "no questions"
						}
					],
				]
            }
          }
        }
			}
			]
			}
			
			elif CountSOI >= 1:
				response = "You have successfully registered! " + re.sub(r'[^\w\s]','',str(name)) + "=)" + "\n \n" +"Your registration id is " + re.sub(r'[^\w\s]','',str(NOSOI)) + " don't lose it! you will need this id in the event if you want to cancel your registration!" + "\n \n" + re.sub(r'[^\w\s]','',str(faci)) + " will contact you soon"
			
				reply = {
				"fulfillmentText": response,
				"fulfillmentMessages": [
				{
					"payload": {
					"telegram": {
					"text": response + "\n \n" + "What would you like to do next?",
					"reply_markup": {
					"inline_keyboard": [
					[
						{
						"callback_data": "Overseas internship",
						"text": "I still have questions regarding Overseas internship"
						}
					],
					[
						{
						"text": "I have questions regarding Study Trips now",
						"callback_data": "Study trip"
						}
					],
					[
						{
						"text": "I have no other questions",
						"callback_data": "no questions"
						}
					],
				]
            }
          }
        }
			}
			]
			}
		


			elif CountSOH >= 1:
				response = "You have successfully registered! " + re.sub(r'[^\w\s]','',str(name)) + "=)" + "\n \n" +"Your registration id is " + re.sub(r'[^\w\s]','',str(NOSOH)) + " don't lose it! you will need this id in the event if you want to cancel your registration!" + "\n \n" + re.sub(r'[^\w\s]','',str(faci)) + " will contact you soon"
			
				reply = {
				"fulfillmentText": response,
				"fulfillmentMessages": [
				{
					"payload": {
					"telegram": {
					"text": response + "\n \n" + "What would you like to do next?",
					"reply_markup": {
					"inline_keyboard": [
					[
						{
						"callback_data": "Overseas internship",
						"text": "I still have questions regarding Overseas internship"
						}
					],
					[
						{
						"text": "I have questions regarding Study Trips now",
						"callback_data": "Study trip"
						}
					],
					[
						{
						"text": "I have no other questions",
						"callback_data": "no questions"
						}
					],
				]
            }
          }
        }
			}
			]
			}
			
			
			elif CountSMC >= 1:
				response = "You have successfully registered! " + re.sub(r'[^\w\s]','',str(name)) + "=)" + "\n \n" +"Your registration id is " + re.sub(r'[^\w\s]','',str(NOSMC)) + " don't lose it! you will need this id in the event if you want to cancel your registration!" + "\n \n" + re.sub(r'[^\w\s]','',str(faci)) + " will contact you soon"
			
				reply = {
				"fulfillmentText": response,
				"fulfillmentMessages": [
				{
					"payload": {
					"telegram": {
					"text": response + "\n \n" + "What would you like to do next?",
					"reply_markup": {
					"inline_keyboard": [
					[
						{
						"callback_data": "Overseas internship",
						"text": "I still have questions regarding Overseas internship"
						}
					],
					[
						{
						"text": "I have questions regarding Study Trips now",
						"callback_data": "Study trip"
						}
					],
					[
						{
						"text": "I have no other questions",
						"callback_data": "no questions"
						}
					],
				]
            }
          }
        }
			}
			]
			}



			elif CountSHL >= 1:
				response = "You have successfully registered! " + re.sub(r'[^\w\s]','',str(name)) + "=)" + "\n \n" +"Your registration id is " + re.sub(r'[^\w\s]','',str(NOSHL)) + " don't lose it! you will need this id in the event if you want to cancel your registration!" + "\n \n" + re.sub(r'[^\w\s]','',str(faci)) + " will contact you soon"
			
				reply = {
				"fulfillmentText": response,
				"fulfillmentMessages": [
				{
					"payload": {
					"telegram": {
					"text": response + "\n \n" + "What would you like to do next?",
					"reply_markup": {
					"inline_keyboard": [
					[
						{
						"callback_data": "Overseas internship",
						"text": "I still have questions regarding Overseas internship"
						}
					],
					[
						{
						"text": "I have questions regarding Study Trips now",
						"callback_data": "Study trip"
						}
					],
					[
						{
						"text": "I have no other questions",
						"callback_data": "no questions"
						}
					],
				]
            }
          }
        }
			}
			]
			}


			elif CountSAS >= 1:
				response = "You have successfully registered! " + re.sub(r'[^\w\s]','',str(name)) + "=)" + "\n \n" +"Your registration id is " + re.sub(r'[^\w\s]','',str(NOSAS)) + " don't lose it! you will need this id in the event if you want to cancel your registration!" + "\n \n" + re.sub(r'[^\w\s]','',str(faci)) + " will contact you soon"
			
				reply = {
				"fulfillmentText": response,
				"fulfillmentMessages": [
				{
					"payload": {
					"telegram": {
					"text": response + "\n \n" + "What would you like to do next?",
					"reply_markup": {
					"inline_keyboard": [
					[
						{
						"callback_data": "Overseas internship",
						"text": "I still have questions regarding Overseas internship"
						}
					],
					[
						{
						"text": "I have questions regarding Study Trips now",
						"callback_data": "Study trip"
						}
					],
					[
						{
						"text": "I have no other questions",
						"callback_data": "no questions"
						}
					],
				]
            }
          }
        }
			}
			]
			}
			
			else:
				response = "that's not right...you are messing with me aren't you? the id you have given shows that either you are not year 2 yet or you are already year 3 (Year 1 and 3 can't register for iprep)"
				reply = {
				"fulfillmentText": response,
				"fulfillmentMessages": [
				{
					"payload": {
					"telegram": {
					"text": response + "\n \n" + "What would you like to do next?",
					"reply_markup": {
					"inline_keyboard": [
					[
						{
						"callback_data": "Overseas internship",
						"text": "I still have questions regarding Overseas internship"
						}
					],
					[
						{
						"text": "I have questions regarding Study Trips now",
						"callback_data": "Study trip"
						}
					],
					[
						{
						"text": "I have no other questions",
						"callback_data": "feedback"
						}
					],
				]
            }
          }
        }
			}
			]
			}

		
		else:
			response = "that's not right...it says here you belong in iprep"
			reply = {
			"fulfillmentText": response,
			"fulfillmentMessages": [
			{
				"payload": {
				"telegram": {
				"text": response + "\n \n" + "What would you like to do next?",
				"reply_markup": {
				"inline_keyboard": [
				[
					{
                    "callback_data": "gotoiprep",
                    "text": "Please re-route me to IPREP registration"
					}
				],
				[
					{
                    "callback_data": "Overseas internship",
                    "text": "I still have questions about Overseas internship"
					}
				],
                [
                  {
                    "text": "I have questions regarding Study Trips now",
                    "callback_data": "Study trip"
                  }
                ],
                [
                  {
                    "text": "I have no other questions",
                    "callback_data": "feedback"
                  }
                ],
              ]
            }
          }
        }
			}
			]
			}

	
	else:
			response = "that's not right...you have given me an invalid id =/"
			reply = {
			"fulfillmentText": response,
			"fulfillmentMessages": [
			{
				"payload": {
				"telegram": {
				"text": response + "\n \n" + "What would you like to do next?",
				"reply_markup": {
				"inline_keyboard": [
				[
					{
                    "callback_data": "Overseas internship",
                    "text": "I still have questions about Overseas internship"
					}
				],
                [
                  {
                    "text": "I have questions regarding Study Trips now",
                    "callback_data": "Study trip"
                  }
                ],
                [
                  {
                    "text": "I have no other questions",
                    "callback_data": "feedback"
                  }
                ],
              ]
            }
          }
        }
			}
			]
			}
	return jsonify(reply)

def user_id(data):

	details = data['queryResult']['parameters']['number']
	
	import mysql.connector
	mydb = mysql.connector.connect(
	host="fyp-jab.cgizee1wopsu.ap-southeast-1.rds.amazonaws.com",
	user="fypchatbot",
	passwd="goldenpan123",
	port ="3306",
	database ="chatbot"
	)
	
	mycursor =mydb.cursor()
	
	
	
	#validate if user exist in the table
	
	sql = "SELECT student_id FROM student WHERE student_id = %s"
	
	exe = (details,)
	
	mycursor.execute(sql,exe)
	
	studentid = mycursor.fetchall()
	
	
	
	
	
	#Count the number of rows returned
	
	mycursor.execute(sql,exe)
	
	counting = len(mycursor.fetchall())
	
	
	
	
	if counting >= 1:
			response = "What would you like to know?"
			reply = {
				"fulfillmentText": response,
				"fulfillmentMessages": [
			{
				"payload": {
				"telegram": {
				"text": response + "\n \n" + "What would you like to do next?",
				"reply_markup": {
				"inline_keyboard": [
                [
					{
                    "callback_data": "Overseas internship",
                    "text": "I have questions regarding Overseas internship"
					}
				],
                [
                  {
                    "text": "I have questions regarding SOT now",
                    "callback_data": "SOT"
                  }
                ]
              ]
            }
          }
        }
			}
			]
				}	

	return jsonify(reply)	
# run Flask app
if __name__ == "__main__":
    app.run()