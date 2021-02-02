#Tutorial de descarga CFDI masivamente : https://pypi.org/project/cfdiclient/
import utils as tool
import datetime


#Solicitar,Verificar,Descargar
op='descargar'

if op=='solicitar':
    print('Solicitar...')
    fecha_inicial = datetime.datetime(2019, 6, 1)
    fecha_final = datetime.datetime(2020, 12, 31)
    lsvalor=tool.solicitaDescarga(fecha_inicial,fecha_final)
if op=='verificar':    
    print('Verificar...')
    lsvalor=tool.verificaSolicitudDescarga('ec162d98-292a-4673-8085-a1d2cfd725f8')
if op=='solicitar' or op=='verificar':
    for item in lsvalor:
        print(item)

if op=='descargar':
    paquete=tool.descargarPaquete('EC162D98-292A-4673-8085-A1D2CFD725F8_01')
    print('ZIP is ready')
  

