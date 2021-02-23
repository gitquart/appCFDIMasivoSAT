from cfdiclient import Autenticacion,Fiel,SolicitaDescarga,VerificaSolicitudDescarga,DescargaMasiva 
import os
import base64
import zipfile
from xml.etree import ElementTree as ET
import openpyxl as excelpy
from InternalControl import cInternalControl

#Important information for this code
#--------------------------------------------------------------------------
#Folder and file names: RFC_TIPO_FECHAS_ID
#lsFolder elements (by order):[rfc_solicitante,tipo,fechaCompleta,fileName] 



objControl=cInternalControl()
#They are filled wit datos.text
rfcFromFile=''
FIEL_PAS = ''
rfc_emisor= ''
rfc_receptor=''
rfc_solicitante=''
#End-They are filled wit datos.text
FIEL_KEY = ''
FIEL_CER = ''
fiel=''
 

def validateFIELFiles(directory):
    global rfcFromFile,rfc_emisor,rfc_receptor,rfc_solicitante,fiel,FIEL_CER,FIEL_KEY,FIEL_PAS
    numFiles=len(os.listdir(directory))
    for file in os.listdir(directory):
        if file == "datos.txt":
            datostxt = open(directory+'/datos.txt', 'r')
            Lines = datostxt.readlines()
            count=1
            for line in Lines:
                if line!="\n":
                    if count==1:
                        rfcFromFile=line.strip()
                        rfc_emisor= rfcFromFile
                        rfc_receptor=rfcFromFile
                        rfc_solicitante=rfcFromFile
                        count+=1
                        continue
                    if count==2:    
                        FIEL_PAS=line.strip()
                        break

        if file.endswith('.key'):
            FIEL_KEY=file
            continue
        if file.endswith('.cer'):
            FIEL_CER=file
            continue 
    if FIEL_CER!='' and FIEL_KEY!='':    
        cer_der = open(directory+'/'+FIEL_CER, 'rb').read()
        key_der = open(directory+'/'+FIEL_KEY, 'rb').read()  
        fiel = Fiel(cer_der, key_der, FIEL_PAS)
    
    return numFiles

   
def autenticacion():
    auth = Autenticacion(fiel)
    token = auth.obtener_token()

    return token

def solicitaDescarga(fecha_inicial,fecha_final,directory,tipo,fechaCompleta):
    #Ejemplo de respuesta  {'mensaje': 'Solicitud Aceptada', 'cod_estatus': '5000', 'id_solicitud': 'be2a3e76-684f-416a-afdf-0f9378c346be'}
    res=validateFIELFiles(directory)
    if res>0:
        lsfolderName=[]
        lsfolderName.append(rfc_solicitante)
        lsfolderName.append(tipo)
        lsfolderName.append(fechaCompleta)
        descarga = SolicitaDescarga(fiel)
        token = autenticacion()
        result=''
        if lsfolderName[1]=='Emisor':
            # Emitidos
            result = descarga.solicitar_descarga(token, rfc_solicitante, fecha_inicial, fecha_final, rfc_emisor=rfc_emisor)
        else:    
            # Recibidos
            result = descarga.solicitar_descarga(token, rfc_solicitante, fecha_inicial, fecha_final, rfc_receptor=rfc_receptor)
        
        res=verificaSolicitudDescarga(result['id_solicitud'],directory,lsfolderName)
        return res
        
    else:
        return [0,"El directorio no contiene archivos FIEL"]   


def verificaSolicitudDescarga(id_solicitud,directory,lsFolderName):
    if id_solicitud!='':
        #Ejemplo re respuesta  {'estado_solicitud': '3', 'numero_cfdis': '8', 'cod_estatus': '5000', 'paquetes': ['a4897f62-a279-4f52-bc35-03bde4081627_01'], 'codigo_estado_solicitud': '5000', 'mensaje': 'Solicitud Aceptada'}   
        v_descarga = VerificaSolicitudDescarga(fiel)
        token = autenticacion()
        result = v_descarga.verificar_descarga(token, rfc_solicitante, id_solicitud)
        if (int(result['numero_cfdis'])>0):
            lsFolderName.append(result['paquetes'][0])
            res=descargarPaquete(result['paquetes'],directory,lsFolderName)
            if int(res[0])==1:
                return [1,'Procesamiento exitoso, el resultado se descargó en '+directory+'/'+result['paquetes'][0]+' (zip y xlsx) ']
            else:
                return res    
        else:
            return [0,'El paquete no trae CFDI']  
    else:
        return [0,'No se encontró Solicitud'] 


