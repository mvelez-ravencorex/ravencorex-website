# Sistema de Componentes Reutilizables - RavencoreX v2

## Filosofía de Diseño

✅ **Mobile-First**: Diseñar primero para móvil, luego escalar
✅ **Componentes Atómicos**: Pequeños, reutilizables, combinables
✅ **Normalización CSS**: Variables centralizadas, sin repetición
✅ **Responsive por defecto**: Cada componente funciona en todos los tamaños
✅ **Accesibilidad**: WCAG 2.1 AA compliance

## Estructura de Componentes

### 1. LAYOUT COMPONENTS (Estructura)

#### Container
```html
<div class="container">
  <!-- Contenido centrado con max-width -->
</div>
```
**Variantes:**
- `.container-sm` - max-width: 768px
- `.container-md` - max-width: 992px
- `.container-lg` - max-width: 1200px (default)
- `.container-xl` - max-width: 1400px
- `.container-full` - width: 100%

#### Section
```html
<section class="section">
  <div class="container">
    <!-- Contenido -->
  </div>
</section>
```
**Variantes:**
- `.section-sm` - padding: 2rem 0
- `.section-md` - padding: 4rem 0 (default)
- `.section-lg` - padding: 6rem 0
- `.section-xl` - padding: 8rem 0

#### Grid
```html
<div class="grid grid-cols-3 gap-lg">
  <div>Item 1</div>
  <div>Item 2</div>
  <div>Item 3</div>
</div>
```
**Modificadores:**
- `.grid-cols-1` hasta `.grid-cols-12`
- `.grid-cols-md-2` - 2 columnas en tablet+
- `.grid-cols-lg-3` - 3 columnas en desktop+
- `.gap-xs`, `.gap-sm`, `.gap-md`, `.gap-lg`, `.gap-xl`

---

### 2. HERO COMPONENTS

#### Hero Simple
```html
<header class="hero hero-height-md">
  <div class="hero-content">
    <h1 class="hero-title">Título Principal</h1>
    <p class="hero-subtitle">Subtítulo descriptivo</p>
    <div class="hero-actions">
      <a href="#" class="btn btn-primary">CTA Principal</a>
      <a href="#" class="btn btn-secondary">CTA Secundario</a>
    </div>
  </div>
  <div class="hero-bg">
    <video autoplay loop muted playsinline>
      <source src="video.mp4" type="video/mp4">
    </video>
    <div class="hero-overlay"></div>
  </div>
</header>
```

**Alturas:**
- `.hero-height-sm` - 400px
- `.hero-height-md` - 500px (default)
- `.hero-height-lg` - 600px
- `.hero-height-xl` - 800px
- `.hero-height-full` - 100vh

**Estilos de fondo:**
- `.hero-bg-dark` - overlay oscuro
- `.hero-bg-light` - overlay claro
- `.hero-bg-gradient` - gradient overlay

---

### 3. CARD COMPONENTS

#### Card Base
```html
<div class="card">
  <div class="card-image">
    <img src="image.jpg" alt="">
  </div>
  <div class="card-content">
    <h3 class="card-title">Título</h3>
    <p class="card-description">Descripción</p>
    <a href="#" class="card-link">Leer más →</a>
  </div>
</div>
```

**Variantes:**
- `.card-horizontal` - layout horizontal
- `.card-featured` - destacada con sombra
- `.card-hover-lift` - levanta al hacer hover

---

### 4. BUTTON COMPONENTS

#### Buttons
```html
<button class="btn btn-primary">Botón Primario</button>
<button class="btn btn-secondary">Botón Secundario</button>
<button class="btn btn-outline">Botón Outline</button>
<button class="btn btn-text">Botón Texto</button>
```

**Tamaños:**
- `.btn-sm` - pequeño
- `.btn-md` - medio (default)
- `.btn-lg` - grande

**Estados:**
- `.btn-loading` - mostrando loader
- `.btn-disabled` - deshabilitado
- `:hover`, `:focus`, `:active`

---

### 5. SECTION COMPONENTS

#### Feature Section (3 columnas)
```html
<section class="section section-features">
  <div class="container">
    <div class="section-header text-center">
      <h2 class="section-title">Nuestros Servicios</h2>
      <p class="section-subtitle">Subtítulo</p>
    </div>

    <div class="grid grid-cols-1 grid-cols-md-2 grid-cols-lg-3 gap-lg">
      <div class="feature-card">
        <div class="feature-icon">
          <svg>...</svg>
        </div>
        <h3 class="feature-title">Título</h3>
        <p class="feature-description">Descripción</p>
        <a href="#" class="feature-link">Ver más →</a>
      </div>
      <!-- Repetir para más features -->
    </div>
  </div>
</section>
```

#### CTA Section
```html
<section class="section section-cta bg-dark text-white">
  <div class="container text-center">
    <h2 class="cta-title">¿Listo para comenzar?</h2>
    <p class="cta-subtitle">Descripción</p>
    <div class="cta-actions">
      <a href="#" class="btn btn-primary">Comenzar Ahora</a>
      <a href="#" class="btn btn-outline-white">Contactar</a>
    </div>
  </div>
  <div class="cta-bg">
    <video autoplay loop muted playsinline>
      <source src="bg-video.mp4" type="video/mp4">
    </video>
  </div>
</section>
```

