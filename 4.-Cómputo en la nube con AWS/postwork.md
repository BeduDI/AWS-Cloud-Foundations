# Amazon Simple Storage Service (S3)
S3 es uno de los servicios icónicos de AWS. S3 lanzado en 2006 se ha convertido en el storage por excelencia a la hora de guardar archivos (objetos) a precios bajos con tiempos de acceso de milisegundos, el hecho de ser altamente resistente a pérdida de archivos ofreciendo un 99,999999999 % de durabilidad de datos (si se almacenan 10 000 objetos se espera una pérdida de un objeto cada 10 000 000 años) brinda mucha seguridad y confianza.
S3 cuenta con diferentes niveles de servicio y precios, hay tipos de storage mas baratos pero el tiempo de acceso a los datos es mayor, si se requiere acceso a datos en el orden de los milisegundos el storage tiende a ser mas costoso.
La forma de trabajar con S3 es por medio de `buckets`, los buckets son un contenedor de archivos u objetos, a cada bucket se le puede asignar un nombre único que no puede ser usado en ninguna otra región ni en ninguna otra cuenta de AWS, los buckets también pueden ser configurados con políticas de seguridad, aquí también es donde se especifica el nivel de storage a requerir y en consecuencia los costos que incurrirán.
Los casos de uso comunes para S3 incluyen backups por su porcentaje de durabilidad, datalakes por su capacidad de escalamiento de unos cuantos gigabytes a petabytes sin esfuerzo, como storage para datos no utilizados que se deben guardar por regulaciones y como web server.


# Hosting en Amazon S3
AWS S3 nos permite hospedar sitios web estáticos sin necesidad de instalar un servidor como Apache o Nginx para tal. 
La desventaja es que si se quiere usar un dominio propio (AWS brinda un dominio específico al habilitar un bucket como servidor de archivos) habrá que usar el servicio Cloud Front, y si hablamos de brindar soporte para el protocolo https tenemos que hacer en conjunto con Cloud Front uso de AWS Certificate Manager, el uso de Cloud Front incurre en costos extras a los de S3, hay que tomar en cuenta también que los buckets quedan expuestos al público por lo que se recomienda que los buckets configurados como web servers no tengan datos sensibles, los datos sensibles deberían manejarse en buckets totalmente privados. La gran ventaja de usar S3 como webserver es que no hay necesidad de preocuparse por la redundancia, disponibilidad, escalado, balanceo de carga, en general se puede ver como un PaaS para el hosting de sitios.

# Glacier Deep Archive
Es un tipo especial de storage de objetos muy económico, el precio se logra manteniendo los datos en una capa donde al requerir los objetos estos pueden tardar horas en estar listos antes de poderlos descargar. Hay que tener en cuenta la criticidad de la información y los RTO y RPO a la hora de seleccionar este tipo de storage, si nuestra organización requiere tiempos de recuperación (RTO) del orden de algunos minutos Glacier no es la opción para estos casos.

# Elastic Block Store
AWS Elastic Block Storage (EBS) es la solución de almacenamiento a nivel de bloque de Amazon usado con el servicio en la nube EC2 para almacenar datos persistentes. Significa que los datos se mantienen en los servidores AWS EBS incluso cuando las instancias de EC2 se apagan o terminan. EBS ofrece la misma alta disponibilidad y baja latencia rendimiento dentro de la zona de disponibilidad seleccionada permitiendo a los usuarios la capacidad de almacenamiento en la escala modelo de precios bajos basado en suscripción. Los volúmenes de datos se pueden unir de forma dinámica, separados y escalados con cualquier instancia de EC2, al igual que una unidad de almacenamiento de física en un servidor tradicional. Es un servicio en la nube altamente fiable, EBS garantiza la disponibilidad del 99,999%.
EBS representa diferentes escalas de costos, nos brinda General Purpose SSD, Provisioned IOPS SSD para cargas de trabajo demandantes, Throughput Optimized HDD para storage de bajo costo que no necesita velocidades altas  y Cold HDD si se requiere bajar los costos lo mas posible.
EBS cuenta con Snapshots o instantáneas. Esta función permite el almacenamiento de volúmenes de datos de forma incremental, mientras que solo se cobra por el cambio en el volumen de datos. Por ejemplo, si se agregaron 5 GB de datos a un bloque de almacenamiento de 100 GB existente con la instantánea, AWS solo cobrará por los 5 GB adicionales de datos. Las instantáneas se pueden expandir, replicar, mover, compartir, copiar, modificar, administrar y organizar dentro y entre las zonas de disponibilidad de AWS utilizando Amazon Data Lifecycle Manager y la función de etiquetas. Todas las instantáneas de EBS se almacenan en AWS S3 que garantizan hasta 99.999999999% de durabilidad. Las instantáneas no se almacenan como objetos accesibles para el usuario, sino a través de la API de EBS. Las instantáneas se almacenan detrás de las imágenes de máquina de Amazon (AMI), lo que proporciona toda la información necesaria para recuperar datos y lanzar instancias EC2 en la nube.
Los snapshots  es clave para los planes de continuidad de negocio para aplicaciones y servicios de misión crítica. Los administradores pueden definir los objetivos de tiempo de recuperación (RTO) y objetivos de punto de recuperación (RPO)  gestionando las instantáneas y servidores EC2 para cumplir con esos objetivos. Además de los objetivos de copia de seguridad de datos y recuperación de desastres, los administradores también utilizan instantáneas de EBS para replica de ambientes de pruebas y producción, de producción tomas una instantánea del ambiente, se renombra, se agrega a una nueva instancia EC2, la instancia se configura con sus política propias de networking y se tiene listo un servidor para desarrollo en minutos.


