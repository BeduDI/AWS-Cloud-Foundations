## Sesión 3 - Ejemplo 2

### 1. Objetivo :dart:
- Conocer como se pueden asegurar los datos de reposo en un bucket por medio del cifrado.

### 2. Requisitos :pushpin:
- AWS CLI instalado y configurado.
- Acceso a AWS Console.
- Un bucket S3 con algunos archivos que simularán ser archivos con información sensible.

### 3. Desarrollo :bookmark_tabs:
El proceso de cifrado será dividido en dos fases para un bucket sin cifrado. Se comenzará especificando la política de cifrado de nuevos archivos que se suban al bucket, esta política no afectará a los archivos que ya existan en él.
Una vez configurado el bucket habrá que cifrar todos los datos ya existentes en él.

1. Acceder a la linea de comandos. Listar todos los buckets solo para corroborar cual será cifrado. Es recomendable especificar la región del bucket.

```ssh
aws --region us-east-1 s3 ls
```
![ej3-list-buckets.png](ej3-list-buckets.png)

2. Configurar la política de cifrado para nuevos archivos especificando el nombre del bucket y el tipo de cifrado que tendrá el bucket con el comando:
```ssh
aws --region us-east-1 s3api put-bucket-encryption --bucket facturas-personales --server-side-encryption-configuration '{"Rules": \[{"App  
lyServerSideEncryptionByDefault": {"SSEAlgorithm": "AES256"}}\]}'
```

3. Al ingresar a la consola de AWS al entrar a las propiedades del bucket se verá la siguiente opción habilitada indicando que el bucket cifrará los archivos nuevos que sean depositados.

![ej2-bucket-facturas-personales.png](ej2-bucket-facturas-personales.png)

![ej2.awsconsole-cifrado.png](ej2.awsconsole-cifrado.png)

4. Al ver el detalle de los archivos se puede ver que los archivos existentes aun no son cifrados.
![ej2-files-ciphered.png](ej2-files-ciphered.png)

5. Para cifrar los archivos se ejecuta el comando

```ssh
aws --region us-east-1 s3 cp s3://facturas-personales s3://facturas-personales --sse AES256 --recursive
```

![ej2-files-ciphered.png](ej2-files-ciphered.png)


6. Al verificar el archivo en la consola se puede ver que ya está cifrado.
![ej2-aws-console-file-cifrado.png](ej2-aws-console-file-cifrado.png)

7. Los archivos pueden ser descargados con el mismo comando de AWS CLI o desde la consola de AWS.

![ej2-list-files.png](ej2-list-files.png)

Los archivos pueden ser abiertos sin ningún problema.
![ej2-files-decrypted.png](ej2-files-decrypted.png)

8. Se sube un archivo para comprobar el cifrado con el comando:
```ssh
aws --region us-east-1 s3 cp .pgAdmin4.startup.log s3://facturas-personales
```

![ej2-upload-file.png](ej2-upload-file.png)


Es de notar que los archivos se están cifrado de manera transparente al subirlos y descargarlos.