from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Donor, Receiver

if __name__ == '__main__':
    
    engine = create_engine('sqlite:///blood_donation.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    import ipdb; ipdb.set_trace() 