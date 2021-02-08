class cInternalControl:
    excel_dir='' 
    prefixCFDI='{http://www.sat.gob.mx/cfd/3}'
    prefixXSI='{http://www.w3.org/2001/XMLSchema-instance}'
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
             'TimbreFiscalDigital_FechaTimbrado'
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

    
