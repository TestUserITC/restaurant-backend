# Historias de Usuario - Autenticación y Onboarding
## MVP SaaS Administración de Restaurantes

---

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

## HU-002: Registro de Restaurante

### Descripción
Como nuevo usuario, quiero registrar mi restaurante en el sistema para poder empezar a usar el punto de venta y las funcionalidades de administración.

### Criterios de Aceptación

**Estructura y Contenido de la Pantalla:**
- La página de registro muestra un formulario centrado con:
  - Logo o nombre de la aplicación
  - Título "Crea tu cuenta"
  - Subtítulo "Comienza a administrar tu restaurante hoy"
  - Campos del formulario organizados verticalmente:
    - Campo "Nombre del restaurante" (requerido, placeholder: "Ej: Restaurante El Sabor")
    - Campo "Tu nombre completo" (requerido, placeholder: "Ej: Juan Pérez")
    - Campo "Correo electrónico" (requerido, placeholder: "tu@correo.com")
    - Campo "Contraseña" (requerido, placeholder: "Mínimo 8 caracteres", con opción de mostrar/ocultar)
    - Campo "Confirmar contraseña" (requerido, placeholder: "Repite tu contraseña", con opción de mostrar/ocultar)
    - Campo "Dirección del restaurante" (opcional, placeholder: "Calle, número, ciudad")
  - Checkbox "Acepto los términos y condiciones" (requerido)
  - Botón "Crear cuenta" (primario)
  - Texto "¿Ya tienes cuenta? Inicia sesión" con link al login

**Validaciones de Campos:**
- Nombre del restaurante: requerido, mínimo 3 caracteres, máximo 100 caracteres
- Tu nombre completo: requerido, mínimo 3 caracteres, máximo 100 caracteres
- Correo electrónico: requerido, formato de email válido
- Contraseña: requerida, mínimo 8 caracteres, debe contener al menos una letra y un número
- Confirmar contraseña: requerida, debe coincidir exactamente con el campo "Contraseña"
- Dirección: opcional, máximo 200 caracteres
- Checkbox términos: debe estar marcado para poder continuar

**Mensajes de Error Específicos:**
- Si nombre del restaurante < 3 caracteres: "El nombre debe tener al menos 3 caracteres"
- Si nombre completo < 3 caracteres: "El nombre debe tener al menos 3 caracteres"
- Si email es inválido: "Ingresa un email válido"
- Si email ya está registrado: "Este email ya está en uso. Por favor, usa otro email o inicia sesión"
- Si contraseña < 8 caracteres: "La contraseña debe tener al menos 8 caracteres"
- Si contraseña no contiene letra y número: "La contraseña debe contener al menos una letra y un número"
- Si confirmar contraseña no coincide: "Las contraseñas no coinciden"
- Si checkbox no está marcado: "Debes aceptar los términos y condiciones"

**Estado del Botón:**
- El botón "Crear cuenta" está habilitado en todo momento
- Al hacer clic, se validan todos los campos antes de enviar
- Durante el envío, el botón muestra spinner y texto "Creando cuenta..."
- Mientras está en estado de carga, el botón está deshabilitado

**Registro Exitoso:**
- Si el registro es exitoso, crear automáticamente:
  - Una cuenta con el email proporcionado
  - Un restaurante con el nombre proporcionado
  - Una sucursal por defecto asociada al restaurante
  - Asignar rol "Owner" al usuario
- Después de crear la cuenta, redirigir automáticamente a `/dashboard`
- Mostrar mensaje de bienvenida temporal: "¡Bienvenido! Tu cuenta ha sido creada exitosamente"

**Campos con Mostrar/Ocultar Contraseña:**
- Ambos campos de contraseña (Contraseña y Confirmar contraseña) tienen icono de ojo independientes
- El comportamiento de mostrar/ocultar es el mismo que en login

