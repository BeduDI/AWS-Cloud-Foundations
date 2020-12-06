# Ejemplo 3

# 1. Objetivo 🎯
- Muchas veces al trabajar con datos el reto consiste en normalizar los datos a un formato útil para los propósitos de las tareas que se desean realizar.

# 2. Requisitos 📌
- Cuenta de AWS Console
- AWS CLI configurado con credenciales con permisos para lectura y escritura en el servicio S3.

# 3. Desarrollo 📑

#### El siguiente ejemplo y código están destinados únicamente a fines educativos. Asegúrese de personalizarlo, probarlo y revisarlo por su cuenta antes de usar cualquiera de esto en producción.


1. Generar un bucket de S3, el bucket será el origen de datos y el destino de los datos ya transformados. Para hacer el trabajo ágilmente se hará por medio de línea de comandos.
Para tal efecto ejecutar el comando 
```ssh
aws s3api create-bucket --bucket my-glue-etl-job-01 --region us-east-1
```
Donde `my-glue-etl-job-01` es el nombre del bucket, se puede personalizar el nombre por uno a conveniencia propia.

![ej3-s3-create-bucket-01.png](ej3-s3-create-bucket-01.png)

2. Generar un par de carpetas en el bucket, una carpeta como origen de datos y otra de destino, para lo cual hay que ejecutar el comando:

```ssh
aws s3api put-object --bucket my-glue-etl-job-01 --key origen/
```

```ssh
aws s3api put-object --bucket my-glue-etl-job-01 --key destino/
```

![ej3-create-bucket-s3-origin-destino-folders.png](ej3-create-bucket-s3-origin-destino-folders.png)


3. Descargar los datos que se van a procesar desde:
https://raw.githubusercontent.com/peetck/IMDB-Top1000-Movies/master/IMDB-Movie-Data.csv
 Guardar el archivo en una ubicación conocida. Normalmente se puede hacer dando click derecho sobre la página y seleccionando "Guardar como"
 ![ej3-save-as-csv-database-imdb-01.png](ej3-save-as-csv-database-imdb-01.png)

 
 
4. Subir el archivo que se acaba de descargar con el comando 
```bash
aws --region us-east-1 s3 cp D:\downloads\IMDB-Movie-Data.csv s3://my-glue-etl-job-01/origen/
```

Donde `D:\downloads\IMDB-Movie-Data.csv` es la ruta del origen del archivo, reemplazar por la ruta del archivo.

![ej3-s3-upload-file-01.png](ej3-s3-upload-file-01.png)


5. Acceder a la consola de AWS, buscar el servicio "Glue", ingresar al servicio.
![ej3-aws-glue-ingress-to-service-01.png](ej3-aws-glue-ingress-to-service-01.png)


6. Ya en el servicio AWS Glue, a) seleccionar "BAse de datos", b) seleccionar "Añadir una base de datos", c) establecer un nombre a los datos que se procesarán.

![ej3-glue-add-database-01.png](ej3-glue-add-database-01.png)

7. a) Seleccionar En el menú "Tablas" y luego b) "Añadir tablas con un rastreador"
![ej3-add-new-table-with-crawler-01.png](ej3-add-new-table-with-crawler-01.png)

8. Especificar un nombre a la tabla, luego click en  "Siguiente"
![ej3-glue-add-name-click-in-next-01.png](ej3-glue-add-name-click-in-next-01.png)

9. Seleccionar las opciones por default
![ej3-add crawler-01.png](ej3-add crawler-01.png)

10. Seleccionar un origen de datos, en este caso S3, seleccionar la ruta de origen de datos que en este caso será la carpeta "origen" en el  bucket S3 recién creado.
![ej3-glue-add-source-files-01.png](ej3-glue-add-source-files-01.png)
 
 11. Seleccionar siguiente
 ![ej3-glue-choose-next-01.png](ej3-glue-choose-next-01.png)

12. Es momento de generar un rol para que AWS Glue tenga acceso al bucket S3. Establecer un sufijo al role y dar click en "siguiente".
![ej3-glue-create-role-01.png](ej3-glue-create-role-01.png)

13. Seleccionar la frecuencia de ejecución "Bajo demanda"
![ej3-glue-run-frequency-01.png](ej3-glue-run-frequency-01.png)


14. Seleccionar la base de datos creada en un principio
![ej3-select-database-01.png](ej3-select-database-01.png)


15. Hechos todos los pasos dar click en "Finalizar":
![ej3-glue-end-crawler-done-01.png](ej3-glue-end-crawler-done-01.png)


16. a) Hacer click en "Rastreadores", b) seleccionar el recién hecho y dar click en "Ejecutar rastreador"
![ej3-glue-run-crawler-01.png](ej3-glue-run-crawler-01.png)

