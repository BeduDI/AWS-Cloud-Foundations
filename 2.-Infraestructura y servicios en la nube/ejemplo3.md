## Sesión 2 - Ejemplo 3 - Servidor web estático

### 1. Objetivo :dart:
- Poner en marcha un bucket S3 como un servidor web estático.

### 2. Requisitos :pushpin:
- Git instalado localmente. [¿Cómo instalar git?](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- Repositorio en local https://github.com/mdn/beginner-html-site-styled


### 3. Desarrollo :bookmark_tabs:

1. Ingresar a la consola de AWS y seleccionar S3.
![b1129b066999b324d197ae15ca6042a2.png](b1129b066999b324d197ae15ca6042a2.png)


2. Dar click en nuevo bucket.
![web-server-bucket-01.png](web-server-bucket-01.png)

3. Seleccionar un nombre para el bucket, recordar que el nombre debe ser único es decir que no se haya repetido en ninguna otra cuenta de AWS.
![sitio-estatico-nombre-bucket.png](sitio-estatico-nombre-bucket.png)

4. Establecer etiquetas para el bucket.
![sitioestatico-tags.png](sitioestatico-tags.png)
5. Dejar la configuración de acceso por defecto
![sitioestatico-bucket-acceso.png](sitioestatico-bucket-acceso.png)

6. Dar click en "Crear bucket"
![sitioestatico-generar-bucket.png](sitioestatico-generar-bucket.png)

Observar la generación del bucket:
![sitioestatico-bucket-generado.png](sitioestatico-bucket-generado.png)

7. Descargar el zip del [repositorio](https://github.com/mdn/beginner-html-site-styled), descomprimir el contenido.
![sitioestatico-descargar-zip.png](sitioestatico-descargar-zip.png)

8. Dar click en "Cargar"
![sitioestatico-cargar.png](sitioestatico-cargar.png)

9. Arrastrar los archivos y carpetas, si no se arrastran las carpetas no pueden ser seleccionadas. Dar click en "Cargar"
![sitioestatico-upload-files.png](sitioestatico-upload-files.png)
Los archivos serán cargados y se podrán ver en la consola de AWS S3.
![sitioestatico-archivos-cargados.png](sitioestatico-archivos-cargados.png)

Al dar click en el archivo index.html se visualizan una serie de propiedades (metadatos), entre ellas se tiene la "URL del objeto"
![sitioestatico-url-objeto.png](sitioestatico-url-objeto.png)
Al dar click en la URL tenemos el siguiente error.
![sitioestatico-error.png](sitioestatico-error.png)

Aún faltan pasos antes de que el archivo sea visible desde internet.
Los pasos siguientes son:

10. Regresando al nivel de bucket (a), dar click en propiedades (b), seleccionar "Alojamiento de sitios web estáticos"
![sitiosestaticos-config-alojamiento.png](sitiosestaticos-config-alojamiento.png)

11. Establecer la configuración de alojamiento estático (a), proporcionar el nombre del archivo que será servido por default (b), click en guardar (c).
![sitioestatico-habilitar-sitio-estatico.png](sitioestatico-habilitar-sitio-estatico.png)
 
 12. A nivel bucket pasar a "Permisos" (a), editar (b) y desactivar la opción bloquear todo acceso público (d), guardar cambios.
 ![74f36eac2ab0dee018358fb8857ae291.png](74f36eac2ab0dee018358fb8857ae291.png)

13. En información general a nivel de búcket (a), seleccionar todos los archivos (b), después click en "Hacer público".
![sitio-estatico-hacer-publico.png](sitio-estatico-hacer-publico.png)

14. Hechos los  pasos anteriores la página web esta lista para ser servida.
![sitioestatico-web-ready.png](sitioestatico-web-ready.png)