**Términos y Condiciones:**
- El texto "términos y condiciones" es un link que abre los términos en una nueva pestaña
- El checkbox permanece desmarcado por defecto
- Al hacer clic en el checkbox, alterna entre marcado/desmarcado

**Navegación:**
- Al hacer clic en "Inicia sesión", redirigir a `/login`
- Si el usuario ya está autenticado y accede a `/register`, redirigir automáticamente a `/dashboard`

### Escenarios

1. **Registro exitoso con datos válidos**: Usuario completa todos los campos correctamente, marca términos, hace clic en "Crear cuenta", ve spinner, es redirigido al dashboard con mensaje de bienvenida
2. **Email ya registrado**: Usuario intenta registrarse con un email que ya existe en el sistema, ve mensaje "Este email ya está en uso. Por favor, usa otro email o inicia sesión"
3. **Contraseñas no coinciden**: Usuario ingresa "Password123" y "Password456" en los campos de contraseña, intenta crear cuenta, ve mensaje "Las contraseñas no coinciden" en el campo "Confirmar contraseña"
4. **Contraseña débil sin números**: Usuario ingresa "password" (solo letras), ve mensaje "La contraseña debe contener al menos una letra y un número"
5. **Contraseña débil con menos de 8 caracteres**: Usuario ingresa "Pass1", ve mensaje "La contraseña debe tener al menos 8 caracteres"
6. **Nombre del restaurante muy corto**: Usuario ingresa "Ab" en nombre del restaurante, ve mensaje "El nombre debe tener al menos 3 caracteres"
7. **Checkbox de términos sin marcar**: Usuario completa todos los campos pero no marca términos, intenta crear cuenta, ve mensaje "Debes aceptar los términos y condiciones"
8. **Campos vacíos**: Usuario hace clic en "Crear cuenta" sin llenar nada, ve mensajes de error en todos los campos requeridos
9. **Error de conexión durante registro**: Usuario completa formulario pero hay error de red, ve mensaje "No se pudo crear la cuenta. Por favor, intenta de nuevo"
10. **Dirección opcional no completada**: Usuario completa todos los campos requeridos pero deja dirección vacía, el registro se completa exitosamente sin problemas
11. **Mostrar/ocultar contraseñas**: Usuario hace clic en ojo de "Contraseña", ve texto plano, hace clic en ojo de "Confirmar contraseña", ve texto plano en ese campo también
12. **Usuario autenticado intenta registrarse**: Usuario ya logueado intenta acceder a `/register`, es redirigido automáticamente a `/dashboard`
13. **Click en términos y condiciones**: Usuario hace clic en link "términos y condiciones", se abre nueva pestaña con los términos, usuario permanece en página de registro

---

## HU-003: Recuperar Contraseña

### Descripción
Como usuario registrado que olvidó su contraseña, quiero poder restablecerla mediante mi correo electrónico para poder volver a acceder al sistema.

### Criterios de Aceptación

**Estructura y Contenido de la Pantalla:**
- La página de recuperación muestra un formulario centrado con:
  - Logo o nombre de la aplicación
  - Título "Recuperar contraseña"
  - Texto explicativo: "Ingresa tu correo electrónico y te enviaremos un link para restablecer tu contraseña"
  - Campo de texto para email con placeholder "Correo electrónico"
  - Botón "Enviar link de recuperación" (primario)
  - Link "Volver al login" debajo del botón

**Validaciones de Campos:**
- El campo email es requerido
- El campo email debe tener formato válido
- Si el campo está vacío al enviar, mostrar mensaje: "El email es requerido"
- Si el formato es inválido, mostrar mensaje: "Ingresa un email válido"

**Estado del Botón:**
- El botón "Enviar link de recuperación" está habilitado en todo momento
- Al hacer clic, el botón muestra spinner y texto cambia a "Enviando..."
- Mientras está en estado de carga, el botón está deshabilitado

