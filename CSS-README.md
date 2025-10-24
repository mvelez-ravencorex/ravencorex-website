# CSS Architecture Documentation - RavencoreX Website v2

## Overview

Esta es la nueva arquitectura CSS organizada, escalable y mantenible para el sitio web de RavencoreX. Se ha reorganizado completamente para eliminar conflictos de estilos y facilitar futuras modificaciones.

## Estructura de Archivos CSS

```
css/
├── normalize.css              # CSS resets (NO MODIFICAR)
├── webflow.css                # Webflow framework (NO MODIFICAR)
├── ravencorex-6ba78a.webflow.css  # Estilos base de Webflow (MÍNIMAS MODIFICACIONES)
├── custom-variables.css       # Variables CSS centralizadas ✨ NUEVO
└── custom-overrides.css       # Todas las customizaciones ✨ NUEVO
```

## Orden de Carga en HTML

```html
<head>
  <!-- 1. Normalización de navegadores -->
  <link href="css/normalize.css" rel="stylesheet" type="text/css">

  <!-- 2. Framework de Webflow -->
  <link href="css/webflow.css" rel="stylesheet" type="text/css">

  <!-- 3. Estilos base exportados de Webflow -->
  <link href="css/ravencorex-6ba78a.webflow.css" rel="stylesheet" type="text/css">

  <!-- 4. Variables CSS personalizadas -->
  <link href="css/custom-variables.css" rel="stylesheet" type="text/css">

  <!-- 5. Overrides y customizaciones (CARGA AL FINAL) -->
  <link href="css/custom-overrides.css" rel="stylesheet" type="text/css">
</head>
```

## Archivo: custom-variables.css

### Propósito
Define todas las variables CSS (design tokens) del proyecto.

### Contenido
- **Colores**: Primary, secundarios, texto, fondos
- **Espaciado**: Escala de spacing (xxs, xs, sm, md, lg, xl, 2xl, 3xl)
- **Tipografía**: Font sizes, weights, line heights
- **Layout**: Alturas de hero, navbar, containers
- **Transiciones**: Duraciones estándar
- **Z-index**: Escala de capas

### Ejemplo de uso
```css
.my-element {
  padding: var(--space-md);
  color: var(--color-primary);
  font-size: var(--font-size-lg);
}
```

## Archivo: custom-overrides.css

### Propósito
Contiene TODAS las customizaciones y modificaciones a los estilos base de Webflow.

### Secciones organizadas

#### 1. NAVIGATION
- Spacing del navbar
- Gap entre menu items
- Padding de links

#### 2. HERO SECTIONS
- Altura del hero (400px)
- Padding reducido
- Video overlay

#### 3. FILTERS
- Estilos de botones de filtro
- Estado seleccionado (negro con texto blanco)
- Estados hover

#### 4. BUTTONS
- Enhancements de botones

#### 5. FORMS
- Estilos de inputs
- Focus states

#### 6. RESPONSIVE UTILITIES
- Media queries mobile, tablet, desktop

#### 7. UTILITY CLASSES
- Text alignment
- Spacing utilities (mt-*, mb-*, pt-*, pb-*)
- Display utilities
- Flexbox utilities

#### 8. ACCESSIBILITY
- Focus visible
- Skip links
- Reduced motion support

## Cómo Hacer Cambios

### ✅ Hacer esto
1. **Para cambiar valores globales**: Editar `custom-variables.css`
2. **Para agregar/modificar estilos**: Editar `custom-overrides.css`
3. **Usar variables CSS**: Siempre que sea posible

### ❌ No hacer esto
1. **NO modificar** `normalize.css`
2. **NO modificar** `webflow.css`
3. **MINIMIZAR modificaciones** a `ravencorex-6ba78a.webflow.css`
4. **NO usar** `!important` (excepto cuando sea absolutamente necesario)

## Ejemplos Prácticos

### Cambiar la altura del hero
```css
/* En custom-variables.css */
:root {
  --hero-height-contact: 400px; /* Cambiar este valor */
}
```

### Cambiar el spacing del navbar
```css
/* En custom-variables.css */
:root {
  --navbar-gap: 0.25rem; /* Cambiar este valor */
}
```

### Agregar un nuevo componente
```css
/* En custom-overrides.css */

/* ===================================
   MI NUEVO COMPONENTE
   =================================== */

.mi-componente {
  padding: var(--space-md);
  background: var(--color-bg-primary);
  border-radius: var(--radius-md);
}

.mi-componente:hover {
  background: var(--color-bg-secondary);
  transition: background var(--transition-base);
}
```

## Filtros de Campaña

Los filtros para campañas (como se solicitó) están implementados en `custom-overrides.css`:

### HTML Structure
```html
<div class="filter-container">
  <button class="filter-button">Todas</button>
  <button class="filter-button selected">Ventas Snoozy Dream</button>
  <button class="filter-button">Ventas Snoozy Dream - Copia</button>
</div>
```

### Estilos
- Botón por defecto: fondo blanco, borde gris
- Botón hover: borde azul
- Botón seleccionado: **fondo negro, texto blanco**

## Responsive Breakpoints

```css
/* Mobile */
@media (max-width: 767px) { }

/* Tablet */
@media (min-width: 768px) and (max-width: 991px) { }

/* Desktop */
@media (min-width: 992px) { }
```

## Testing

Después de hacer cambios:

1. ✅ Verificar en Chrome DevTools
2. ✅ Probar en mobile (< 768px)
3. ✅ Probar en tablet (768px - 991px)
4. ✅ Probar en desktop (> 992px)
5. ✅ Verificar accesibilidad (keyboard navigation)

## Migración de Páginas

Para migrar otras páginas HTML al nuevo sistema:

1. Abrir el archivo HTML
2. Reemplazar la sección de CSS:

```html
<!-- ANTES -->
<link href="css/responsive-enhancements.css" rel="stylesheet" type="text/css">

<!-- DESPUÉS -->
<link href="css/custom-variables.css" rel="stylesheet" type="text/css">
<link href="css/custom-overrides.css" rel="stylesheet" type="text/css">
```

## Beneficios de esta Arquitectura

✅ **Separación clara de responsabilidades**
✅ **Fácil de mantener y escalar**
✅ **Sin guerras de especificidad**
✅ **Variables reutilizables**
✅ **Cambios globales simples**
✅ **Git-friendly** (cambios claros en diffs)
✅ **Documentado y organizado**

## Soporte

Para preguntas o problemas:
1. Revisar este README
2. Consultar `CSS-ARCHITECTURE.md` para detalles técnicos
3. Verificar que el orden de carga de CSS sea correcto

## Changelog

### v2.0 (2025-10-21)
- ✨ Creado `custom-variables.css` con design tokens
- ✨ Creado `custom-overrides.css` con todas las customizaciones
- 🔧 Reorganizado orden de carga de CSS
- 🔧 Implementados filtros de campaña con estado seleccionado
- 🔧 Hero height: 400px (desktop), 350px (tablet), 300px (mobile)
- 🔧 Navbar gap reducido para items más juntos
- 📝 Documentación completa
