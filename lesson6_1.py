import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("raspberrytest-b0d46-firebase-adminsdk-tm9y4-95d8b16bd2")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://raspberrytest-b0d46-default-rtdb.asia-southeast1.firebasedatabase.app/'
})
ref = db.reference('/')
print(ref.get())
