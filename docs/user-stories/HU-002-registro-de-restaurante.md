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