**Envío Exitoso:**
- Si el email existe en el sistema, mostrar mensaje de éxito: "Te hemos enviado un link de recuperación a tu correo. Por favor, revisa tu bandeja de entrada"
- Si el email NO existe en el sistema, mostrar el MISMO mensaje de éxito (para no revelar si el email está registrado)
- El mensaje de éxito se muestra en un banner verde en la parte superior del formulario
- El formulario permanece visible para permitir reintentos
- El email enviado contiene un link único con token de recuperación válido por 1 hora

**Manejo de Errores:**
- Si hay error de conexión, mostrar mensaje: "No se pudo enviar el email. Por favor, intenta de nuevo"
- Si el servidor responde con error, mostrar mensaje genérico: "Hubo un problema al procesar tu solicitud. Por favor, intenta más tarde"

**Link de Recuperación (Email):**
- El email recibido contiene:
  - Asunto: "Recuperación de contraseña - [Nombre App]"
  - Mensaje personalizado con nombre del restaurante si está disponible
  - Botón o link "Restablecer mi contraseña" que redirige a `/restablecer-password?token=xyz123`
  - Mensaje indicando que el link expira en 1 hora
  - Mensaje de seguridad: "Si no solicitaste este cambio, ignora este email"

**Página de Restablecer Contraseña:**
- Al hacer clic en el link del email, el usuario es redirigido a una página con:
  - Título "Establece tu nueva contraseña"
  - Campo "Nueva contraseña" (requerido, con mostrar/ocultar)
  - Campo "Confirmar nueva contraseña" (requerido, con mostrar/ocultar)
  - Botón "Restablecer contraseña"

**Validaciones en Página de Restablecimiento:**
- Nueva contraseña: mínimo 8 caracteres, debe contener al menos una letra y un número
- Confirmar nueva contraseña: debe coincidir exactamente con nueva contraseña
- Los mensajes de error son los mismos que en la página de registro

**Restablecimiento Exitoso:**
- Si el restablecimiento es exitoso, mostrar mensaje: "Tu contraseña ha sido actualizada exitosamente"
- Redirigir automáticamente al login después de 2 segundos
- Mostrar contador regresivo: "Redirigiendo al login en 2 segundos..."

**Tokens Inválidos o Expirados:**
- Si el token es inválido o ya fue usado, mostrar mensaje: "Este link de recuperación no es válido o ya fue usado"
- Si el token está expirado (más de 1 hora), mostrar mensaje: "Este link de recuperación ha expirado. Por favor, solicita uno nuevo"
- En ambos casos, mostrar botón "Solicitar nuevo link" que redirige a `/recuperar-password`

**Navegación:**
- Al hacer clic en "Volver al login" en página de recuperación, redirigir a `/login`
- Si el usuario está autenticado y accede a `/recuperar-password`, redirigir a `/dashboard`

### Escenarios

1. **Recuperación exitosa con email registrado**: Usuario ingresa email registrado, hace clic en "Enviar link", ve mensaje de éxito, recibe email con link de recuperación
2. **Email no registrado en sistema**: Usuario ingresa email que no existe, hace clic en "Enviar link", ve el mismo mensaje de éxito (por seguridad), pero no recibe email
3. **Email con formato inválido**: Usuario ingresa "usuario@" (incompleto), intenta enviar, ve mensaje "Ingresa un email válido"
4. **Campo vacío**: Usuario hace clic en "Enviar link" sin ingresar email, ve mensaje "El email es requerido"
5. **Error de conexión al enviar**: Usuario ingresa email válido pero hay error de red, ve mensaje "No se pudo enviar el email. Por favor, intenta de nuevo"
6. **Restablecimiento exitoso**: Usuario recibe email, hace clic en link, ingresa "NewPass123" en ambos campos, hace clic en "Restablecer contraseña", ve mensaje de éxito, es redirigido a login después de 2 segundos
7. **Contraseñas no coinciden en restablecimiento**: Usuario ingresa "NewPass123" y "NewPass456", intenta restablecer, ve mensaje "Las contraseñas no coinciden"
8. **Nueva contraseña débil**: Usuario intenta establecer "pass123" (menos de 8 caracteres), ve mensaje "La contraseña debe tener al menos 8 caracteres"
9. **Token expirado**: Usuario hace clic en link de recuperación después de 2 horas, ve mensaje "Este link de recuperación ha expirado. Por favor, solicita uno nuevo" con botón para solicitar nuevo link
10. **Token inválido o ya usado**: Usuario intenta usar el mismo link dos veces, la segunda vez ve mensaje "Este link de recuperación no es válido o ya fue usado"
11. **Reenvío de email de recuperación**: Usuario solicita recuperación, espera y no ve el email, vuelve a `/recuperar-password`, ingresa email nuevamente, recibe nuevo email con nuevo token
12. **Usuario autenticado intenta recuperar**: Usuario con sesión activa intenta acceder a `/recuperar-password`, es redirigido automáticamente a `/dashboard`
13. **Click en Volver al login**: Usuario en página de recuperación hace clic en "Volver al login", es redirigido a página de login

