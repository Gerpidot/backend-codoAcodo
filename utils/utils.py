import re #para matchear strings lo uso en email validations

#Compara email enviado con un patron estandar de emails
def validar_email(email):
    patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    
    if re.match(patron, email):
        return True
    else:
        return False