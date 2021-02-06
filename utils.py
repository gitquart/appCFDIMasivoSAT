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
import openpyxl as excelpy
from lxml import etree 

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
    directory='C:\\Users\\1098350515\\Documents\\'
    myZip=zipfile.ZipFile(directory+'testZIP\\EC162D98-292A-4673-8085-A1D2CFD725F8_01.zip','r')
    #The zip's file name will be the name of excel file name, like the "Database"
    excel_fileName=os.path.splitext(os.path.split(myZip.filename)[1])[0]+'.xlsx'
    #Creating the workbook (database)
    #Create the sheets: Ingreso_Egreso,Pago,Resto
    wb=excelpy.Workbook() 
    wb.create_sheet('Ingreso_Egreso')
    wb.create_sheet('Pago')
    resto_sheet = wb['Sheet']
    resto_sheet.title = 'Resto'
    wb.save(directory+excel_fileName)
    contDocs=0
    #dicTableFields is a dictionary with the following structura key:table, value: list of fields
    dicTableFields={}
    #Dictionaries for every kind of "tipo de comprobante"
    #First, get all the columns for all the tables
    for xml in myZip.namelist():
        chunkName=xml.split('.')
        fileName=chunkName[0]
        doc_xml=myZip.open(xml)
        root = ET.parse(doc_xml).getroot()
        for node in root.iter():
            #Column = attribute , Node= Table
            #Get attributes (columns) of current Node (table) 
            #Split the node (table) name because all come as "{something}Node" and {content} is not needed
            #If the number of nodes > 1 then not get its fields, we only want 1 row
            chunk=str(node.tag).split('}')
            tableName=chunk[1] 
            numOfNodes=len(node.getchildren())
            if (numOfNodes<2) or (numOfNodes>1 and tableName=='Comprobante'):
                chunk=str(node.tag).split('}')
                tableName=chunk[1]  
                #As all the fields will be in one single sheet, it can occur two fields with the same
                #name ex: Rfc and Rfc (Emisor and recipient), then it's needed to add prefix tableName
                for attr in node.attrib:
                    fieldName=tableName+'_'+attr
                    if tableName not in dicTableFields:
                        dicTableFields[tableName]=[fieldName]
                    else:
                        if fieldName not in dicTableFields[tableName]:
                            dicTableFields[tableName].append(fieldName)            
            #End of node iteration 

    #Second, when got all fields from all xml, print them in spread sheet
    lsFields=[] 
    #I add the ID (xlm name)
    lsFields.append('ID')
    for key in dicTableFields:
        for val in dicTableFields[key]:
            lsFields.append(val)
    #Test: remove fields that may be noisy (or any field you want)
    lsRemove=['Comprobante_{http://www.w3.org/2001/XMLSchema-instance}schemaLocation',
             'TimbreFiscalDigital_{http://www.w3.org/2001/XMLSchema-instance}schemaLocation',
             'TimbreFiscalDigital_UUID',
             'TimbreFiscalDigital_Version',
             'TimbreFiscalDigital_SelloCFD',
             'TimbreFiscalDigital_NoCertificadoSAT',
             'TimbreFiscalDigital_SelloSAT',
             'Traslado_Base',
             'Traslado_Impuesto',
             'Traslado_TipoFactor',
             'Traslado_TasaOCuota',
             'Traslado_Importe' ] 
    for field in lsRemove:
        lsFields.remove(field)     

    for sheet in wb.sheetnames:
        wb[sheet].append(lsFields)
    wb.save(directory+excel_fileName)     
               
  
    #Third, read information and insert where belongs  
    for xml in myZip.namelist():
        #Get field TipoDeComprobante to knwo where sheet to print
        #"Resto" is the default spread sheet
        sheetPrint='Resto'
        doc_xml=myZip.open(xml)
        root = ET.parse(doc_xml).getroot()
        for node in root.iter():
            if node.get('TipoDeComprobante')=='I' or node.get('TipoDeComprobante')=='E':
                sheetPrint='Ingreso_Egreso'
                break
            elif  node.get('TipoDeComprobante')=='P':
                sheetPrint='Pago'
                break
        #End of TipoComprobante iteration        

        #Start to read the fields from lsFields=[]
        #Example of a field in lsFields : "Comprobante_Version" -> "tableName_Field"
        #One row per xml
        lsRow=[]
        #The field leads all the insertion
        #bFieldAddedToRow is a flag to know if the field has been proccesed, it might be found in xml or not
        bFieldAddedToRow=False
        bNotFoundInXmlYet=False
        tableName=''
        #Notes about "Algorith of reading fields": It's working well as it is, but is printing TotalFields-1, don't know why
        #Algorith of reading fields
        for field in lsFields:
            if field=='ID':
                lsRow.append(xml)
                continue
            #Look for the "field" all over the xml
            for node in root.getiterator():
                if bFieldAddedToRow:
                    bFieldAddedToRow=False
                    break
                chunk=str(node.tag).split('}')
                tableName=chunk[1]       
                for attr in node.attrib:
                    bFieldAddedToRow=False
                    fieldName=tableName+'_'+attr
                    if fieldName==field:
                        #Current "Field" found in the xml, add to Row , break and look for next "Field"
                        lsRow.append(node.get(attr)) 
                        bFieldAddedToRow=True
                        bNotFoundInXmlYet=False  
                        break
                    else:
                        bNotFoundInXmlYet=True
            if bNotFoundInXmlYet:
                lsRow.append('Sin valor')
                bFieldAddedToRow=False 
                bNotFoundInXmlYet=False
    

                #End of node iteration 
            #End of fiel iteration

        #Append the whole xml in a single row            
        wb[sheetPrint].append(lsRow)                 
        contDocs+=1
        #End of each document (xml) iteration in a zip
        wb.save(directory+excel_fileName)

    #All xml processed at this point    
    print('Files processed in ZIP file:',str(contDocs))   
        
          
             
    
    


    
        


   
    


