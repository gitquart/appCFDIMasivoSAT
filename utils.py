from cfdiclient import Autenticacion
from cfdiclient import Fiel
from cfdiclient import SolicitaDescarga
import datetime

import os

FIEL_KEY = ''
FIEL_CER = ''
FIEL_PAS = 'chuy1987'
pathToFiel=os.getcwd()+'\\FIEL'
for file in os.listdir(pathToFiel):
    if file.endswith('.key'):
        FIEL_KEY=file
        continue
    if file.endswith('.cer'):
        FIEL_CER=file
        continue 
cer_der = open(pathToFiel+'\\'+FIEL_CER, 'rb').read()
key_der = open(pathToFiel+'\\'+FIEL_KEY, 'rb').read()        

def autenticacion():
    
    fiel = Fiel(cer_der, key_der, FIEL_PAS)
    auth = Autenticacion(fiel)
    token = auth.obtener_token()

    return token

def solicitaDescarga():
    
    fiel = Fiel(cer_der, key_der, FIEL_PAS)
    descarga = SolicitaDescarga(fiel)

    token = autenticacion()
    rfc_solicitante = 'XAXX010101000'
    fecha_inicial = datetime.datetime(2018, 1, 1)
    fecha_final = datetime.datetime(2018, 12, 31)
    rfc_emisor = 'XAXX010101000'
    rfc_receptor = 'XAXX010101000'
    # Emitidos
    result = descarga.solicitar_descarga(token, rfc_solicitante, fecha_inicial, fecha_final, rfc_emisor=rfc_emisor)
    print(result)
    # Recibidos
    result = descarga.solicitar_descarga(token, rfc_solicitante, fecha_inicial, fecha_final, rfc_receptor=rfc_receptor)
    print(result)


