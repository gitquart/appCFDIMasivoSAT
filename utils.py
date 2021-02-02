from cfdiclient import Autenticacion
from cfdiclient import Fiel
from cfdiclient import SolicitaDescarga
from cfdiclient import VerificaSolicitudDescarga
from cfdiclient import DescargaMasiva
import os
import json
import base64
import zipfile
from xml.dom import minidom
import pandas as pd


FIEL_KEY = ''
FIEL_CER = ''
FIEL_PAS = 'chuy1987'
rfc_solicitante = 'QCG190521ND3'
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
fiel = Fiel(cer_der, key_der, FIEL_PAS)      

def autenticacion():
    auth = Autenticacion(fiel)
    token = auth.obtener_token()

    return token

def solicitaDescarga(fecha_inicial,fecha_final):
    #Ejemplo de respuesta  {'mensaje': 'Solicitud Aceptada', 'cod_estatus': '5000', 'id_solicitud': 'be2a3e76-684f-416a-afdf-0f9378c346be'}
    descarga = SolicitaDescarga(fiel)
    token = autenticacion()
    rfc_emisor = 'QCG190521ND3'
    rfc_receptor = 'QCG190521ND3'
    # Emitidos
    result = descarga.solicitar_descarga(token, rfc_solicitante, fecha_inicial, fecha_final, rfc_emisor=rfc_emisor)
    id_solicitud_emisor=result['id_solicitud']
    # Recibidos
    result = descarga.solicitar_descarga(token, rfc_solicitante, fecha_inicial, fecha_final, rfc_receptor=rfc_receptor)
    id_solicitud_receptor=result['id_solicitud']
    lsSolicitud=[id_solicitud_emisor,id_solicitud_receptor]

    return lsSolicitud


def verificaSolicitudDescarga(id_solicitud):
    #Ejemplo re respuesta  {'estado_solicitud': '3', 'numero_cfdis': '8', 'cod_estatus': '5000', 'paquetes': ['a4897f62-a279-4f52-bc35-03bde4081627_01'], 'codigo_estado_solicitud': '5000', 'mensaje': 'Solicitud Aceptada'}   
    v_descarga = VerificaSolicitudDescarga(fiel)
    token = autenticacion()
    result = v_descarga.verificar_descarga(token, rfc_solicitante, id_solicitud)
    lsPaquete=[result['paquetes']]

    return lsPaquete

def descargarPaquete(id_paquete):
    #ejemplo de respuesta # {'cod_estatus': '', 'mensaje': '', 'paquete_b64': 'eyJhbG=='} 
    descarga = DescargaMasiva(fiel)
    token = autenticacion()
    result = descarga.descargar_paquete(token, rfc_solicitante, id_paquete)
    paquete=result['paquete_b64']
    data = readBase64FromZIP(paquete)
    
    return data
   

"""
readBase64FromZIP: Reads the package in base64 from SAT and returns the zip file (the zip file is actually)
created on the go.
"""
def readBase64FromZIP(file): 
    if file is not None:
        with open(file+'.zip', 'wb') as result:
            result.write(base64.b64decode(file))
        zip_ref = zipfile.ZipFile(file+".zip", 'r')
        zip_ref.close()
    else:
        extractAndReadZIP()
        print('No file found')    

def extractAndReadZIP():
    directory='C:\\Users\\1098350515\\Documents\\testZIP\\EC162D98-292A-4673-8085-A1D2CFD725F8_01.zip'
    myZip=zipfile.ZipFile(directory,'r')
    lsComprobante=['Fecha','LugarExpedicion','Moneda','NoCertificado','SubTotal','TipoDeComprobante','Total']
    lsEmisor=['Nombre','RegimenFiscal','Rfc']
    lsReceptor=['Nombre','Rfc','UsoCFDI']
    lsConcepto=['Cantidad','ClaveProdServ','ClaveUnidad','Descripcion','Importe','ValorUnitario']
    #I add coumn ID in lsPago to relate Pago and its detail
    lsPago=['FechaPago','FormaDePagoP','MonedaP','Monto','ID']
    dfCfdi=pd.DataFrame(columns=lsColumns)
    for xml in myZip.namelist():
        doc_xml=myZip.open(xml)
        cfdi = minidom.parse(doc_xml)
        #Comprobante
        nodeComprobante=cfdi.getElementsByTagName('cfdi:Comprobante')
        for item in nodeComprobante:
            valor=item.getAttribute('Moneda')
        #Start reading fields

        #Renaming Columns
        dfCfdi.rename(columns={ dfCfdi.columns[1]: "your value" }, inplace = True)
        print('...')
  
             
    
    


    
        


   
    


