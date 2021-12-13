from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, session
from sqlalchemy import Column, Integer, String
from sqlalchemy import Sequence
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql.schema import ForeignKey
Session = sessionmaker()
engine = create_engine('sqlite:///:memory:', echo=True)
Session.configure(bind=engine)
Base = declarative_base()

class User(Base):
     __tablename__ = 'users'

     id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
     name = Column(String)
     fullname = Column(String)
     nickname = Column(String)
     group_id=Column(Integer,ForeignKey("Group.id"))
     def __repr__(self):
        return "<User(name='%s', fullname='%s', nickname='%s')>" % (
                             self.name, self.fullname, self.nickname)
class Group(Base):
     __tablename__ = 'groups'

     id = Column(Integer, Sequence('group_id_seq'), primary_key=True)
     name = Column(String)

     def __repr__(self):
        return "<User(name='%s', fullname='%s', nickname='%s')>" % (
                             self.name, self.fullname, self.nickname)


Base.metadata.create_all(engine)
vip_group = User(name='vip')
ed_user = User(name='ed', fullname='Ed Jones', nickname='edsnickname')
session = Session()
session.add(ed_user)
session.rollback()  #Rollback of model
print ("Users: {}".format(session.query(User).all()))
session.add(ed_user)
session.commit()    #Commit changes in model into DB
print ("Users: {}".format(session.query(User).all()))
session.add_all([User(name='ed2', fullname='Ed Jones2', nickname='ed2snickname'),User(name='ed3', fullname='Ed Jones3', nickname='ed3snickname')])
session.commit()    #Commit changes in model into DB
print ("User nicknames: {}".format(session.query(User.nickname).first()))#Get first entry matching querry
