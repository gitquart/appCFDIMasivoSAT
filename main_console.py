#Tutorial de descarga CFDI masivamente : https://pypi.org/project/cfdiclient/
import utils as tool
import datetime
from InternalControl import cInternalControl
import pandas as pd
import openpyxl as excelpy
import os
import threading

objControl=cInternalControl()
#Solicitar,Verificar,Descargar
print('---------Menu--------')
print('1.Solicitar CFDI')
print('2.Verificar CFDI')
print('3.Descargar CFDI en ZIP')
print('4.Extraer ZIP')
print('5.Validar estado CFDI')
print('6. Extraer ZIP (Batch)')

op=input()
op=int(op)

if op==1:
    print('Solicitar...')
    #year, month, day
    fecha_inicial = datetime.datetime(2014, 1, 1)
    fecha_final = datetime.datetime(2014, 12, 31)
    lsvalor=tool.solicitaDescarga(fecha_inicial,fecha_final)
if op==2:    
    #ejemplo :ec162d98-292a-4673-8085-a1d2cfd725f8
    print('Introduce el ID a verificar:')
    strid_v=input()
    directory='C:\\Users\\1098350515\\Documents\\CFDI\\Claves_Johnson_wfmx801 - Johnson Controls BE Manufactura S de RL de CV'
    #lsValor=Regresa los ID o ID's de paquetes si es que hay
    lsvalor=tool.verificaSolicitudDescarga_Consola(strid_v,'JCB6805038G1',directory)
if op==1 or op==2:
    accion=''
    if op==1:
        accion='Solicitud'
    if op==2:
        accion='Verificación'    
    print('Imprimiendo IDs de ',accion)
    if len(lsvalor)==0:
        print('No hay paquetes / CFDI')
    else:    
        for item in lsvalor:
            print(item)

if op==3:
    print('Introduce el ID a descargar:')
    strid_d=input()
    res=tool.descargarPaquete(strid_d)
    print('ZIP is ready')
if op==4:
    print('Extraer ZIP')
    print('Choose a version 1.EXCEL 2.SQL')
    op=input()
    #Do not put \\ at the end of directory if console mode, the code will add it.
    directory='C:\\Users\\1098350515\\Desktop'
    zipFile='Condensado wfm 802 xml.zip'
    rfc='JCB021126K89'
    if int(op)==1:    
        tool.extractAndReadZIP(directory,zipFile,rfc,True)
    else:
        tool.extractAndReadZIP_SQL(directory,zipFile,rfc,True)
if op==5:
    print('Validate CFDI...') 
    directory='C:\\Users\\1098350515\\Desktop\\'
    excel_name='Consolidado_xml_enero_a_diciembre_2020_CIR0706145CA'
    excel=excel_name+'.xlsx'
    completePath=directory+excel
    excelDF=pd.DataFrame()
    lsSheetsToRead=['Emisor','Receptor']
    wb=excelpy.Workbook() 
    wb.save(directory+'/'+excel_name+'_withStatus.xlsx')
    for sheet in lsSheetsToRead:
        print('-------Reading ',sheet,'-----------')
        excelDF=pd.read_excel(completePath,sheet_name=sheet)
        #Create the excel file where the state with the rest of records will be printed
        lsFields=[]
        #Get columns from dataframe and print into excel
        for header in excelDF.columns:
            lsFields.append(header)
        #Add the status field 
        fieldEstado='Estado'   
        lsFields.append(fieldEstado)
        wb.create_sheet(sheet+'_estado')    
        wb[sheet+'_estado'].append(lsFields) 
        rowCount=0
        for index,row in excelDF.iterrows():
            lsRow=[]
            #Copy current values from spreadsheet
            for field in lsFields:
                if field!=fieldEstado:
                    lsRow.append(row[field])
            #ColumnHeaders: Emisor_Rfc,Receptor_Rfc,TimbreFiscalDigital_UUID,Comprobante_Total 
            res=tool.validaEstadoDocumento(row['Emisor_Rfc'],row['Receptor_Rfc'],row['TimbreFiscalDigital_UUID'],str(row['Comprobante_Total']))
            estadoValue=''
            estadoValue=res['estado']
            lsRow.append(estadoValue)
            wb[sheet+'_estado'].append(lsRow)
            rowCount+=1
            print(f'Processed {str(rowCount)} record(s).Estatus :{estadoValue}')

    #Save whole file    
    wb.save(directory+'/'+excel_name+'_withStatus.xlsx') 
if op==6:
    print('Extraer ZIP en BATCH ')
    print('Choose a version 1.EXCEL 2.SQL')
    op=input()
    #Do not put \\ at the end of directory if console mode, the code will add it.
    directory='C:\\Users\\1098350515\\Desktop\\condensado por mes 802\\2018'
    lszipFile=list()
    for file in os.listdir(directory):
        lszipFile.append(file)
    rfc='JCB021126K89'
    if int(op)==1:    
        lsThreads=[]
        #Start - Create threads Subprocess per month, per excel
        for zipFile in lszipFile:
            process=threading.Thread(target=tool.extractAndReadZIP_Batch,args=[directory,zipFile,rfc,True])
            lsThreads.append(process)

        for process in lsThreads:
            process.start()

        #Join() in another process because if not it won't be parallel
        for process in lsThreads:    
            process.join()

        #End - Create threads 
        print('All processes are ready!')    
    else:
        tool.extractAndReadZIP_SQL(directory,lszipFile,rfc,True)

           
    
  

