#Tutorial de descarga CFDI masivamente : https://pypi.org/project/cfdiclient/
import utils as tool
import datetime
from InternalControl import cInternalControl

objControl=cInternalControl()
#Solicitar,Verificar,Descargar
print('---------Menu--------')
print('1.Solicitar CFDI')
print('2.Verificar CFDI')
print('3.Descargar CFDI en ZIP')
print('4.Extraer ZIP')

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
    if int(op)==1:    
        tool.extractAndReadZIP('C:\\Users\\1098350515\\Desktop\\QCG190521ND3_Emisor_122021_2222021_D4B2864D-52E8-420C-B61F-C2ED5C98191F_01','QCG190521ND3_Emisor_122021_2222021_D4B2864D-52E8-420C-B61F-C2ED5C98191F_01.zip','QCG190521ND3')
    else:
        tool.extractAndReadZIP_SQL('C:\\Users\\1098350515\\Desktop\\QCG190521ND3_Receptor_112021_3012021_3E6B3DE6-3C2D-4633-B54E-0A5FC6C6D1B4_01','QCG190521ND3_Receptor_112021_3012021_3E6B3DE6-3C2D-4633-B54E-0A5FC6C6D1B4_01.zip','QCG190521ND3');    
    
  

