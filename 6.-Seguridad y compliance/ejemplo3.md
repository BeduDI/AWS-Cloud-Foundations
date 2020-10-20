## Sesión 6 - Ejemplo 3

### 1. Objetivo :dart:
- En un bucket S3 buscar información sensible.

### 2. Requisitos :pushpin:
- AWS CLI instalado y configurado.
- Un bucket S3 con algunos archivos que simularán ser archivos con información sensible.

### 3. Desarrollo :bookmark_tabs:

1. Ingresar a la consola de AWS buscando el servicio Amazon Macie.
![ej3-macie-get-start.png](ej3-macie-get-start.png)

2. Habilitar Macie, al habilitarlo se genera un rol con la política necesaria para que el servicio acceda al servicio S3.

![el3-habilitar-macie.png](el3-habilitar-macie.png)

![ej2-habilitar-macie-02.png](ej2-habilitar-macie-02.png)

3. Al habilitar el servicio, Macie  da un reporte de los buckets a los que tiene acceso. Habrá que ejecutar un trabajo de escaneo

![ej2-macie-dashboard-01.png](ej2-macie-dashboard.png)

4. Se debe seleccionar el o los buckets para ser analizados.

![ej2-buckets-selected.png](ej2-buckets-selected.png)


5. Confirmar el bucket y el costo estimado.
![ej3-macie-estimado.png](ej3-macie-estimado.png)

6. Para no incurrir en costos periódicos se deberá seleccionar como trabajo único.
![ej3-macie-periodicidad.png](ej3-macie-periodicidad.png)

7. En la siguiente pantalla se pueden escoger identificadores personales, son patrones basados en regex o palabras clave que deben ser identificados como información sensible, por defecto Macie ya detecta nombres,direcciones y números de tarjetas de crédito.
![ej3-identificadores-personales.png](ej3-identificadores-personales.png)

8. Se asigna un nombre y descripción para el trabajo.
![ej3-macie-add-name-and-description.png](ej3-macie-add-name-and-description.png)

9. Se revisan los datos configurados, de ser correctos se finaliza la configuración.
![ej3-macie-config-review.png](ej3-macie-config-review.png)

10. El trabajo comienza a ejecutarse.
![ej3-macie-running-job.png](ej3-macie-running-job.png)

11.  Completado el trabajo se tendrá acceso a un reporte de hallazgos.

![ej2-macie-job-done.png](ej2-macie-job-done.png)

12. Verificando el contenido del archivo se puede ver que son 4 nombres encontrados y reportados.
![ej3-report-done.png](ej3-report-done.png)