---

## CSS Custom Properties (Variables)

### Espaciado
```css
--space-xs: 0.25rem;   /* 4px */
--space-sm: 0.5rem;    /* 8px */
--space-md: 1rem;      /* 16px */
--space-lg: 1.5rem;    /* 24px */
--space-xl: 2rem;      /* 32px */
--space-2xl: 3rem;     /* 48px */
--space-3xl: 4rem;     /* 64px */
```

### Colores
```css
--color-primary: #4d65ff;
--color-secondary: #6c757d;
--color-success: #28a745;
--color-danger: #dc3545;
--color-warning: #ffc107;
--color-info: #17a2b8;

--color-text: #212529;
--color-text-light: #6c757d;
--color-bg: #ffffff;
--color-bg-light: #f8f9fa;
```

### Tipografía
```css
--font-size-xs: 0.75rem;
--font-size-sm: 0.875rem;
--font-size-base: 1rem;
--font-size-lg: 1.125rem;
--font-size-xl: 1.25rem;
--font-size-2xl: 1.5rem;
--font-size-3xl: 2rem;
--font-size-4xl: 2.5rem;
```

### Breakpoints
```css
/* Mobile: < 768px */
/* Tablet: 768px - 991px */
/* Desktop: >= 992px */

@media (min-width: 768px) { /* tablet+ */ }
@media (min-width: 992px) { /* desktop+ */ }
```

---

## Utilidades CSS

### Spacing
```css
.mt-sm { margin-top: var(--space-sm); }
.mb-md { margin-bottom: var(--space-md); }
.p-lg { padding: var(--space-lg); }
/* ... más variantes */
```

### Text
```css
.text-center { text-align: center; }
.text-left { text-align: left; }
.text-right { text-align: right; }
.text-white { color: white; }
.text-dark { color: var(--color-text); }
```

### Display
```css
.d-none { display: none; }
.d-block { display: block; }
.d-flex { display: flex; }
.d-grid { display: grid; }
```

### Flex
```css
.flex-row { flex-direction: row; }
.flex-column { flex-direction: column; }
.justify-center { justify-content: center; }
.align-center { align-items: center; }
.gap-md { gap: var(--space-md); }
```

---

## Guía de Uso

### 1. Estructura de Página Típica

```html
<!DOCTYPE html>
<html lang="es">
<head>
  <!-- Meta tags -->
  <link href="css/normalize.css" rel="stylesheet">
  <link href="css/webflow.css" rel="stylesheet">
  <link href="css/ravencorex-6ba78a.webflow.css" rel="stylesheet">
  <link href="css/custom-variables.css" rel="stylesheet">
  <link href="css/custom-overrides.css" rel="stylesheet">
</head>
<body>
  <!-- Navbar -->
  <nav class="navbar">...</nav>

  <!-- Hero -->
  <header class="hero hero-height-md">...</header>

  <!-- Main Content -->
  <main>
    <section class="section">...</section>
    <section class="section bg-light">...</section>
    <section class="section">...</section>
  </main>

  <!-- Footer -->
  <footer class="footer">...</footer>

  <script src="js/webflow.js"></script>
</body>
</html>
```

### 2. Responsive Grid Example

```html
<!-- 1 col en móvil, 2 en tablet, 3 en desktop -->
<div class="grid grid-cols-1 grid-cols-md-2 grid-cols-lg-3 gap-lg">
  <div class="card">...</div>
  <div class="card">...</div>
  <div class="card">...</div>
</div>
```

### 3. CTA Section Example

```html
<section class="section section-cta bg-primary text-white">
  <div class="container text-center">
    <h2 class="mb-md">¿Listo para transformar tu negocio?</h2>
    <p class="mb-lg">Contáctanos hoy y descubre cómo podemos ayudarte</p>
    <a href="/contact" class="btn btn-white btn-lg">Comenzar Ahora</a>
  </div>
</section>
```

---

## Principios de Desarrollo

1. **Mobile First**: Diseñar primero para móvil
2. **Progressive Enhancement**: Agregar features para pantallas más grandes
3. **Semantic HTML**: Usar etiquetas semánticas (`<header>`, `<main>`, `<section>`, etc.)
4. **Accesibilidad**: ARIA labels, contraste de colores, keyboard navigation
5. **Performance**: Lazy loading, optimización de imágenes, minificación
6. **Consistencia**: Usar componentes y variables, evitar estilos arbitrarios
7. **Documentación**: Documentar nuevos componentes en este archivo

---

## Checklist para Nuevos Componentes

- [ ] Funciona en móvil (< 768px)
- [ ] Funciona en tablet (768px - 991px)
- [ ] Funciona en desktop (>= 992px)
- [ ] Usa variables CSS en lugar de valores hardcoded
- [ ] Tiene clases reutilizables
- [ ] Es accesible (ARIA, keyboard, contrast)
- [ ] Está documentado
- [ ] Tiene estados hover/focus/active
- [ ] Performance optimizado (imágenes, videos)

---

## Changelog

### v2.0 (2025-10-21)
- ✨ Sistema de componentes modular creado
- ✨ Variables CSS centralizadas
- ✨ Grid system responsive
- ✨ Hero components con alturas controladas
- 📝 Documentación completa
