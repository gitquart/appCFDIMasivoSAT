/*Crear tabla de usuario*/

CREATE TABLE usuario (
        ID SERIAL primary key,
        rfc_solicitante varchar(80)
);


/*Crear tabla de solicitud*/

CREATE TABLE solicitud (
        ID SERIAL primary key,
        fechainicio date,
        fechafin date,
        conteo int,
        tipo varchar(10),
        id_usuario int references usuario (ID)
);

/*date postgresql yyyy-mm-dd*/



/*Crear tabla de emisor, receptor y pago (las 3 tienes los mismos campos) */

CREATE table pago  (
        ID SERIAL primary key,
        nombrearchivo text,
        mes varchar(20),
        comprobante_fecha varchar(50),
        comprobante_serie varchar (20),
        comprobante_folio varchar (50),
        comprobante_metodopago varchar (10),
        comprobante_tipodecomprobante varchar(10),
        receptor_usocfdi varchar(10),
        comprobante_subtotal float,
        impuestos_totalimpuestosretenidos float,
        impuestos_totalimpuestostrasladados float,
        comprobante_total float,
        comprobante_lugarexpedicion varchar(20),
        comprobante_moneda varchar(20),
        comprobante_tipoCambio varchar(10),
        comprobante_descuento float,
        comprobante_formapago varchar(10),
        comprobante_condicionesdepago varchar(100),
        comprobante_version varchar(10),
        emisor_rfc varchar(30),
        receptor_rfc varchar(30),
        emisor_nombre text,
        receptor_nombre text,
        timbrefiscaldigital_uuid text,
        id_solicitud int references solicitud (ID)
);

/*Transacciones y consultas*/

/*SELECT*/
select * from solicitud;
select * from usuario;
select * from pago;
select * from emisor;
select * from receptor;
/*ALTER SEQUENCE <table>_<field>_seq RESTART;*/
ALTER SEQUENCE pago_id_seq RESTART;