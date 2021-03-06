#Tutorial de descarga CFDI masivamente : https://pypi.org/project/cfdiclient/
import utils as tool
import datetime
from InternalControl import cInternalControl
import pandas as pd
import openpyxl as excelpy

objControl=cInternalControl()
#Solicitar,Verificar,Descargar
print('---------Menu--------')
print('1.Solicitar CFDI')
print('2.Verificar CFDI')
print('3.Descargar CFDI en ZIP')
print('4.Extraer ZIP')
print('5.Validar estado CFDI')

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
    lsvalor=tool.verificaSolicitudDescarga(strid_v)
if op==1 or op==2:
    accion=''
    if op==1:
        accion='Solicitud'
    if op==2:
        accion='Verificación'    
    print('Imprimiendo IDs de ',accion)
    for item in lsvalor:
        print(item)

if op==3:
    print('Introduce el ID a descargar:')
    strid_d=input()
    res=tool.descargarPaquete(strid_d)
    print('ZIP is ready')
if op==4:
    print('Choose a version 1.EXCEL 2.SQL')
    op=input()
    #Do not put \\ at the end of directory if console mode, the code will add it.
    directory='C:\\Users\\1098350515\\Desktop'
    zipFile='testing.zip'
    rfc='CIR0706145CA'
    if int(op)==1:    
        tool.extractAndReadZIP(directory,zipFile,rfc)
    else:
        tool.extractAndReadZIP_SQL(directory,zipFile,rfc)
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

           
    
  

