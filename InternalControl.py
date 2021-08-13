
class cInternalControl:
    
    #----Data to change per user----
    #zipToRead is the name of zip that will be created from download
    #and also the one to read to transform to excel
    #600 secs = 10 mins, 2400 secs= 40 mins
    TIME_REQUEST_MINS=8
    TIME_FOR_REQUEST=TIME_REQUEST_MINS*60
    testingMode=False
    THIS_SOFTWARE_VERSION='2.0'
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
        'Retencion_Impuesto',
        'Retencion_Importe',
        'Traslado_Impuesto',
        'Traslado_Importe',
        'Traslado_Tasa',
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
             'Traslado_TipoFactor',
             'Traslado_TasaOCuota',
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
             'Retencion_TasaOCuota',
             'Retencion_TipoFactor',
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
             #Campos de algunos clientes (Campos hasta ahora han sido personalizados)
             #'Retencion_Impuesto',
             #'Retencion_Importe',
             #'Traslado_Impuesto',
             #'Traslado_Importe',
             #'Traslado_Tasa'
              ] 


    
