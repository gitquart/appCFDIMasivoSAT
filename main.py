#Tutorial de descarga CFDI masivamente : https://pypi.org/project/cfdiclient/
import utils as tool

"""
Solicitues de Descarga

Agotadas
Enero a dic 2020
emisor:   332c9953-c899-4628-be96-6e57ef57867f
receptor: 88afce35-ffb3-4e75-91a5-08c1dadb3430

enero a dic 2020
emisor: 935d1fbb-6530-4945-86c9-d4bb1606e996
receptor: ac3646b9-c09f-43e4-bcb6-a16d1d9124ac

enero 2020
0668ebef-a669-4e62-a14a-b02a1649dfd1  paquete 0668EBEF-A669-4E62-A14A-B02A1649DFD1_01
f552e510-3838-4b29-87b2-1651318df7ae

9d6a20c1-012c-458d-89cb-010fdf1f8adc
e021df73-87a9-4be7-b336-571a2d31fedf

"""

#lsvalor=tool.solicitaDescarga()
#lsvalor=tool.verificaSolicitudDescarga('e021df73-87a9-4be7-b336-571a2d31fedf')
lsvalor=tool.descargarPaquete('E021DF73-87A9-4BE7-B336-571A2D31FEDF_01')
#for item in lsvalor:
    #print(item)

"""
f = open("archivo_decodificado.txt", "r") 
texto=f.read()
valor=str(texto).decode("utf-8")
"""   

