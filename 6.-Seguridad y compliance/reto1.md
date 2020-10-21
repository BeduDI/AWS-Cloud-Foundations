## Sesión 3 - Reto 1


### 1. Objetivo :dart:
- Establecer una administración de políticas y usuarios de fácil administración.

### 2. Requisitos :pushpin:
- Una cuenta de usuario de IAM con una **política insertada**, es decir una política agregada directamente al usuario.

### 3. Desarrollo :bookmark_tabs:

Una política insertada es una política que no puede ser rehusada ya que solo está disponible para el usuario para la que se generó. En el escenario que se deban agregar 20 usuarios para administrar el contenido del bucket configurado como servidor web habría que ir en cada usuario agregando la política, si la política se requiere cambiar en el futuro habrá que ir en cada usuario cambiando a política proceso en el cual es muy propenso a error humano pudiendo no aplicar correctamente las políticas de acceso o denegación a algún usuario. Se generará un grupo, a ese grupo se agregará una política, así si se requiere usar esa política solo habría que agregar a los 20 usuarios al grupo sin necesidad de ir definiendo la política usuario por usuario.

1. Ingresar a IAM, usuarios y seleccionar le usuario con la política insertada. Expandir la política insertada y copiar el contenido JSON de la política.
![r1-politica-insertada-copiar.png](r1-politica-insertada-copiar.png)

2. Dirigirse al menú de políticas y luego dar click en "crear una nueva política", con ello se generará una política que puede ser reutilizada.
![r1-add-new-policy.png](r1-add-new-policy.png)

3. Dar click en JSON, copiar la política previamente copiada y dar click en "Revisar política".
![r1-json-policy.png](r1-json-policy.png)

4. AL pasar a revisión se debe especificar el nombre de la política y una descripción, la descripción debe ser lo suficientemente detallada para saber a que aplica la política y para que fue diseñada.
![r1-add-shared-policy.png](r1-add-shared-policy.png)

5. Creada la política habrá que dirigirse a "Grupos"
![r1-add-group-menu.png](r1-add-group-menu.png)
Dar click en "Crear grupo"
![r1-add-group.png](r1-add-group.png)

6. Establecer un nombre al grupo.
![r1-add-group.png](r1-add-group.png)

7. Se busca la política recién creada para asociarla al grupo.
![r1-add-policy-to-grouo.png](r1-add-policy-to-grouo.png)

8. Revisar que la política asociada es correcta, después dar click en "Crear grupo"
![r1-add-group-done.png](r1-add-group-done.png)

9. Ingresar al grupo recién creado, para agregar usuarios. Todos los usuarios agregados tendrán aplicada la política asociada al grupo, basta con sacar al usuario del grupo para que la política deje de aplicarle.

![r1-add-user.png](r1-add-user.png)

![r1-add-user-done.png](r1-add-user-done.png)

10. Al ingresar el usuario se observa aún la política administrada, también se observan las políticas aplicadas al usuario por medio de la pertenencia a grupos de IAM. Ya se puede eliminar con seguridad la política insertada (a) con ello se ha generado una estructura de permisos bastante mantenible.

![r1-remove-inserted-policy.png](r1-remove-inserted-policy.png)

11. Se comprueba que el comportamiento de los permisos del usuario sigan siendo los correctos después de eliminar la política insertada. ¡Éxito!

![r1-access-denied-bucket-01.png](r1-access-denied-bucket-01.png)

![r1-access-granted.png](r1-access-granted.png)
