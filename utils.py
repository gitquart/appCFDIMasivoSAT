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
from InternalControl import cInternalControl

objControl=cInternalControl()
prefixCFDI='{http://www.sat.gob.mx/cfd/3}'
prefixXSI='{http://www.w3.org/2001/XMLSchema-instance}'
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
    myZip=zipfile.ZipFile(directory+'CFDI\\testZIP\\EC162D98-292A-4673-8085-A1D2CFD725F8_01.zip','r')
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
    #I add the ID (nombre archivo) (xlm name)
    lsFields.append('nombrearchivo')
    for key in dicTableFields:
        for val in dicTableFields[key]:
            lsFields.append(val)
    
    for field in objControl.lsRemove:
        lsFields.remove(field)     

    for sheet in wb.sheetnames:
        wb[sheet].append(lsFields)
    wb.save(directory+excel_fileName)     
               
  
    #Third, read information and insert where belongs 
    #Conclusiones: 
    # getroot() : Gets the root of the xml, then use getRoot to get "Comprobante"
    # root.find(.//...): gets any node inside the root, use this to any other node except the root
    for xml in myZip.namelist():
        #Get field TipoDeComprobante to knwo where sheet to print
        #"Resto" is the default spread sheet
        sheetPrint='Resto'
        doc_xml=myZip.open(xml)
        root = ET.parse(doc_xml).getroot()
        if root.get('TipoDeComprobante')=='I' or node.get('TipoDeComprobante')=='E':
            sheetPrint='Ingreso_Egreso'
        elif  root.get('TipoDeComprobante')=='P':
            sheetPrint='Pago'      

        #Start to read the fields from lsFields=[]
        #Example of a field in lsFields : "Comprobante_Version" -> "tableName_Field"
        #One row per xml
        lsRow=[]
        #The field leads all the insertion
        #Algorith of reading fields
        for field in lsFields:
            #ID case
            if field=='nombrearchivo':
                lsRow.append(xml)
                continue
            #Rest of cases
            chunks=field.split('_')
            table=chunks[0]
            column=chunks[1]
            if table=='Comprobante':
                lsRow.append(root.get(column))
            else:
                #All normal cases, but also set here special cases that are not Root
                currentNode=root.find('.//'+prefixCFDI+table)
                if currentNode is not None:
                    lsRow.append(currentNode.get(column))
                else:
                    lsRow.append('Sin valor')    
            #End of field iteration

        #Append the whole xml in a single row            
        wb[sheetPrint].append(lsRow)                 
        contDocs+=1
        #End of each document (xml) iteration in a zip
        wb.save(directory+excel_fileName)

    #All xml processed at this point    
    print('Files processed in ZIP file:',str(contDocs))   
        
          
             
    
    


    
        


   
    


