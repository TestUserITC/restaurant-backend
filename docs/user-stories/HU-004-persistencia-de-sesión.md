## HU-004: Persistencia de Sesión

### Descripción
Como usuario autenticado, quiero que mi sesión persista en el navegador para no tener que iniciar sesión cada vez que vuelvo a abrir la aplicación.

### Criterios de Aceptación

**Almacenamiento de Sesión:**
- Al hacer login exitoso, el token de autenticación se guarda de forma segura en el cliente
- El token se mantiene almacenado incluso si el usuario cierra el navegador
- La sesión persiste hasta que el usuario haga logout explícito o el token expire

**Validación de Sesión al Cargar la App:**
- Al cargar cualquier página protegida, validar si existe un token válido
- Si el token es válido, permitir acceso a la página solicitada
- Si el token es inválido o no existe, redirigir a `/login`
- La validación debe ocurrir antes de renderizar contenido protegido

**Redirección Automática:**
- Si el usuario autenticado intenta acceder a `/login`, `/register`, o `/recuperar-password`, redirigir a `/dashboard`
- Si el usuario no autenticado intenta acceder a páginas protegidas, redirigir a `/login`
- Después de redirigir a login, al autenticarse exitosamente, redirigir al usuario a la página que originalmente intentaba acceder

**Token Expirado:**
- Si el token expiró durante una sesión activa, mostrar modal: "Tu sesión ha expirado. Por favor, inicia sesión nuevamente"
- Al cerrar el modal o hacer clic en "Aceptar", redirigir a `/login`
- Limpiar el token almacenado

**Estado de Autenticación Global:**
- El estado de autenticación (isAuthenticated, user, role) debe estar disponible en toda la aplicación
- Al hacer logout, limpiar completamente el estado de autenticación y el token almacenado

**Indicador de Carga:**
- Mientras se valida el token al cargar la app, mostrar un loader/spinner centrado en pantalla
- Evitar mostrar flashes de contenido no autenticado antes de la validación

### Escenarios

1. **Usuario regresa después de cerrar navegador**: Usuario hace login, cierra navegador, vuelve a abrir y navega a la URL de la app, ve directamente el dashboard sin necesidad de login
2. **Token válido en navegación**: Usuario autenticado navega entre diferentes secciones (`/menu`, `/pos`, `/orders`), mantiene sesión activa sin interrupciones
3. **Token expirado durante uso**: Usuario tiene sesión activa, deja la pestaña abierta por muchas horas, el token expira, al intentar hacer una acción ve modal "Tu sesión ha expirado", hace clic en "Aceptar", es redirigido a login
4. **Acceso a login estando autenticado**: Usuario autenticado intenta navegar manualmente a `/login`, es redirigido automáticamente a `/dashboard`
5. **Acceso a página protegida sin autenticación**: Usuario sin sesión intenta acceder a `/menu`, es redirigido a `/login`, después de iniciar sesión exitosamente es redirigido de vuelta a `/menu`
6. **Logout explícito**: Usuario hace clic en "Cerrar sesión" en el menú, su token es eliminado, es redirigido a `/login`, al intentar volver atrás no puede acceder a contenido protegido
7. **Token inválido al cargar**: Usuario tiene un token corrupto almacenado, al cargar la app, el sistema detecta token inválido, limpia el token, redirige a login
8. **Validación en carga inicial**: Usuario abre la app, mientras se valida token ve un spinner centrado por 0.5-1 segundo, después ve el dashboard (o login si no está autenticado)

---