class cInternalControl:
    excel_dir='' 
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
              #Traslado
             'Traslado_Base',
             'Traslado_Impuesto',
             'Traslado_TipoFactor',
             'Traslado_TasaOCuota',
             'Traslado_Importe'
             #DoctoRelacionado
             'DoctoRelacionado_ImpSaldoInsoluto',
             'DoctoRelacionado_ImpPagado',
             'DoctoRelacionado_ImpSaldoAnt',
             'DoctoRelacionado_NumParcialidad',
             'DoctoRelacionado_MetodoDePagoDR',
             'DoctoRelacionado_MonedaDR',
             'DoctoRelacionado_Folio'
              ] 

    
