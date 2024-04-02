import json

# JSON data representing the training session
training_session_json = '''
{
  "name": "Python Training",
  "date": "April 19, 2024",
  "completed": true,
  "instructor": {
   "name": "XYZ",
   "website": "http://pqr.com/"
  },
  "participants": [
    {
      "name": "Participant 1",
      "email": "email1@example.com"
    },
    {
      "name": "Participant 2",
      "email": "email2@example.com"
    }
  ]
}
'''

# Parse the JSON data into a Python dictionary
training_session = json.loads(training_session_json)

# Accessing individual elements
name = training_session["name"]
date = training_session["date"]
completed = training_session["completed"]
instructor_name = training_session["instructor"]["name"]
instructor_website = training_session["instructor"]["website"]
participants = training_session["participants"]

# Printing the extracted information
print("Training Session Name:", name)
print("Date:", date)
print("Completed:", completed)
print("Instructor Name:", instructor_name)
print("Instructor Website:", instructor_website)
print("Participants:")
for participant in participants:
    print("Name:", participant["name"])
    print("Email:", participant["email"])
