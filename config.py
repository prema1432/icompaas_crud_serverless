class Config:
    # sqlite3
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///prema2.db'

    # local postgresql
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@localhost/icompass_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