def descargarPaquete(id_paquete,directory,lsFolderName):
    #ejemplo de respuesta # {'cod_estatus': '', 'mensaje': '', 'paquete_b64': 'eyJhbG=='} 
    descarga = DescargaMasiva(fiel)
    token = autenticacion()
    result = descarga.descargar_paquete(token, rfc_solicitante, id_paquete[0])
    paquete=result['paquete_b64']
    if paquete is not None:
        #if paquete is not None, the create the folder where zip and xls will be saved
        folderAndFileName='_'.join(lsFolderName)
        ZipExcelDir=directory+'/'+folderAndFileName
        if not os.path.isdir(ZipExcelDir):
            os.mkdir(ZipExcelDir)
        readBase64FromZIP(paquete,folderAndFileName,ZipExcelDir)
        extractAndReadZIP(ZipExcelDir,folderAndFileName+'.zip',rfc_solicitante)
        return [1]
    else:
        return [0,'No se descargó CFDI: '+result['mensaje']]



"""
readBase64FromZIP: Reads the package in base64 from SAT and returns the zip file (the zip file is actually)
created on the go.
"""
def readBase64FromZIP(file,folderAndFileName,directory): 
    if file is not None:
        with open(directory+'/'+folderAndFileName+'.zip', 'wb') as result:
            result.write(base64.b64decode(file))
        zip_ref = zipfile.ZipFile(directory+'/'+folderAndFileName+'.zip', 'r')
        zip_ref.close()


