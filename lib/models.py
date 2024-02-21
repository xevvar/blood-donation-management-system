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
    
    @staticmethod
    def delete_by_id(session, donor_id):
        
        donor = session.query(Donor).get(donor_id)
        if donor:
            session.delete(donor)
            session.commit()
            print(f"Donor with ID {donor_id} deleted successfully")
        else:
            print(f"Donor with ID {donor_id} not found")


class Receiver(Base):
    __tablename__ = 'receivers'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    blood_type_requirement = Column(String(3))
    contact_number = Column(Integer())

    donors = relationship("Donor", secondary=association_table, back_populates="receivers")

    def __repr__(self):
        return f"<Receiver(id={self.id}, name='{self.name}', blood_type_requirement='{self.blood_type_requirement}', contact_number='{self.contact_number}')>"
    
    
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
    
    