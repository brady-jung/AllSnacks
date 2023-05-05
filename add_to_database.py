from database import init_db, db_session
from models import *


init_db()
#subjects that are available
snack1 = Snack("Doritos", 5, "/static/images/doritos.png")
snack2 = Snack("Lays", 4, "/static/images/lays.jpeg")
snack3 = Snack("Cheetos", 5, "/static/images/cheetos.webp")
db_session.add_all([snack1, snack2, snack3])
db_session.commit()

# test data to make sure relationships work
#db_session.add_all()
#db_session.commit()