from sqlalchemy import create_engine, Integer
from sqlalchemy import Column, String, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import func


class IssuesDb():
    def __init__(self, db_type, user_name, password, host, port, db_name):
        self.db_type   = db_type
        self.user_name = user_name
        self.password  = password
        self.host      = host
        self.port      = port
        self.db_name   = db_name
        self.initialize()

    base = declarative_base()

    def initialize(self):
        db_string = "{0}://{1}:{2}@{3}:{4}/{5}".format(self.db_type,
                                                       self.user_name,
                                                       self.password,
                                                       self.host,
                                                       self.port,
                                                       self.db_name)
        self.db = create_engine(db_string)
        self.Session = sessionmaker(self.db)

    def get_session(self):
        session = self.Session()
        return WrappedSession(session)

    def create_defined_tables(self):
        self.base.metadata.create_all(self.db)

    def add_issue(self, session, project, issue_number, link, status, creation_time, close_time, labels):
        issue = Issue(project=project,
                      issue_number=issue_number,
                      link=link,
                      status=status,
                      creation_time=creation_time,
                      close_time=close_time,
                      labels=labels)
        session.add(issue)

    def get_all_issues(self, session):
        query = session.query(Issue).all()
        return query

    def get_first_issue(self, session):
        query = session.query(Issue).first()
        return query

    def delete_issue(self, session, id):
        query = session.query(Issue).filter(Issue.id == id)
        return query.delete()

    def add_issue_file_change(self, session, issue_number, filename, good_code, bad_code):
        issue_file_change = IssueFileChange(issue_number=issue_number,
                                            filename=filename,
                                            good_code=good_code,
                                            bad_code=bad_code)
        session.add(issue_file_change)

    def get_all_issue_file_changes(self, session):
        query = session.query(IssueFileChange).all()
        return query

    def get_first_issue_file_change(self, session):
        query = session.query(IssueFileChange).first()
        return query

    def delete_issue_file_change(self, session, id):
        query = session.query(IssueFileChange).filter(IssueFileChange.id == id)
        return query.delete()

    def commit_session(self, session):
        session.commit()


class WrappedSession(object):
    def __init__(self, session):
        self.session = session

    def __getattr__(self, key):
        return getattr(self.session, key)

    def __enter__(self):
        return self.session

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.rollback()


class Issue(IssuesDb.base):
    __tablename__ = 'issues'

    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    project = Column(String)
    issue_number = Column(Integer)
    link = Column(String)
    status = Column(String)
    insertion_time = Column(DateTime(timezone=True), server_default=func.now())
    creation_time = Column(DateTime(timezone=True))
    close_time = Column(DateTime(timezone=True))
    labels = Column(String)


class IssueFileChange(IssuesDb.base):
    __tablename__ = 'issue_file_changes'

    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    issue_number = Column(Integer)
    filename = Column(String)
    good_code = Column(String)
    bad_code = Column(String)
    insertion_time = Column(DateTime(timezone=True), server_default=func.now())