Se verá como comienza la ejecución:
![ej3-glue-crawler-starded-01.png](ej3-glue-crawler-starded-01.png)

17. a) Dar click en "Tablar", b) se verá una tabla creada por el rastreador
![ej3-glue-table-created-by-crawler-01.png](ej3-glue-table-created-by-crawler-01.png)



-----------------------
Cambio políticas.

Para asegurar que AWS Glue podrá escribir y leer en el bucket S3 habrá que modificar un poco la política que fue generada en el paso 12.

1. Habrá que ir al servicio AWS IAM.

![ej3-access-to-iam-01.png](ej3-access-to-iam-01.png)



2. Dirigirse a la sección de políticas. 
![ej3-iam-goto-to-policies-01.png](ej3-iam-goto-to-policies-01.png)


3. a) filtrar la política escribiendo la palabra "glue", b) seleccionar la política creada por el servicio de AWS Glue.
![ej3-glue-select-policy-01.png](ej3-glue-select-policy-01.png)


4. La política es mostrada, aquí hay que observar un par de cosas.
a) AWS Glue generó los permisos necesarios para depositar y obtener objetos del servicio S3
b) El problema es que solo lo hizo para la carpeta "origen" en el bucket S3, es aqui donde habrá que editar la política para permitir la lectura y escritura a la carpeta "destino", click en editar:
![ej3-iam-edit-policy-01.png](ej3-iam-edit-policy-01.png)

3. Editar la política editando su definición en formato JSON directamente:
![ej3-iam-edit-policy-json-format-01.png](ej3-iam-edit-policy-json-format-01.png)

4. Copiar la linea de "resources" y editarla para que quede de la misma forma pero ahora con al carpeta "destino".


![ej3-iam-role-edit-01.png](ej3-iam-role-edit-01.png)


![ej3-iam-add-new-origin-01.png](ej3-iam-add-new-origin-01.png)


Guardar el cambio de política.

![ej3-iam-save-policy-01.png](ej3-iam-save-policy-01.png)


![ej3-iam-save-policy-02.png](ej3-iam-save-policy-02.png)


---------------------------
De Regreso a AWS Glue:

1. Hacer click en "AWS Glue Studio", aquí será el lugar para generar el _trabajo_ ETL que transformará los datos.
![ej3-glue-access-aws-glue-studio-01.png](ej3-glue-access-aws-glue-studio-01.png)


2. Click en "Create and manage jobs"
![ej3-glue-create-and-manage-jobs-01.png](ej3-glue-create-and-manage-jobs-01.png)



3. Seleccionar a) para el trabajo "Source and target", b) seleccionar en el origen y destino de datos un bucket S3, finalmente click en "Create"
![ej3-glue-etl-job-create-01.png](ej3-glue-etl-job-create-01.png)

4. Configurar la tarea requerirá configurar el origen y destino de los datos.
a) Seleccionar el bucket de origen
b), c) Seleccionar la base de datos

![ej3-select-bucket-s3-and-configure-01.png](ej3-select-bucket-s3-and-configure-01.png)

5. Click en el ícono del mapeo de datos, se puede observar los campos del CSV y el tipo de datos.

![ej3-glue-apply-mapping-01.png](ej3-glue-apply-mapping-01.png)


6. Seleccionar la configuración de la salida de datos.
b) Seleccionar el formato de salida
c) Seleccionar el bucket y la carpeta donde se depositaran los datos.
d) Click en "Job details"
![ej3-glue-configure-output-01.png](ej3-glue-configure-output-01.png)

7. Antes de guardar el trabajo
a) Establecer un nombre
b) Seleccionar el role modificado con anterioridad.
![ej3-glue-establish-name-and-role-01.png](ej3-glue-establish-name-and-role-01.png)


8. Después de guardado el trabajo click en "Run", con ello comenzará la transformación del archivo CSV a JSON.

![ej3-glue-Job-Done-01.png](ej3-glue-Job-Done-01.png)


9. Al ir a la parte de monitoreo de tareas se verá una tarea ejecutándose. Después de algunos minutos el trabajo se completará. 
![ej3-glue-job-running-01.png](ej3-glue-job-running-01.png)

10. Ir al servicio S3, al bucket creado a la carpeta "destino", se podrá ver un archivo recién creado.
![ej3-aws-glue-created-file-01.png](ej3-aws-glue-created-file-01.png)


11. Al descargar el archivo y abrirlo en un editor de texto plano se puede ver que el archivo es un archivo con contenido Json listo para ser usado.
![ej3-json-file-done-01.png](ej3-json-file-done-01.png)