---

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

## HU-005: Roles de Usuario (Owner vs Cajero)

### Descripción
Como sistema, necesito diferenciar entre roles de usuario (Owner y Cajero) para mostrar u ocultar funcionalidades según los permisos de cada rol.

### Criterios de Aceptación

**Rol de Owner:**
- Tiene acceso completo a todas las funcionalidades del sistema
- Puede acceder a:
  - Dashboard (con todos los KPIs)
  - Gestión de menú (categorías y productos)
  - POS (punto de venta)
  - Órdenes
  - Historial de ventas
  - Configuración del restaurante
- El menú lateral/navegación muestra todas las opciones disponibles

**Rol de Cajero:**
- Tiene acceso limitado solo a funcionalidades operativas
- Puede acceder a:
  - Dashboard (solo vista de órdenes abiertas y básicos)
  - POS (punto de venta)
  - Órdenes (ver y cambiar estados)
- NO puede acceder a:
  - Gestión de menú
  - Historial de ventas
  - Configuración
- El menú lateral/navegación solo muestra las opciones permitidas (Dashboard, POS, Órdenes)

**Asignación de Rol:**
- El primer usuario que registra el restaurante (usuario que crea la cuenta) recibe automáticamente rol "Owner"
- Solo el Owner puede invitar/crear nuevos usuarios con rol "Cajero" (esto está fuera del MVP pero el sistema debe estar preparado)

**Protección de Rutas por Rol:**
- Si un Cajero intenta acceder manualmente a una URL protegida (ej: `/menu`, `/sales`, `/settings`), mostrar página de error 403 con mensaje: "No tienes permisos para acceder a esta sección"
- Incluir botón "Volver al inicio" que redirige a `/dashboard`

**Visual de Rol:**
- En el menú lateral, mostrar el nombre del usuario y su rol debajo (ej: "Juan Pérez - Owner" o "María López - Cajero")
- El rol se muestra siempre visible para que el usuario sepa con qué permisos está operando

**Dashboard según Rol:**
- Owner ve dashboard completo con todos los KPIs (ventas del día, órdenes abiertas, ticket promedio, productos más vendidos)
- Cajero ve dashboard simplificado con solo órdenes abiertas y pendientes de preparar
- El título del dashboard es el mismo ("Dashboard"), pero el contenido varía según rol

**Navegación según Rol:**
- El menú lateral renderiza dinámicamente según el rol:
  - Owner: Dashboard, Menú, POS, Órdenes, Ventas, Configuración
  - Cajero: Dashboard, POS, Órdenes

### Escenarios

