from .database import Base, engine


# create all table in the db
Base.metadata.create_all(engine)
