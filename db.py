from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker 


engine = create_engine('postgresql://postgres:root@127.0.0.1:5432/flassk')

Session = sessionmaker(bind=engine)
