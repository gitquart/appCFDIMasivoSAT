#Tutorial de descarga CFDI masivamente : https://pypi.org/project/cfdiclient/
import utils as tool

"""
Solicitues de Descarga
9079e0a3-3ecc-4132-8818-383e5df99b44
cb75d5b5-d1fd-4fb0-892c-fd94aab56ce2

"""
#Solicitar,Verificar,Descargar
op='descargar'

if op=='solicitar':
    lsvalor=tool.solicitaDescarga()
if op=='verificar':    
    lsvalor=tool.verificaSolicitudDescarga('cb75d5b5-d1fd-4fb0-892c-fd94aab56ce2')
if op=='solicitar' or op=='verificar':
    for item in lsvalor:
        print(item)

if op=='descargar':
    paquete=tool.descargarPaquete('CB75D5B5-D1FD-4FB0-892C-FD94AAB56CE2_01')
    print('ZIP is ready')
  

