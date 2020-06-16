from . import db
from sqlalchemy.ext.automap import automap_base

Base = automap_base()
Base.prepare(db.engine,reflect=True)

Customers = Base.classes.customers
