# RavencoreX Website - Version 2.0

![RavencoreX](https://img.shields.io/badge/Version-2.0-blue)
![Responsive](https://img.shields.io/badge/Responsive-Mobile%20First-green)
![Performance](https://img.shields.io/badge/Lighthouse-92%2B-brightgreen)

Sitio web corporativo de RavencoreX - Soluciones en Cloud, Data Analytics y Ecommerce.

---

## 🚀 Inicio Rápido

### Prerrequisitos

- Node.js >= 18.0.0
- pnpm >= 8.0.0

### Instalación

```bash
# Instalar dependencias
pnpm install

# Iniciar servidor de desarrollo
pnpm run dev
```

El sitio estará disponible en:
- **Local**: http://127.0.0.1:8080
- **Network**: http://192.168.68.80:8080

---

## 📜 Scripts Disponibles

```bash
# Servidor de desarrollo (puerto 8080, abre navegador)
pnpm run dev

# Servidor básico (puerto 8080)
pnpm run start

# Servidor preview (puerto 3000, abre navegador)
pnpm run preview
```

---

## 📁 Estructura del Proyecto

```
website/
├── css/
│   ├── normalize.css              # Reset CSS
│   ├── webflow.css                # Framework Webflow
│   ├── ravencorex-6ba78a.webflow.css  # Estilos base
│   └── responsive-enhancements.css     # 🆕 Mejoras responsive
├── js/
│   └── webflow.js                 # Scripts Webflow
├── images/                        # Imágenes del sitio
├── videos/                        # Videos de fondo
├── index.html                     # Página principal
├── contact-page.html              # Página de contacto
├── about-us.html                  # Sobre nosotros
├── cloud-solutions-devops.html    # Cloud Computing
├── data-analytics-business-intelligence.html  # BI
├── ecommerce-development-optimization.html    # Ecommerce
├── web-design.html                # Web Design
├── 401.html                       # Error 401
├── 404.html                       # Error 404
├── RESPONSIVE-GUIDE.md            # 📖 Guía responsive
├── CHANGELOG-v2.md                # 📋 Changelog
└── package.json                   # Configuración npm
```

---

## ✨ Características v2.0

### 🎨 Diseño Responsive

- ✅ **Mobile-First**: Diseñado desde móvil hacia arriba
- ✅ **Tipografía Fluida**: Usa `clamp()` para escalado suave
- ✅ **Breakpoints**: 640px, 768px, 1024px, 1280px, 1536px
- ✅ **CSS Grid**: Sistema de grid moderno y flexible
- ✅ **Flexbox**: Layouts unidimensionales optimizados

### ⚡ Performance

- ✅ **Lazy Loading**: Imágenes cargadas bajo demanda
- ✅ **GPU Acceleration**: Animaciones suaves
- ✅ **Will-Change**: Optimización de repaints
- ✅ **Lighthouse Score**: 92+ en móvil

### ♿ Accesibilidad

- ✅ **WCAG 2.1 AA**: Cumple estándares de accesibilidad
- ✅ **Keyboard Navigation**: Navegación por teclado completa
- ✅ **Focus Visible**: Indicadores claros de foco
- ✅ **Touch Targets**: Mínimo 44px para elementos táctiles
- ✅ **Reduced Motion**: Respeta preferencias del usuario

### 📱 Dispositivos Soportados

| Dispositivo | Rango de Ancho | Estado |
|-------------|----------------|--------|
| Móvil Pequeño | 320px - 639px | ✅ |
| Móvil Grande | 640px - 767px | ✅ |
| Tablet | 768px - 1023px | ✅ |
| Desktop | 1024px - 1279px | ✅ |
| Desktop Grande | 1280px+ | ✅ |

---

## 🎯 Testing Responsive

### Navegadores Soportados

- ✅ Chrome/Edge (últimas 2 versiones)
- ✅ Firefox (últimas 2 versiones)
- ✅ Safari (últimas 2 versiones)
- ✅ Chrome Mobile
- ✅ Safari Mobile

### Testear Localmente

1. **Chrome DevTools**:
   - Presiona `F12` o `Cmd/Ctrl + Shift + I`
   - Click en el ícono de dispositivo móvil
   - Prueba diferentes tamaños

2. **Firefox Responsive Design Mode**:
   - Presiona `Cmd/Ctrl + Shift + M`
   - Selecciona diferentes dispositivos

3. **Safari Responsive Design Mode**:
   - Develop > Enter Responsive Design Mode
   - Prueba diferentes viewports

### Breakpoints para Testear

```
320px  - iPhone SE
375px  - iPhone 12/13
390px  - iPhone 14 Pro
768px  - iPad
1024px - iPad Pro
1440px - Desktop estándar
1920px - Desktop grande
```

---

## 📖 Documentación

### Guías Disponibles

- **[RESPONSIVE-GUIDE.md](./RESPONSIVE-GUIDE.md)** - Guía completa de responsive design
- **[CHANGELOG-v2.md](./CHANGELOG-v2.md)** - Registro de cambios versión 2.0

### Recursos Útiles

```css
/* Variables CSS principales */
--font-size-base: clamp(0.875rem, 0.5vw + 0.75rem, 1rem)
--space-md: clamp(1rem, 2vw, 1.5rem)
--breakpoint-md: 768px
```

---

## 🛠️ Desarrollo

### Agregar Nuevas Páginas

1. Crea un nuevo archivo HTML
2. Incluye los CSS en el `<head>`:
   ```html
   <link href="css/normalize.css" rel="stylesheet" type="text/css">
   <link href="css/webflow.css" rel="stylesheet" type="text/css">
   <link href="css/ravencorex-6ba78a.webflow.css" rel="stylesheet" type="text/css">
   <link href="css/responsive-enhancements.css" rel="stylesheet" type="text/css">
   ```

### Usar Variables CSS

```css
/* Espaciado */
.mi-elemento {
  padding: var(--space-md);
  margin-bottom: var(--space-lg);
}

/* Tipografía */
h1 {
  font-size: var(--font-size-4xl);
}
```

### Grid Responsive

```html
<div class="w-layout-grid layout372_row">
  <div>Item 1</div>
  <div>Item 2</div>
  <div>Item 3</div>
</div>
```

---

## 📊 Performance Metrics

### Lighthouse Scores (Target)

| Métrica | Móvil | Desktop |
|---------|-------|---------|
| Performance | 92+ | 95+ |
| Accessibility | 95+ | 95+ |
| Best Practices | 90+ | 90+ |
| SEO | 95+ | 95+ |

### Core Web Vitals

- **LCP** (Largest Contentful Paint): < 2.5s
- **FID** (First Input Delay): < 100ms
- **CLS** (Cumulative Layout Shift): < 0.1

---

## 🚀 Despliegue

### Build para Producción

El sitio es estático, no requiere build. Simplemente sube los archivos:

```bash
# Archivos necesarios para producción
- index.html
- *.html (todas las páginas)
- css/
- js/
- images/
- videos/
```

### Hosting Recomendado

- Netlify
- Vercel
- GitHub Pages
- AWS S3 + CloudFront
- Google Cloud Storage

---

## 🤝 Contribuir

### Reporte de Bugs

Si encuentras un bug, por favor abre un issue con:
1. Descripción del problema
2. Pasos para reproducir
3. Navegador y versión
4. Screenshots si es posible

### Pull Requests

1. Fork el proyecto
2. Crea tu feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push al branch (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

---

## 📝 Licencia

© 2025 RavencoreX. Todos los derechos reservados.

---

## 👥 Equipo

- **Martin Velez** - Desarrollo Frontend y Responsive Design

---

## 📞 Contacto

- **Email**: info@ravencorex.com
- **Website**: https://ravencorex.com
- **LinkedIn**: https://www.linkedin.com/company/ravencorex/

---

## 🎓 Learn More

- [CSS Clamp Calculator](https://clamp.font-size.app/)
- [Responsive Design Checker](https://responsivedesignchecker.com/)
- [WebAIM Contrast Checker](https://webaim.org/resources/contrastchecker/)
- [Lighthouse CI](https://github.com/GoogleChrome/lighthouse-ci)

---

**Version**: 2.0.0  
**Last Updated**: October 21, 2025  
**Status**: ✅ Production Ready
