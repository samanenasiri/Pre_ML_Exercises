
import re    
class Account:
    def __init__(self,username,password,phone_number,Email):
        self.username=Account.get_username(username)
        self.password=Account.get_password(password)
        self.phone_number=Account.get_phone_number(phone_number)
        self.Email=Account.get_Email(Email)
    @classmethod
    def get_username(cls):
        if not re.match("^\w+_\w+$", cls.username):
            raise Exception('invalid username')
        return cls.username     
    @classmethod
    def get_password(cls):
        if not re.match("^.*(?=.{8,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=]).*$",cls.password):
            raise Exception('invalid password')  
        return cls.password 
    @classmethod
    def get_phone_number(cls):
        if not re.search("09(1[0-9]|3[1-9]|2[1-9])-?[0-9]{3}-?[0-9]{4}", cls.phone_number):
            raise Exception('invalid phone number')
        return cls.phone_number

    @classmethod
    def get_Email(cls):
        if not re.match("[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}", cls.Email):
            raise Exception('invalid Email')
        return cls.Email





class Site:
    def __init__(self,register_users,url,active_users):
        self.url=url
        self.register_users=[]
        self.active_users=[]
    def register(self,username):
        if username in self.register_users :
            raise Exception('user already registered')
        else:
            self.register_users.append(username)
            raise Exception('register successful')
    
    def logout(self,username):
        if username in self.register_users :
            self.active_users.remove(username)
            raise Exception('log out successful')
        else:
            raise Exception('user not logged in.')



    def login(self,password,*args):
        pass

