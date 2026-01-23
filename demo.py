from us_visa.logger import  logging
from us_visa.exception import USVisaException
import sys
import os


#logging.info("Logging setup complete.")


# try:
#     r = 3/0
#     print(r)
# except Exception as e:
#     logging.info(e)
#     raise USVisaException(e,sys) 




monogodburl = os.getenv("MONGODB_URL")
print(monogodburl)