# Elastic File System
 Amazon EFS nos genera la posibilidad d de contar con un almacenamiento de alto rendimiento no conectado directamente al sistema operativo como es el caso de EBS si no nos conectaremos por medio del protocolo de red NFS , por si mismo NFS da la posibilidad de conectarse a un mismo EFS desde distintas instancias EC2 (escala de cientos o miles de ellas), EBS solo puede ser accedido desde la instancia a la que está asociada. EFS escala sin problemas hasta capacidades del orden de PetaBytes, el storage va creciendo a la par que nuestros datos y lo interesante es que igual se va reduciendo a  medida que eliminamos datos.
 EFS se integra con IAM para ofrecer una solución apegada a la seguridad empresarial, es posible configurar políticas de IAM que limiten los permisos con los que una instancia se conecta o forzarlos a conectarse solo si se cumplen condiciones como el cifrado, inclusive es posible administrar el acceso a un volumen EFS desde otras cuentas de AWS. AWS Key Management Se integra con EFS para brindar soporte a volúmenes cifrados. 
 Es posible establecer también un esquema híbrido entre las instalaciones e infraestructura local y EFS conectando a servidores locales un volumen EFS por medio de una AWS VPN. No solo se puede acceder a un volumen EFS desde instancias EC2, también se puede hacer desde AWS Lambdas, Elastic Container Services, Elastic Kubernetes Service y AWS SageMaker. En sistemas de storage avanzados de la marca NetApp se tiene la inteligencia necesaria para mover información poco usada a discos duros mas lentos (y mas baratos), esta característica también la comparte EFS, ahorrándonos un poco en costos dependiendo de la cantidad de información que maneje el volumen, la decisión se hace por medio de una barrera de tiempo.
 Al generar un volumen podemos especificar a partir de cuantos días los datos no son accesados moverlos a una "capa" de EFS mas económica, también podemos definir la VPC donde se conectará e volumen y las redes sin dejar pasar el control de acceso por medio de grupos de seguridad, para complementar la seguridad de nuestro volumen podremos definir políticas de cifrado de tránsito, acceso de solo lectura y restricción de acceso a la raíz del volumen.
 La verdad es que es muy rápido generar un volumen EFS, después de 10 minutos de lectura y algunos clicks tendremos un volumen listo para ser usado. 
 ![efs](efs.png)
 
 
 

