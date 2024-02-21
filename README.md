**BLOOD DONATION MANAGEMENT SYSTEM**

**Introduction**

This is a CLI application for blood donation management.

**Features**

Add Donors and their information,
Add Receivers and their information,
Search for a specific blood_type

**Setup Instructions**

Create a virtual environment: run pipenv install.

Activate the virtual environment: run pipenv shell.

Install dependencies: run pipenv install.

Run migrations: run alembic upgrade head.

**For Testing purposes and interaction with the CLI**

- navigate to the lib directory and run python debug.py

- To create donor: run Donor.create_donor(session) 

- To create receiver; run  Receiver.create_receiver(session)

- To search_donors_by_blood_type: run Receiver.search_donors_by_blood_type(session, <blood_type>)

- To get_all_donors: run Donor.get_all_donors(session)

- To get all receivers: run Receiver.get_all_receivers(session)

- To delete a donor: run Donor.delete_by_id(session, <donor_id>)

- To delete a receiver: run Receiver.delete_by_id(session, <receiver_id>)
  
**External Libraries**

Faker to populate data 

SQLAlchemy for database interaction.

Alembic for database migrations.

IPDB for debuging and testing
