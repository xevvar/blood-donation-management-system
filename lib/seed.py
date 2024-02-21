from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from  models import Donor, Receiver

from faker import Faker
import random

if __name__ == '__main__':
    engine = create_engine('sqlite:///blood_donation.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    session.query(Donor).delete()
    session.query(Receiver).delete()

    blood_types = ['A-', 'A+', 'B-', 'B+', 'AB-', 'AB+', 'O-', 'O+']
    blood_type_requirements = ['A-', 'A+', 'B-', 'B+', 'AB-', 'AB+', 'O-', 'O+']

    fake = Faker()

    donors = []
    for i in range(15):
        donor = Donor(
            name=fake.name(),
            blood_type=random.choice(blood_types),
            allergies= 'NO',
            diseases='None',
            contact_number=fake.phone_number()
        )

        session.add(donor)
        session.commit()

        donors.append(donor)        

       

    receivers = []
    for i in range(5):
        receiver = Receiver(
            name=fake.name(),
            blood_type_requirement=random.choice(blood_type_requirements),
            contact_number=fake.phone_number()
        )

        session.add(receiver)
        session.commit()

        receivers.append(receiver)

    session.close() 