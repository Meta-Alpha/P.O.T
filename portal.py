from werkzeug.security import generate_password_hash, check_password_hash
from portalvars import *

adminUserName = input("Enter the admin username that you want to use for the portal: ")
if len(list(db[adminCollection].find({"adminName":adminUserName}))) == 0:
    adminPwd = input("\nEnter the password: ")
    encryptedPassword = generate_password_hash(adminPwd)
    db[adminCollection].insert({"adminName": adminUserName,"adminPassword":encryptedPassword})
else:
    print("\nAdmin is already present")


#class Admin:

from app import app