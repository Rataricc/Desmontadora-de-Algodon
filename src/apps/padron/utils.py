#from operator import ne
import secrets
#from django.db import models




def custom_id(): 
    return secrets.randbelow(10000)

"""
class Numero_LoteCustom(models.BigIntegerField): 
    
    def db_type(self): 
        return 'integer(5) UNSIGNED AUTO_INCREMENT PRIMARY KEY'

    def rel_db_type(self): 
        return 'integer(5) UNSIGNED'
"""