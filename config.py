class Config:
    # sqlite3
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///prema2.db'

    # local postgresql
    SQLALCHEMY_DATABASE_URI = "postgresql://iCompass_db:Prema143@database-1.cfsqyk4ui4co.ap-south-1.rds.amazonaws.com/initial_db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