1. **Owner accede a todas las secciones**: Usuario con rol Owner navega a cada sección del menú, puede acceder sin problemas a Menú, Ventas y Configuración
2. **Cajero accede a secciones permitidas**: Usuario con rol Cajero navega a Dashboard, POS y Órdenes, puede acceder sin problemas
3. **Cajero intenta acceder a Menú**: Usuario con rol Cajero intenta navegar manualmente a `/menu`, ve página de error 403 "No tienes permisos para acceder a esta sección" con botón "Volver al inicio"
4. **Cajero intenta acceder a Ventas**: Usuario con rol Cajero intenta navegar a `/sales`, ve página 403 con mensaje de permiso denegado
5. **Cajero intenta acceder a Configuración**: Usuario con rol Cajero intenta navegar a `/settings`, ve página 403 con mensaje de permiso denegado
6. **Dashboard de Owner**: Usuario Owner accede a dashboard, ve todos los KPIs: ventas del día ($1,250.00), órdenes abiertas (5), ticket promedio ($25.00), y top 5 productos más vendidos
7. **Dashboard de Cajero**: Usuario Cajero accede a dashboard, ve solo órdenes abiertas y pendientes, NO ve KPIs de ventas ni productos más vendidos
8. **Visualización de rol en menú**: Usuario Owner ve en menú lateral "Juan Pérez - Owner", usuario Cajero ve "María López - Cajero"
9. **Registro crea Owner automáticamente**: Nuevo usuario completa registro de restaurante, al acceder por primera vez a dashboard, su rol es "Owner" y ve todas las opciones en menú lateral
10. **Menú lateral dinámico para Owner**: Usuario Owner ve en menú lateral 6 opciones: Dashboard, Menú, POS, Órdenes, Ventas, Configuración
11. **Menú lateral dinámico para Cajero**: Usuario Cajero ve en menú lateral solo 3 opciones: Dashboard, POS, Órdenes
12. **Click en Volver al inicio desde 403**: Usuario Cajero ve página 403, hace clic en "Volver al inicio", es redirigido a `/dashboard`

---

## Resumen de Rutas

| Ruta | Descripción | Roles Permitidos | Redirección |
|------|-------------|------------------|-------------|
| `/login` | Pantalla de inicio de sesión | Sin autenticar | Si autenticado → `/dashboard` |
| `/register` | Registro de restaurante | Sin autenticar | Si autenticado → `/dashboard` |
| `/recuperar-password` | Recuperación de contraseña | Sin autenticar | Si autenticado → `/dashboard` |
| `/restablecer-password` | Establecer nueva contraseña | Sin autenticar (con token) | - |
| `/dashboard` | Panel principal | Owner, Cajero | Si no autenticado → `/login` |
| `/menu` | Gestión de menú | Solo Owner | Si no autenticado → `/login`<br>Si Cajero → Error 403 |
| `/pos` | Punto de venta | Owner, Cajero | Si no autenticado → `/login` |
| `/orders` | Gestión de órdenes | Owner, Cajero | Si no autenticado → `/login` |
| `/sales` | Historial de ventas | Solo Owner | Si no autenticado → `/login`<br>Si Cajero → Error 403 |
| `/settings` | Configuración | Solo Owner | Si no autenticado → `/login`<br>Si Cajero → Error 403 |

---

## Notas Técnicas

**Almacenamiento de Sesión:**
- Se recomienda usar localStorage o sessionStorage para el token (según requerimientos de seguridad)
- El token debe incluir información del rol para evitar requests adicionales
- Implementar refresh token si la sesión debe extenderse automáticamente

**Validación de Token:**
- Validar el token en cada request al API
- Manejar respuestas 401 (no autenticado) y 403 (sin permisos) apropiadamente
- Implementar un interceptor global para requests HTTP

**Estados de Carga:**
- Mostrar skeleton loaders en lugar de spinners donde sea posible para mejor UX
- Los loaders de validación de token no deben exceder 1 segundo en condiciones normales

**Seguridad:**
- Nunca exponer contraseñas en logs o estados del cliente
- Los tokens deben tener expiración definida
- Implementar HTTPS en producción
- Rate limiting en endpoints de login y registro
