## REQUERIMIENTOS TÉCNICOS

1. **Tecnologías Utilizadas:**
   - Backend: Django para la lógica de servidor y la gestión de bases de datos.
   - Frontend: Angular para la interfaz de usuario interactiva.
   - Se debe implementar una comunicación eficiente entre el frontend y el backend a través de la libreria API REST FRAMEWORK de Django.

2. **Base de Datos:**
   - Se utilizara el servicio de base de datos SQLite3 para manejar eficientemente el almacenamiento de archivos.

3. **Gestión de Usuarios:**
   - Implementar un sistema de gestión de usuarios.
   - Garantizar la persistencia de los datos de usuario en la base de datos.
4. **Dependencias:**
    ----------FRONTEND--------------
    - @angular/animations": "^16.2.0",
    - "@angular/cdk": "^16.2.0",
    - "@angular/common": "^16.2.0",
    - "@angular/forms": "^16.2.0",
    - "primeicons": "^6.0.1",
    - "primeng": "^16.2.0",
   ----------BACKEND----------------

## REQUERIIENTOS FUNCIONALES

### David Garay

1. **Subida de Archivos:**
   - El sistema debe permitir la carga de uno o varios archivos simultáneamente en la base de datos.
   - Los archivos subidos deben ser gestionados y almacenados de manera segura en el sistema.

2. **Búsqueda de Archivos:**
   - El sistema debe contar con funcionalidades de búsqueda que permitan buscar archivos por nombre y por propietario.

3. **Visualización de Información de Archivos:**
   - Debe mostrar de manera clara y organizada el nombre, tamaño y propietario de cada archivo en la interfaz.

4. **Descarga de Archivos:**
   - Los usuarios deben poder descargar archivos almacenados en la base de datos de forma segura.

5. **Registro de Usuario:**
   - Se debe implementar un sistema de registro que permita a los usuarios crear cuentas de manera segura.

6. **Edición de Datos del Usuario:**
   - Los usuarios registrados deben tener la capacidad de editar sus datos de usuario, como nombre, correo electrónico, etc.

### Erickson Meliano

1. **Interfaz de Usuario:**
   - El sistema debe ofrecer una interfaz de usuario intuitiva, sencilla y amigable, siguiendo las mejores prácticas de diseño.

2. **Edición de Nombres de Archivos:**
   - Se debe proporcionar la capacidad de editar los nombres de los archivos previamente subidos por los usuarios.

3. **Eliminación de Archivos:**
   - Los usuarios deben poder eliminar archivos que hayan subido previamente, con la garantía de que la operación sea segura.

4. **Autenticación de Usuario:**
   - Debe existir un sistema de autenticación que permita a los usuarios iniciar y cerrar sesión de manera segura.

5. **Visualización de Archivos por Usuario:**
   - El sistema debe mostrar de manera clara la lista de archivos subidos por cada usuario en su sesión.

## REQUERIMIENTOS NO FUNCIONALES

1. **Seguridad:**
   - El sistema debe implementar medidas de seguridadpara proteger la integridad y confidencialidad de los datos del usuario.
   - La comunicación entre el frontend (Angular) y el backend (Django) debe ser segura utilizando HTTPS.

2. **Rendimiento:**
   - El sistema debe ser eficiente y capaz de manejar cargas de trabajo variables, garantizando un rendimiento óptimo incluso con múltiples usuarios concurrentes.

3. **Escalabilidad:**
   - La arquitectura del sistema debe ser escalable para permitir futuras expansiones y ajustes de capacidad.
