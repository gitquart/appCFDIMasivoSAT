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
print('4.Extraer ZIP en excel')

op=input()
op=int(op)

if op==1:
    print('Solicitar...')
    fecha_inicial = datetime.datetime(2019, 6, 1)
    fecha_final = datetime.datetime(2020, 12, 31)
    lsvalor=tool.solicitaDescarga(fecha_inicial,fecha_final)
if op==2:    
    print('Verificar...')
    lsvalor=tool.verificaSolicitudDescarga('ec162d98-292a-4673-8085-a1d2cfd725f8')
if op==1 or op==2:
    for item in lsvalor:
        print(item)

if op==3:
    res=tool.descargarPaquete('')
    print('ZIP is ready')
if op==4:    
    tool.extractAndReadZIP(objControl.zipToRead)
    
  

