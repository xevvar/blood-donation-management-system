from sqlalchemy import create_engine
from sqlalchemy import ForeignKey, Table, Column, Integer, String, CheckConstraint
from sqlalchemy.orm import relationship, backref, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///blood_donation.db')

Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

association_table = Table('association', Base.metadata,
    Column('donor_id', Integer, ForeignKey('donors.id')),
    Column('receiver_id', Integer, ForeignKey('receivers.id'))
)

class Donor(Base):
    __tablename__ = 'donors'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    blood_type = Column(String(3))
    allergies = Column(String(3), CheckConstraint("allergies IN ('yes', 'no')"))
    diseases = Column(String(3), CheckConstraint("diseases IN ('yes', 'no')"))
    contact_number = Column(Integer())

    receivers = relationship("Receiver", secondary=association_table, back_populates="donors")

    def __repr__(self):
        return f"<Donor(id={self.id}, name='{self.name}', blood_type='{self.blood_type}', allergies='{self.allergies}', diseases='{self.diseases}', contact_number='{self.contact_number}')>"
    
    @classmethod
    def create_donor(cls, session):
    
        name = input("Enter donor's name: ")
        blood_type = input("Enter donor's blood type: ")
        allergies = input("Does the donor have allergies? (yes/no): ")
        diseases = input("Does the donor have diseases? (yes/no): ")
        contact_number = input("Enter donor's contact number: ")

        new_donor = Donor(name=name, blood_type=blood_type, allergies=allergies, diseases=diseases, contact_number=contact_number)

        session.add(new_donor)
        session.commit()

        print("New donor added successfully")
        return new_donor

    
    @staticmethod
    def delete_by_id(session, donor_id):
        
        donor = session.query(Donor).get(donor_id)
        if donor:
            session.delete(donor)
            session.commit()
            print(f"Donor with ID {donor_id} deleted successfully")
        else:
            print(f"Donor with ID {donor_id} not found")

    @classmethod
    def get_all_donors(cls, session):
        all_donors =  session.query(cls).all()
        if all_donors:
            print("All donors:")
            for donor in all_donors:
                print(donor)
        else:
            print("No donors found in the database")


class Receiver(Base):
    __tablename__ = 'receivers'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    blood_type_requirement = Column(String(3))
    contact_number = Column(Integer())

    donors = relationship("Donor", secondary=association_table, back_populates="receivers")

    def __repr__(self):
        return f"<Receiver(id={self.id}, name='{self.name}', blood_type_requirement='{self.blood_type_requirement}', contact_number='{self.contact_number}')>"
    
    
    @classmethod
    def create_receiver(cls, session):
    
        name = input("Enter receiver's name: ")
        blood_type_requirement = input("Enter receiver's blood type requirement: ")
        contact_number = input("Enter receiver's contact number: ")

        new_receiver = Receiver(name=name, blood_type_requirement=blood_type_requirement, contact_number=contact_number)

        session.add(new_receiver)
        session.commit()

        print("New receiver added successfully")
        return new_receiver

    
    
    @staticmethod
    def search_donors_by_blood_type(session, blood_type_requirement):

        donors = session.query(Donor).filter(Donor.blood_type == blood_type_requirement).all()
        if donors:
            print(f"Donors with blood type {blood_type_requirement}:")
            for donor in donors:
                print(f"Name: {donor.name}, Blood Type: {donor.blood_type}, Contact:{donor.contact_number}")
        else:
            print(f"No donors found with blood type {blood_type_requirement}")

    @staticmethod
    def delete_by_id(session, receiver_id):
        
        receiver = session.query(Receiver).get(receiver_id)
        if receiver:
            session.delete(receiver)
            session.commit()
            print(f"Receiver with ID {receiver_id} deleted successfully")
        else:
            print(f"Receiver with ID {receiver_id} not found")

    @classmethod
    def get_all_receivers(cls, session):
        all_receivers =  session.query(cls).all()
        if all_receivers:
            print("All receivers:")
            for receiver in all_receivers:
                print(receiver)
        else:
            print("No receivers found in the database")
    
    