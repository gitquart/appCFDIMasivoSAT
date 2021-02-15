class cInternalControl:
    
    #----Data to change per user----
    #zipToRead is the name of zip that will be created from download
    #and also the one to read to transform to excel
    zipToRead='EC162D98-292A-4673-8085-A1D2CFD725F8_01.zip' 
    #----Program variables----
    prefixCFDI='{http://www.sat.gob.mx/cfd/3}'
    prefixXSI='{http://www.w3.org/2001/XMLSchema-instance}'
    prefixTFD='{http://www.sat.gob.mx/TimbreFiscalDigital}'
    lsPrefix=[prefixCFDI,prefixXSI,prefixTFD]
    #lsCustomFields has the list of fields that a user may want for himself
    #customizing the excel result, if it is empty, the code must display the normal set of fields
    lsCustomFields=[
        'Comprobante_Fecha',
        'Comprobante_Serie',
        'Comprobante_Folio',
        'Comprobante_MetodoPago',
        'Comprobante_TipoDeComprobante',
        'Receptor_UsoCFDI',
        'Comprobante_SubTotal',
        'Impuestos_TotalImpuestosRetenidos',
        'Impuestos_TotalImpuestosTrasladados',
        'Comprobante_Total',
        'Comprobante_LugarExpedicion',
        'Comprobante_Moneda',
        'Comprobante_TipoCambio',
        'Comprobante_Descuento',
        'Comprobante_FormaPago',
        'Comprobante_CondicionesDePago',
        'Comprobante_Version',
        'Emisor_Rfc',
        'Receptor_Rfc',
        'Emisor_Nombre',
        'Receptor_Nombre',
        'TimbreFiscalDigital_UUID'
    ]
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
             'Concepto_Descuento',
             #Emisor
             'Emisor_RegimenFiscal'
              ] 


    