# Data Transfer con AWS Snowball
Snowball es el servicio de AWS diseñado para la transferencia de altos volúmenes de datos desde y hacia los centros de datos de AWS.
Snowball son dispositivos físicos de unos 21 kilogramos de peso, de 50x30x50 cm con capacidad de almacenamiento de 42 TB y 72TB, con conexiones 10 gigabit para transferencia de datos diseñado para llevar datos desde nuestro propio centro de datos hacia AWS S3 y de regreso en el caso de tener tantos datos que sería inviable la transferencia por Internet en periodos cortos de tiempo.
Los dispositivos son resistentes a la extracción no autorizada de información (tramper), protegidos por cifrado 256 bits con AWS KMS, físicamente son resistentes a los tratos rudos, el propio dispositivo es el contenedor de envío.
![https://docs.aws.amazon.com/snowball/latest/developer-guide/images/Snowball-Edge-Image.png](https://docs.aws.amazon.com/snowball/latest/developer-guide/images/Snowball-Edge-Image.png)

En cuanto a precio, ronda los 300 USD por 10 días de uso.

# Aurora
Es un motor no open source de base de datos relacional compatible con MySQL y Postgres con capacidad de autoescalado y almacenamientos de hasta 64 TB
Es compatible con snapshots para backups, cifrado con llaves KMS, es compatible con operación por instancia, nosotros decidimos el tamaño de instancia al crear la base de datos, aunque también ofrece un modelo de precio basado en `serverless` especialmente atractivo en aplicaciones de uso poco frecuente donde la aplicación es accesada pocos minutos varias veces en un día,  es posible también adquirir un contrato con plazo de 1 o 3 años consiguiendo un mejor precio por instancia por hora.
Aurora brinda un rendimiento aproximado 5X cuando hablamos de bases de datos MySQL tradicionales y 3X al hablar de Postgres, esto se logra con su motor propietario optimizado para ejecutarse sobre una configuración de hardware específica de SSD.
Si es posible modificar el tamaño de la instancia, la memoria y el número de CPUs, sin embargo no es en `caliente`, se tiene que entrar en un periodo de mantenimiento (la instancia deja de estar disponible) hasta que los cambios se realicen, es el análogo a reiniciar la instancia para que se ajuste a los nuevos valores.

- Amazon Relational Database Service (RDS)
# Amazon DynamoDB
DynamoDB es una base de datos NoSQL, 
El esquema de precios de DynamoDB es difícil de calcular, en resumen el precio es calculado  por el almacenamiento de datos, escrituras y leecturas de información.

Almacenamiento de datos
DynamoDB cobra por GB de espacio en disco que consume una tabla. Los primeros 25 GB consumidos por mes son gratuitos y los precios comienzan en 0,25 dólares por GB al mes.

Escritura
AWS calcula el costo de las escrituras utilizando "Unidades de capacidad de escritura". Cada WCU proporciona hasta una escritura por segundo, suficiente para 2.6 millones de escrituras por mes. DynamoDB cobra una unidad de solicitud de escritura por cada escritura (hasta 1 KB) y dos unidades de solicitud de escritura por escrituras transaccionales.

Lectura
AWS calcula el costo de las lecturas mediante "Unidades de capacidad de lectura". Cada RCU proporciona hasta dos lecturas por segundo, suficiente para 5.2 millones de lecturas por mes. DynamoDB cobra una unidad de solicitud de lectura por cada lectura de gran coherencia (hasta 4 KB), dos unidades de solicitud de lectura por cada lectura transaccional y la mitad de la unidad de solicitud de lectura por cada lectura eventualmente coherente.

Cuando se solicita una lectura  consistente, DynamoDB devuelve una respuesta con los datos más actualizados, lo que refleja las actualizaciones de todas las operaciones de escritura anteriores que tuvieron éxito

# Amazon Elasticache 
# Amazon Redshift


# AWS Storage Gateway
Es un servicio que nos permite conectar aplicaciones on premise con storage basado en la nube.
Soporta conexión con tres tipos de storage, File gateway (almacén en S3) compatible con el protocolo NFS y SMB integrando con IAM, KSM para cifrado, CloudWatch para monitoreo , Volume gateway (almacén en EBS) y Tape gateway (Almacén en S3 Gacier).
El servicio puede ser hosteado en una maquina virtual on premise en hypervisores ESX, HyperV o lanzar una instancia EC2.

Un ejemplo es el uso de la solución de respaldos Backup Exec de Symantec. Es posible provisionar un nodo de storage Gateway de tipo Tape y conectar Backup Exec para guardar los respaldos directamente en S3.
![backupexec.png](backupexec.png)

Otro ejemplo:
Tenemos dos oficinas cada una en diferentes ciudades, montando una instancia de AWS Sotrage Gateway de tipo File en cada oficina con acceso a un bucket específico de S3 ambas localizaciones tendrán acceso a los archivos del bucket de forma fácil en sus sitemas operativos, en el caso de Widows se refleja como una unidad de red montada.
![Montando-carpetas-compartidas.png](Montando-carpetas-compartidas.png)

![unidad virtual.png](unidad virtual.png)




# AWS DocumentDB
Las bases de datos de documentos o documentales se centran en métodos de almacenamiento y acceso optimizados para documentos en lugar de filas o registros en una base de datos relacional. La forma de modelar   datos es un conjunto de colecciones de documentos que contienen colecciones de valores clave. En un almacén de documentos, los valores pueden ser otros documentos o listas anidadas y  valores escalares. Los nombres de los atributos no están predefinidos en un esquema global, sino que se definen dinámicamente para cada documento en tiempo de ejecución. A diferencia de las bases de datos relacionales, se autoriza una amplia gama de valores. 
![Document-db.png](Document-db.png)

| RDBSM         | Mongo DB      |
|---------------|---------------|
| Base de datos | Base de datos |
| Tabla         | Colección       |
| Registro/Tupla| JSON            |
| Columnas      | Campos del JSON |


AWS DocumentDB es una base de datos especializada en el guardado de información en formato JSON. Es compatible con la API MongoDB 3.6, en principio bastaría con modificar la cadena de conexión de la aplicación para migrar a AWS DocumenrDB.
Es un servivio PaaS, no hay necesidad de preocuparse por administrar provisionamiento de hardware, red, parches de seguridad, configuración o instalación, incluso los respaldos están cubiertos con capacidad para respaldar directamente en S3.
En cuanto a precio, DocumentDB se divide en cuatro dimensiones: costo por instancia, costo por E/S de datos, espacio de almacenamiento y respaldos. Un estimado en la AWS Pricing Calculator nos da el [siguiente resultado](https://calculator.aws/#/estimate?id=a8d70de522d91d5266c310c057038c7dcdde557c).




# AWS Keyspaces
https://www.youtube.com/watch?v=zehVQzlSuEU

# AWS Neptune
Las bases de datos relacionales modelan bien datos que no tienen alta tasa de relación entre ellos, para modelar datos con mucha relaciones es posible utilizar bases de datos orientadas a grafos.
Las bases orientadas a grafos centran el guardado de información en las relaciones entre entidades.
![graph](https://upload.wikimedia.org/wikipedia/commons/5/53/GraphDatabase_PropertyGraph.svg)
AWS ofrece Amazon Neptune como un PaaS (no hay necesidad de preocuparse por hardware, parches, provisionamiento, configuración o backups) con soporte Gremlin de Apache TinkerPop como el lenguaje de consulta SPARQL del formato de datos [RDF](https://skos.um.es/TR/rdf-sparql-query/).
Neptune ofrece disponibilidad de 99.99%, lo logra replicando la base de datos en tres zonas de disponibilidad totalmente transparente, en caso de fallo de una zona de disponibilidad el cambio a otra zona de disponibilidad tarda unos 30 segundos en realizarse sin necesidad de intervención del administrador. Soporta tasas de hasta 100 000 queries por segundo con capacidad de almacenar  64 TB  de información. Se integra con VPC para el networking y con AWS KSM para el cifrado de la información.
Después de llenar un formulario en AWS Console es posible tener funcionando una instancia de base de datos de Neptune lista para operar.

![neptune](neptune.png)

![neptune2](neptune2.png)

Un [ejemplo](https://twitter.com/omarsar0/status/1309106152106602497?s=20) de visualización de datos con este tipo de base de datos.



# Amazon Timestream
Otro tipo de base de datos que sale de lo común de las bases de datos relacionales son las bases de datos para series temporales (time series database), se especializan en el almacenamiento y procesamiento de datos con `estampas de tiempo` a altas tasas de ingestión con optimización para la recuperación de información con el parámetro principal del tiempo.
Las aplicaciones comunes son procesamiento de datos financieros para hacer trading, autos autónomos con la cantidad de información generada por las cámaras, radares y sensores. 
Timestream es un servicio PaaS, unos cuantos click bastarán para despreocuparse sobre clusters, infraestructura, tipos de storage para tener lista una base de datos funcionando.
Aunque el servicio fue anunciado en el AWS re:Invent 2018 el servicio no está abierto a todo público, no se puede seleccionar en AWS Console, en su lugar habrá que llenar un formulario que AWS evaluará para dar acceso al servicio.
![timestream-preview](timestream-preview.png)





# Amazon Quantum Ledger Database

Amazon QLDB es una base de datos diseñada para mantener todo el historial de las transacciones hechas inmutable, el historial de las transacciones no puede ser modificado, eliminado u alterado garantizando la integridad de las transacciones por criptografía. 
Esta característica hace de QLDB especialmente interesante en aplicaciones del ramo bancario donde debe quedar un registro inalterable y verificable de cada movimiento financiero de las cuentas bancarias.
QLDB no soporta por el momento ningún tipo de restauración de datos ni respaldo, solo es posible exportar los datos a un bucket S3, para garantizar la disponibilidad de la información se replica a todas las zonas de disponibilidad de la región donde se ejecuta el servicio.
QLDB tiene cifrado por defecto habilitado además es compatible con conexiones VPC privadas.

Literal en dos click tenemos una instancia ejecutándose. 

![qldb.png](qldb.png)

![qldb-2.png](qldb-2.png)


![qldb-3.png](qldb-3.png)

En la propia consola de QLDB podemos ejecutar consultas con el lenguaje [PartiQL](https://partiql.org/faqs.html#what-is-partiql).

![qldb-4](qldb-4.png)


