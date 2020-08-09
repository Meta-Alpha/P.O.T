from pymongo import MongoClient

db = MongoClient("127.0.0.1", 27017, connect=False).pot
adminCollection = 'admin'
studentCollection = 'student'
teacherCollection = 'teacher'