def extractAndReadZIP(directory,zipToRead,rfc_solicitante):
    objControl=cInternalControl()
    #Change / to \\ if neccesary
    myZip=zipfile.ZipFile(directory+'/'+zipToRead,'r')
    #The zip's file name will be the name of excel file name, like the "Database"
    excel_fileName=os.path.splitext(os.path.split(myZip.filename)[1])[0]+'.xlsx'
    #Creating the workbook (database)
    #Create the sheets: Ingreso_Egreso,Pago,Resto
    wb=excelpy.Workbook() 
    wb.create_sheet('Emisor')
    wb.create_sheet('Receptor')
    pago_sheet = wb['Sheet']
    pago_sheet.title = 'Pago'
    wb.save(directory+'/'+excel_fileName)
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
    #Add extra fields here
    lsFields.append('mes')
    lsSource=[]
    if len(objControl.lsCustomFields)==0:
        lsSource=dicTableFields   
    else:
        lsSource=objControl.lsCustomFields    

    #I append insetad of just assign the list, because I need the column "mes" in the very beginning
    for field in lsSource:
        lsFields.append(field)

    for field in objControl.lsRemove:
        if field in lsFields:
            lsFields.remove(field)     

    for sheet in wb.sheetnames:
        wb[sheet].append(lsFields)  
    #Rename columns in excel if necessary
    #As the excel doesn't have values but the header row, then don't need to add any more logic
    #Rename the columns you want and that's it.
    """
    for sheet in wb.sheetnames:
        for row in wb[sheet].rows:
            for cell in row:
                #Rename any column you want here
    """            


    wb.save(directory+'/'+excel_fileName)     
               
  
    #Third, read information and insert where belongs 
    #Conclusiones: 
    # getroot() : Gets the root of the xml, then use getRoot to get "Comprobante"
    # root.find(.//...): gets any node inside the root, use this to any other node except the root
    for xml in myZip.namelist():
        #Get field TipoDeComprobante to knwo where sheet to print
        #"Resto" is the default spread sheet
        doc_xml=myZip.open(xml)
        root = ET.parse(doc_xml).getroot()
        lsRfcTable=['Emisor','Receptor']
        for item in lsRfcTable:
            node=returnFoundNode(root,item)
            if len(node)>0:
                rfc_value=node[0].get('Rfc')
                if rfc_value==rfc_solicitante:
                    if root.get('TipoDeComprobante')=='I' or root.get('TipoDeComprobante')=='E':
                        sheetPrint=item
                    elif  root.get('TipoDeComprobante')=='P':
                        sheetPrint='Pago' 
                    else:
                        sheetPrint='Pago'
                    break         

        #Start to read the fields from lsFields=[]
        #Example of a field in lsFields : "Comprobante_Version" -> "tableName_Field"
        #One row per xml
        lsRow=[]
        #The field leads all the insertion
        #Algorith of reading fields
        for field in lsFields:
            #Cases
            if field=='mes':
                fechaFactura=root.get('Fecha')
                monthWord=returnMonthWord(int(fechaFactura.split('-')[1]))
                lsRow.append(monthWord)
                continue
            #Rest of cases
            chunks=field.split('_')
            table=chunks[0]
            column=chunks[1]
            if table=='Comprobante':  
                addColumnIfFound(root,column,lsRow,0)  
            else:
                #Find the right prefix for table
                lsNode=returnFoundNode(root,table)
                if len(lsNode)==1:
                    addColumnIfFound(lsNode[0],column,lsRow,0)
                elif len(lsNode)>1:
                    #More than 1 table_column found with the same name in XML
                    for node in root.findall('.//'+objControl.prefixCFDI+table):
                        if len(node.attrib)>0: 
                            #If this table has attributes, read it, other wise skip it becase
                            #if the column doesn't have fields, it means it holds children
                            addColumnIfFound(node,column,lsRow,0)
                else:
                    #No table name found
                    lsRow.append(0)  
            #End of field iteration

        #Append the whole xml in a single row            
        wb[sheetPrint].append(lsRow)                 
        contDocs+=1
        #End of each document (xml) iteration in a zip
        wb.save(directory+'/'+excel_fileName)

    #All xml processed at this point    
    print('Files processed in ZIP file:',str(contDocs)) 


def addColumnIfFound(table,column,lsRow,notFoundValue):
    if column in table.attrib:
        #Add all cases here
        if (column=='SubTotal' or column=='TotalImpuestosRetenidos' or
            column=='TotalImpuestosTrasladados' or column=='Total'):
            #Condition if the value is null, then add 0.0
            if (table.get(column)!=""):
                lsRow.append(float(table.get(column)))
            else:
                lsRow.append(0)

        else:
            #No special case or string case
            lsRow.append(table.get(column))


    else:
        #Table found, but no column found
        lsRow.append(notFoundValue)    

#returnFoundNode: regresa nodo (tabla) si existe en en XML
def returnFoundNode(root,table):
    lsNode=[]
    result=[]
    for prefix in objControl.lsPrefix:
        lsNode=root.findall('.//'+prefix+table) 
        if len(lsNode)>0:
            result=lsNode
            break
    #If the code reaches this point, it means the Node doesn't exit in the XML, therefore return an empty list
    return result  

def returnMonthWord(monthNumber):
    monthWord=''
    if monthNumber==1:
        monthWord='Enero'
    if monthNumber==2:
        monthWord='Febrero'
    if monthNumber==3:
        monthWord='Marzo'
    if monthNumber==4:
        monthWord='Abril'
    if monthNumber==5:
        monthWord='Mayo'
    if monthNumber==6:
        monthWord='Junio'         
    if monthNumber==7:
        monthWord='Julio'
    if monthNumber==8:
        monthWord='Agosto'
    if monthNumber==9:
        monthWord='Septiembre'  
    if monthNumber==10:
        monthWord='Octubre'
    if monthNumber==11:
        monthWord='Noviembre'
    if monthNumber==12:
        monthWord='Diciembre'                                     

    return monthWord       

        
          
             
    
    


    
        


   
    


