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
from xml.etree import ElementTree as ET
import pandas as pd

#For practical purposes, each table or sheet in excel, will be managed by a dictionary (data) and a flag
dataIE={}
dataPago={}
dataMain={}
bIE=False
bPago=False
bMain=False
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


def dataToDataFrame(column,value,sheet_name):
    if sheet_name=='Ingresos_Egresos':
        #dataIE
        if column not in dataIE:
            dataIE[column]=[] 
        dataIE[column].append(value)   

    elif sheet_name=='Pago':
        #dataPago
        if column not in dataPago:
            dataPago[column]=[] 
        dataPago[column].append(value)    
    else:
        #dataMain - this is the default value  
        if column not in dataMain:
            dataMain[column]=[] 
        dataMain[column].append(value)  



def extractAndReadZIP():
    directory='C:\\Users\\1098350515\\Documents\\testZIP\\EC162D98-292A-4673-8085-A1D2CFD725F8_01.zip'
    myZip=zipfile.ZipFile(directory,'r')
    bIE=False
    bPago=False
    bMain=False
    dataIE.clear()
    dataPago.clear()
    dataMain.clear()
    contDocs=0
    #Dictionaries for every kind of "tipo de comprobante"
    for xml in myZip.namelist():
        #Each xml represent a row of dataframe (Serie)
        chunkName=xml.split('.')
        fileName=chunkName[0]
        doc_xml=myZip.open(xml)
        root = ET.parse(doc_xml).getroot()
        #Every column and serie will be appended this way
        sheet_name=''
        #Start reading fields
        #No hay un patrón específico
        #La única forma de estructurarlo es, si tiene hijos, en algún nodo hijo existe detalle
        for node in root.iter():

            #The only one FORCELY with children is Comprobante
            #Get the name of the node (it will be the prefix of each columns)
            #Column = attribute
            #Node= Table
            #root.iter() brings ALL the nodes in the xml file, ALL means even CHILDREN
            chunk=str(node.tag).split('}')
            tableName=chunk[1]
            #Get attributes of current Node (get columns of current table)
            for attr in node.attrib:
                dataToDataFrame(tableName+'_'+attr,node.get(attr),sheet_name)
                if attr=='TipoDeComprobante':
                    if node.get(attr)=='I' or node.get(attr)=='E':
                        sheet_name='Ingresos_Egresos'
                        bIE=True
                        break
                    elif node.get(attr)=='P' :
                        sheet_name='Pago'
                        bPago=True
                        break
                    else:
                        sheet_name='Main'
                        bMain=True
                        break
            #Adding ID        
            dataToDataFrame('ID',fileName,sheet_name)         
            #End of node iteration        
            
        contDocs+=1
    #End of the process of all xml in a zip
    writer = pd.ExcelWriter('C:\\Users\\1098350515\\Documents\\cfdi.xlsx', engine='xlsxwriter')
    if bIE:     
        dfCfdi=pd.DataFrame.from_dict(dataIE,orient='index')
        dfCfdiIE=dfCfdi.transpose()
        dfCfdiIE.to_excel(writer,sheet_name='Ingresos_Egresos')
    if bPago:     
        dfCfdi=pd.DataFrame.from_dict(dataPago,orient='index')
        dfCfdiPago=dfCfdi.transpose()
        dfCfdiPago.to_excel(writer,sheet_name='Pago')
    if bMain:     
        dfCfdi=pd.DataFrame.from_dict(dataMain,orient='index') 
        dfCfdi=dfCfdi.transpose()
        dfCfdiMain.to_excel(writer,sheet_name='Main')   

    writer.save() 
    print('Files processed in ZIP file:',str(contDocs))   
        
          
             
    
    


    
        


   
    


