class Config:
    SECRET_KEY = 'root'
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:@localhost/crud_flask'
    HEMY_TRACK_MODIFICATIONS = False