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