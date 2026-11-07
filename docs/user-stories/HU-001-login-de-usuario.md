## HU-001: Login de Usuario

### Descripción
Como usuario registrado (Owner o Cajero), quiero iniciar sesión en el sistema para acceder a las funcionalidades del punto de venta y administración del restaurante según mi rol.

### Criterios de Aceptación

**Estructura y Contenido de la Pantalla:**
- La página de login muestra un formulario centrado con:
  - Logo o nombre de la aplicación
  - Título "Iniciar Sesión"
  - Campo de texto para email con placeholder "Correo electrónico"
  - Campo de contraseña con placeholder "Contraseña" y opción de mostrar/ocultar contraseña (icono de ojo)
  - Botón "Iniciar Sesión" (primario)
  - Link "¿Olvidaste tu contraseña?" debajo del botón
  - Link "¿No tienes cuenta? Regístrate" al final del formulario

**Validaciones de Campos:**
- El campo email es requerido y debe tener formato de email válido
- El campo contraseña es requerido y debe tener mínimo 8 caracteres
- Si un campo está vacío al intentar enviar, mostrar mensaje de error específico: "El email es requerido" o "La contraseña es requerida"
- Si el email no tiene formato válido, mostrar mensaje "Ingresa un email válido"
- Los mensajes de error aparecen debajo del campo correspondiente en color rojo

**Estado del Botón:**
- El botón "Iniciar Sesión" permanece habilitado en todo momento
- Al hacer clic y durante la validación, el botón muestra un spinner y el texto cambia a "Iniciando sesión..."
- Mientras está en estado de carga, el botón está deshabilitado para prevenir múltiples envíos

**Autenticación Exitosa:**
- Si las credenciales son correctas, redirigir al usuario al dashboard (`/dashboard`)
- Guardar el token de autenticación en el cliente de forma segura
- Identificar y guardar el rol del usuario (Owner o Cajero)

**Errores de Autenticación:**
- Si el email no existe o la contraseña es incorrecta, mostrar mensaje de error genérico: "Email o contraseña incorrectos" debajo del botón de login
- Si hay error de conexión o timeout, mostrar mensaje: "No se pudo conectar al servidor. Por favor, intenta de nuevo"
- Los mensajes de error persisten hasta que el usuario modifique algún campo o intente nuevamente

**Interacción con Contraseña:**
- El campo contraseña muestra puntos/asteriscos por defecto
- Al hacer clic en el icono de ojo, la contraseña se muestra en texto plano
- Al hacer clic nuevamente en el icono (ahora ojo tachado), la contraseña vuelve a ocultarse

**Navegación:**
- Al hacer clic en "¿Olvidaste tu contraseña?", redirigir a `/recuperar-password`
- Al hacer clic en "¿No tienes cuenta? Regístrate", redirigir a `/register`
- Si el usuario ya está autenticado y accede a `/login`, redirigir automáticamente a `/dashboard`

### Escenarios

1. **Login exitoso con credenciales válidas**: Usuario ingresa email y contraseña correctos, hace clic en "Iniciar Sesión", ve spinner durante 1-2 segundos, es redirigido al dashboard
2. **Email con formato inválido**: Usuario ingresa "usuario@correo" (sin dominio completo), hace clic en "Iniciar Sesión", ve mensaje de error "Ingresa un email válido"
3. **Credenciales incorrectas**: Usuario ingresa email válido pero contraseña incorrecta, hace clic en "Iniciar Sesión", ve mensaje "Email o contraseña incorrectos"
4. **Campos vacíos**: Usuario deja ambos campos vacíos y hace clic en "Iniciar Sesión", ve mensaje de error en ambos campos: "El email es requerido" y "La contraseña es requerida"
5. **Error de conexión**: Usuario intenta login pero no hay conexión a internet, ve mensaje "No se pudo conectar al servidor. Por favor, intenta de nuevo"
6. **Mostrar/ocultar contraseña**: Usuario ingresa contraseña, hace clic en icono de ojo, ve la contraseña en texto plano, hace clic nuevamente, la contraseña se oculta
7. **Usuario ya autenticado**: Usuario autenticado intenta acceder a `/login` manualmente, es redirigido automáticamente a `/dashboard`
8. **Navegación a registro**: Usuario hace clic en "¿No tienes cuenta? Regístrate", es redirigido a página de registro
9. **Navegación a recuperar contraseña**: Usuario hace clic en "¿Olvidaste tu contraseña?", es redirigido a página de recuperación

---