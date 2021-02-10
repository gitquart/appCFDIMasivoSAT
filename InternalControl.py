class cInternalControl:
    
    #Data to change per user
    rfc_emisor = 'QCG190521ND3'
    rfc_receptor = 'QCG190521ND3'
    rfc_solicitante = 'QCG190521ND3'
    FIEL_PAS = 'chuy1987'

    #Progra, variables
    #Folder for extractAndReadZIP()
    directory='C:\\Users\\1098350515\\Documents\\'
    zipToRead='EC162D98-292A-4673-8085-A1D2CFD725F8_01.zip' 
    prefixCFDI='{http://www.sat.gob.mx/cfd/3}'
    prefixXSI='{http://www.w3.org/2001/XMLSchema-instance}'
    prefixTFD='{http://www.sat.gob.mx/TimbreFiscalDigital}'
    lsPrefix=[prefixCFDI,prefixXSI,prefixTFD]
    #Test: remove fields that may be noisy (or any field you want)
    lsRemove=[
               #Comprobante
              'Comprobante_'+prefixXSI+'schemaLocation',
              'Comprobante_Certificado',
              'Comprobante_NoCertificado',
              'Comprobante_Sello',
               #TimbreFiscalDigital
              'TimbreFiscalDigital_'+prefixXSI+'schemaLocation',
              'TimbreFiscalDigital_Version',
              'TimbreFiscalDigital_SelloCFD',
             'TimbreFiscalDigital_NoCertificadoSAT',
             'TimbreFiscalDigital_SelloSAT',
             'TimbreFiscalDigital_FechaTimbrado',
             'TimbreFiscalDigital_RfcProvCertif',
              #Traslado
             'Traslado_Base',
             'Traslado_Impuesto',
             'Traslado_TipoFactor',
             'Traslado_TasaOCuota',
             'Traslado_Importe',
             #DoctoRelacionado
             'DoctoRelacionado_ImpPagado',
             'DoctoRelacionado_ImpSaldoAnt',
             'DoctoRelacionado_NumParcialidad',
             'DoctoRelacionado_MetodoDePagoDR',
             'DoctoRelacionado_MonedaDR',
             'DoctoRelacionado_Folio',
             'DoctoRelacionado_ImpSaldoInsoluto',
             'DoctoRelacionado_Serie',
             'DoctoRelacionado_IdDocumento',
             #Pago
             'Pago_Monto',
             'Pago_MonedaP',
             'Pago_FormaDePagoP',
             'Pago_FechaPago',
             'Pagos_Version',
             #Retención
             'Retencion_Importe',
             'Retencion_TasaOCuota',
             'Retencion_TipoFactor',
             'Retencion_Impuesto',
             'Retencion_Base',
             #Concepto
             'Concepto_ClaveProdServ',
             'Concepto_Cantidad',
             'Concepto_ClaveUnidad',
             'Concepto_Descripcion',
             'Concepto_ValorUnitario',
             'Concepto_Importe',
             'Concepto_NoIdentificacion',
             'Concepto_Unidad',
             'Concepto_Descuento'

              ] 

    
