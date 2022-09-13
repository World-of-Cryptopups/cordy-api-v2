import os
from deta import Deta

deta = Deta(os.getenv("DETA_PROJECT_KEY"))

# base for only dps
dpsDB = deta.Base("DpsDB")

# base for users
usersDB = deta.Base("Users")
