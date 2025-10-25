#!/usr/bin/env python3
"""
Script to translate all visible content in Spanish pages
This script reads the /ar pages and translates all visible text content
"""

import os
import re
from pathlib import Path

BASE_DIR = Path(__file__).parent
AR_DIR = BASE_DIR / "ar"

# Complete translation dictionary for all visible content
TRANSLATIONS = {
    # Hero section - Index page
    "Turning Data into Real Business Advantage with Google Cloud & Looker BI": "Convertimos Datos en Ventaja Competitiva Real con Google Cloud & Looker BI",
    "We build cloud data pipelines and BI ecosystems powered by Google Cloud and Looker — designed for scale, speed, and clarity.": "Construimos pipelines de datos en la nube y ecosistemas BI potenciados por Google Cloud y Looker — diseñados para escala, velocidad y claridad.",

    # Buttons and CTAs
    "Get Started": "Comenzar",
    "Watch Demo": "Ver Demo",
    "Learn More": "Conocer Más",
    "Request Free Audit": "Solicitar Auditoría Gratuita",
    "See Our Work": "Ver Nuestro Trabajo",
    "Book Strategy Call": "Reservar Llamada Estratégica",
    "Request Quote": "Solicitar Cotización",
    "Contact Us": "Contactanos",
    "Discover": "Descubrir",

    # Architecture section
    "Architecture": "Arquitectura",
    "End-to-End Cloud Architecture": "Arquitectura Cloud de Extremo a Extremo",
    "We design and manage data platforms on Google Cloud — from ingestion to analytics. Built for performance, governance, and scale.": "Diseñamos y gestionamos plataformas de datos en Google Cloud — desde la ingesta hasta la analítica. Construidas para rendimiento, gobernanza y escala.",
    "Strategy to Implementation": "De Estrategia a Implementación",
    "From cloud architecture design to full pipeline deployment and optimization.": "Desde el diseño de arquitectura cloud hasta el despliegue completo de pipelines y optimización.",
    "Optimized Data Layers": "Capas de Datos Optimizadas",
    "Secure cloud storage and efficient data ingestion with cost optimization.": "Almacenamiento cloud seguro e ingesta de datos eficiente con optimización de costos.",
    "Cloud architecture design, pipeline deployment, and infrastructure optimization.": "Diseño de arquitectura cloud, despliegue de pipelines y optimización de infraestructura.",
    "Efficient data ingestion, cloud storage, and cost-optimized infrastructure on Google Cloud.": "Ingesta de datos eficiente, almacenamiento cloud e infraestructura optimizada en costos en Google Cloud.",

    # Solutions section
    "Solutions": "Soluciones",
    "Scalable BI Solutions Built on Looker & BigQuery": "Soluciones BI Escalables Construidas en Looker & BigQuery",
    "From performance optimization to LookML governance and dashboard design — we build analytics that scale with your business.": "Desde optimización de rendimiento hasta gobernanza LookML y diseño de dashboards — construimos analítica que escala con tu negocio.",
    "Cloud Data Pipelines": "Pipelines de Datos en la Nube",
    "Google Cloud architecture from ingestion to warehouse — optimized for cost and performance.": "Arquitectura Google Cloud desde ingesta hasta warehouse — optimizada para costo y rendimiento.",
    "Looker & BigQuery Expertise": "Experiencia en Looker & BigQuery",
    "Custom dashboards, LookML development, and performance tuning for data teams at scale.": "Dashboards personalizados, desarrollo LookML y ajuste de rendimiento para equipos de datos a escala.",
    "Data-Driven E-commerce Growth": "Crecimiento E-commerce Basado en Datos",
    "Integrate Shopify, Tiendanube, and Meta Ads with BigQuery and Looker Studio for smarter decisions.": "Integramos Shopify, Tiendanube y Meta Ads con BigQuery y Looker Studio para decisiones más inteligentes.",
    "End-to-End Cloud Data Platform": "Plataforma de Datos Cloud de Extremo a Extremo",
    "Optimized and Secure Data Layers": "Capas de Datos Optimizadas y Seguras",
    "Dashboards That Move Decisions": "Dashboards que Impulsan Decisiones",

    # Platform sections
    "Platform": "Plataforma",
    "Growth": "Crecimiento",
    "Storage": "Almacenamiento",
    "Analytics": "Analítica",

    # Services
    "Our Services": "Nuestros Servicios",
    "What We Do": "Lo Que Hacemos",
    "Cloud Solutions & DevOps": "Soluciones Cloud & DevOps",
    "Build scalable cloud infrastructure": "Construimos infraestructura cloud escalable",
    "Business Intelligence & Analytics": "Business Intelligence & Análisis",
    "Transform data into actionable insights": "Transformamos datos en insights accionables",
    "E-Commerce Analytics": "Análisis E-Commerce",
    "Unified analytics for online stores": "Análisis unificado para tiendas online",
    "Web Design & Development": "Diseño & Desarrollo Web",
    "High-performance websites that convert": "Sitios web de alto rendimiento que convierten",

    # Footer
    "Subscribe to our newsletter for the latest updates on features and releases.": "Suscribite a nuestro newsletter para recibir las últimas novedades sobre funcionalidades y lanzamientos.",
    "Your Email Here": "Tu Email Aquí",
    "Join": "Unirse",
    "By subscribing, you agree to our Privacy Policy and consent to receive updates.": "Al suscribirte, aceptás nuestra Política de Privacidad y consentís recibir actualizaciones.",
    "Thank you! We have received your submission.": "¡Gracias! Recibimos tu solicitud.",
    "Oops! There was an error submitting the form.": "¡Ups! Hubo un error al enviar el formulario.",
    "Quick Links": "Links Rápidos",
    "Home Page": "Página Principal",
    "Follow Us": "Seguinos",
    "Facebook Page": "Página de Facebook",
    "Instagram Feed": "Feed de Instagram",
    "Twitter Profile": "Perfil de Twitter",
    "LinkedIn Page": "Página de LinkedIn",
    "YouTube Channel": "Canal de YouTube",
    "Legal Links": "Links Legales",
    "Privacy Policy": "Política de Privacidad",
    "Terms of Use": "Términos de Uso",
    "Cookie Settings": "Configuración de Cookies",
    "© 2025 RavencoreX. All rights reserved.": "© 2025 RavencoreX. Todos los derechos reservados.",

    # About page specific
    "Who We Are": "Quiénes Somos",
    "Data Engineers Who Ship": "Ingenieros de Datos que Entregan Resultados",
    "We're a team of data and cloud engineers specialized in Google Cloud, Looker, and modern BI infrastructure.": "Somos un equipo de ingenieros de datos y cloud especializados en Google Cloud, Looker e infraestructura BI moderna.",
    "Years of Experience": "Años de Experiencia",
    "In cloud data engineering": "En ingeniería de datos cloud",
    "Projects Delivered": "Proyectos Entregados",
    "Across industries": "En diferentes industrias",
    "Our Approach": "Nuestro Enfoque",
    "How We Work": "Cómo Trabajamos",

    # Contact page specific
    "Get In Touch": "Ponete en Contacto",
    "Ready to transform your data infrastructure? Let's talk.": "¿Listo para transformar tu infraestructura de datos? Hablemos.",
    "First Name": "Nombre",
    "Last Name": "Apellido",
    "Email": "Email",
    "Phone Number": "Número de Teléfono",
    "Message": "Mensaje",
    "Send Message": "Enviar Mensaje",
    "Enter your first name": "Ingresá tu nombre",
    "Enter your last name": "Ingresá tu apellido",
    "Enter your email": "Ingresá tu email",
    "Enter your phone": "Ingresá tu teléfono",
    "Enter your message": "Ingresá tu mensaje",

    # Common phrases
    "Read More": "Leer Más",
    "View All": "Ver Todo",
    "Back to Home": "Volver al Inicio",
    "Submit": "Enviar",
    "Cancel": "Cancelar",
    "Save": "Guardar",
    "Edit": "Editar",
    "Delete": "Eliminar",
    "Search": "Buscar",
    "Filter": "Filtrar",
    "Sort By": "Ordenar Por",
    "Show More": "Mostrar Más",
    "Show Less": "Mostrar Menos",

    # Cloud Solutions DevOps page specific
    "Cloud-First Analytics & DevOps for Data Platforms": "Analítica Cloud-First & DevOps para Plataformas de Datos",
    "We architect, build and operate your cloud data infrastructure with Google Cloud and modern DevOps practices — enabling fast, reliable insights at scale.": "Arquitectamos, construimos y operamos tu infraestructura de datos en la nube con Google Cloud y prácticas DevOps modernas — habilitando insights rápidos y confiables a escala.",
    "Explore Cloud Services": "Explorar Servicios Cloud",
    "Our Cloud & DevOps Offerings": "Nuestras Ofertas Cloud & DevOps",
    "Modern cloud infrastructure and DevOps automation for data-driven teams": "Infraestructura cloud moderna y automatización DevOps para equipos basados en datos",
    "Infrastructure Design & Automation": "Diseño de Infraestructura & Automatización",
    "Terraform-based IaC, auto-scaling, and cloud resource management optimized for analytics workloads.": "IaC basado en Terraform, auto-escalado y gestión de recursos cloud optimizada para cargas de trabajo analíticas.",
    "Data Platform Integration": "Integración de Plataformas de Datos",
    "Connect BigQuery, Looker, Cloud Functions and data pipelines into one cohesive analytics ecosystem.": "Conectamos BigQuery, Looker, Cloud Functions y pipelines de datos en un ecosistema analítico cohesivo.",
    "CI/CD Pipeline & Orchestration": "Pipeline CI/CD & Orquestación",
    "Automated deployments, dbt orchestration, and testing frameworks for reliable data delivery.": "Despliegues automatizados, orquestación dbt y frameworks de testing para entrega de datos confiable.",
    "Performance & Cost Optimisation": "Optimización de Rendimiento & Costos",
    "Query optimization, resource right-sizing, and cost monitoring to maximize ROI on cloud spend.": "Optimización de queries, dimensionamiento de recursos y monitoreo de costos para maximizar el ROI en gastos cloud.",
    "Why Our Cloud-First Approach Delivers": "Por Qué Nuestro Enfoque Cloud-First Entrega Resultados",
    "Proven results through modern infrastructure and DevOps best practices": "Resultados probados a través de infraestructura moderna y mejores prácticas DevOps",
    "Faster Deployments": "Despliegues Más Rápidos",
    "With automated CI/CD pipelines": "Con pipelines CI/CD automatizados",
    "Platform Uptime": "Tiempo de Actividad de Plataforma",
    "Across production environments": "En entornos de producción",
    "Cost Reduction": "Reducción de Costos",
    "Through infrastructure optimization": "A través de optimización de infraestructura",
    "Infrastructure as Code": "Infraestructura como Código",
    "Version-controlled, reproducible environments that eliminate configuration drift.": "Entornos versionados y reproducibles que eliminan la desviación de configuración.",
    "Auto-Scaling Analytics": "Analítica Auto-Escalable",
    "Handle peak loads seamlessly without manual intervention or over-provisioning.": "Manejá cargas pico sin problemas sin intervención manual o sobre-aprovisionamiento.",
    "Security & Compliance Built-In": "Seguridad & Cumplimiento Integrados",
    "Automated security scanning, access controls, and audit trails from day one.": "Escaneo de seguridad automatizado, controles de acceso y registros de auditoría desde el día uno.",
    "How We Work with You": "Cómo Trabajamos con Vos",
    "A structured, collaborative approach from planning to production": "Un enfoque estructurado y colaborativo desde la planificación hasta la producción",
    "Assessment & Architecture Design": "Evaluación & Diseño de Arquitectura",
    "We audit your current setup, understand your data workflows, and design a cloud architecture tailored to your analytics and business intelligence goals.": "Auditamos tu configuración actual, entendemos tus flujos de datos y diseñamos una arquitectura cloud adaptada a tus objetivos de analítica y business intelligence.",
    "Infrastructure Audit": "Auditoría de Infraestructura",
    "Requirements Gathering": "Recolección de Requerimientos",
    "Architecture Blueprint": "Plano de Arquitectura",
    "Build & Automate": "Construir & Automatizar",
    "We provision infrastructure, set up CI/CD pipelines, integrate data tools, and establish monitoring — all using Infrastructure as Code for full reproducibility.": "Aprovisionamos infraestructura, configuramos pipelines CI/CD, integramos herramientas de datos y establecemos monitoreo — todo usando Infraestructura como Código para reproducibilidad total.",
    "Terraform IaC": "Terraform IaC",
    "CI/CD Setup": "Configuración CI/CD",
    "Monitoring & Alerts": "Monitoreo & Alertas",
    "Deploy, Monitor & Optimise": "Desplegar, Monitorear & Optimizar",
    "After launch, we continuously monitor performance, fine-tune resources, and iterate based on real usage data — ensuring your platform stays fast and cost-efficient.": "Después del lanzamiento, monitoreamos continuamente el rendimiento, ajustamos recursos e iteramos basándonos en datos de uso real — asegurando que tu plataforma se mantenga rápida y eficiente en costos.",
    "Production Deployment": "Despliegue en Producción",
    "Performance Tuning": "Ajuste de Rendimiento",
    "Cost Optimization": "Optimización de Costos",
    "Ready to Modernise Your Data Infrastructure?": "¿Listo para Modernizar Tu Infraestructura de Datos?",
    "Let's design a cloud architecture that scales with your business and keeps your data teams productive.": "Diseñemos una arquitectura cloud que escale con tu negocio y mantenga a tus equipos de datos productivos.",
    "Start the Conversation": "Iniciar la Conversación",

    # Index page (Home) specific
    "Watch Demo": "Ver Demo",
    "We design and manage data platforms on Google Cloud — from ingestion to analytics. Built for performance, governance, and scale.": "Diseñamos y gestionamos plataformas de datos en Google Cloud — desde la ingesta hasta la analítica. Construidas para rendimiento, gobernanza y escala.",
    "From cloud architecture design to full pipeline deployment and optimization.": "Desde el diseño de arquitectura cloud hasta el despliegue completo de pipelines y optimización.",
    "Secure cloud storage and efficient data ingestion with cost optimization.": "Almacenamiento cloud seguro e ingesta de datos eficiente con optimización de costos.",
    "From performance optimization to LookML governance and dashboard design — we build analytics that scale with your business.": "Desde optimización de rendimiento hasta gobernanza LookML y diseño de dashboards — construimos analítica que escala con tu negocio.",
    "Google Cloud architecture from ingestion to warehouse — optimized for cost and performance.": "Arquitectura Google Cloud desde ingesta hasta warehouse — optimizada para costo y rendimiento.",
    "Custom dashboards, LookML development, and performance tuning for data teams at scale.": "Dashboards personalizados, desarrollo LookML y ajuste de rendimiento para equipos de datos a escala.",
    "Integrate Shopify, Tiendanube, and Meta Ads with BigQuery and Looker Studio for smarter decisions.": "Integramos Shopify, Tiendanube y Meta Ads con BigQuery y Looker Studio para decisiones más inteligentes.",
    "We design and manage data platforms on Google Cloud — from ingestion to analytics.": "Diseñamos y gestionamos plataformas de datos en Google Cloud — desde la ingesta hasta la analítica.",
    "Cloud architecture design, pipeline deployment, and infrastructure optimization.": "Diseño de arquitectura cloud, despliegue de pipelines y optimización de infraestructura.",
    "Efficient data ingestion, cloud storage, and cost-optimized infrastructure on Google Cloud.": "Ingesta de datos eficiente, almacenamiento cloud e infraestructura optimizada en costos en Google Cloud.",
    "Real-time BI dashboards, Looker implementations, and data-driven insights for business growth.": "Dashboards BI en tiempo real, implementaciones Looker e insights basados en datos para crecimiento empresarial.",
    "Start": "Comenzar",
    "E-commerce": "E-commerce",
    "We integrate Shopify, Tiendanube, and Meta Ads with BigQuery and Looker Studio to drive smarter sales decisions. From attribution modeling to funnel optimization — we turn your e-commerce data into actionable growth strategies.": "Integramos Shopify, Tiendanube y Meta Ads con BigQuery y Looker Studio para impulsar decisiones de ventas más inteligentes. Desde modelado de atribución hasta optimización de embudos — convertimos tus datos e-commerce en estrategias de crecimiento accionables.",
    "Build Your Data Foundation with RavencoreX": "Construí Tu Base de Datos con RavencoreX",
    "Let's design a BI ecosystem that grows with your business — from cloud infrastructure to executive dashboards.": "Diseñemos un ecosistema BI que crezca con tu negocio — desde infraestructura cloud hasta dashboards ejecutivos.",
    "Book a Call": "Reservar Llamada",

    # About Us page specific
    "We Turn Your Data into Strategic Advantage": "Convertimos Tus Datos en Ventaja Estratégica",
    "RavencoreX is a data and cloud engineering company built on Google Cloud & Looker expertise to scale analytics from raw data to business decisions.": "RavencoreX es una empresa de ingeniería de datos y cloud construida sobre experiencia en Google Cloud & Looker para escalar la analítica desde datos crudos hasta decisiones de negocio.",
    "Learn More About Us": "Conocer Más Sobre Nosotros",
    "Founded with over 20 years of experience in cloud, data analytics and business intelligence, RavencoreX helps organisations unlock value from their data by combining engineering discipline with strategic insight.": "Fundada con más de 20 años de experiencia en cloud, analítica de datos y business intelligence, RavencoreX ayuda a las organizaciones a desbloquear valor de sus datos combinando disciplina de ingeniería con visión estratégica.",
    "Trusted Partnership: Long-term relationships built on transparency and results.": "Asociación Confiable: Relaciones a largo plazo construidas sobre transparencia y resultados.",
    "Technical Excellence: Certified Google Cloud & Looker expertise with proven delivery.": "Excelencia Técnica: Experiencia certificada en Google Cloud & Looker con entrega probada.",
    "Data-Driven Growth: Every solution designed to scale your analytics and business impact.": "Crecimiento Basado en Datos: Cada solución diseñada para escalar tu analítica e impacto empresarial.",
    "We engineer your end-to-end analytics solution: ingestion, transformation, storage, modelling and visualization — all on Google Cloud and powered by Looker.": "Ingenierizamos tu solución analítica de extremo a extremo: ingesta, transformación, almacenamiento, modelado y visualización — todo en Google Cloud y potenciado por Looker.",
    "Sources": "Fuentes",
    "We connect to your business data — from APIs, databases, and files — to centralize everything into one reliable pipeline.": "Conectamos con tus datos de negocio — desde APIs, bases de datos y archivos — para centralizar todo en un pipeline confiable.",
    "Pipeline": "Pipeline",
    "Automated ETL and data validation flows built with Airbyte and Cloud Functions to keep your data fresh and consistent.": "Flujos ETL automatizados y validación de datos construidos con Airbyte y Cloud Functions para mantener tus datos frescos y consistentes.",
    "Warehouse": "Almacén",
    "We design BigQuery data models for performance and cost efficiency, ensuring a scalable foundation for analytics.": "Diseñamos modelos de datos BigQuery para rendimiento y eficiencia de costos, asegurando una base escalable para analítica.",
    "Dashboard": "Dashboard",
    "Actionable insights delivered through Looker and Looker Studio dashboards that empower smarter decisions.": "Insights accionables entregados a través de dashboards Looker y Looker Studio que potencian decisiones más inteligentes.",
    "Why We're Different": "Por Qué Somos Diferentes",
    "We're not a one-size-fits-all agency. We're a highly specialized team with over 20 years of data analytics experience and more than 5 years working with Google Cloud and Looker technologies — focused on delivering performance, scalability, and measurable results.": "No somos una agencia genérica. Somos un equipo altamente especializado con más de 20 años de experiencia en analítica de datos y más de 5 años trabajando con tecnologías Google Cloud y Looker — enfocados en entregar rendimiento, escalabilidad y resultados medibles.",
    "Deep Google Cloud & Looker Expertise": "Experiencia Profunda en Google Cloud & Looker",
    "Our team has extensive experience designing, optimizing, and maintaining enterprise-scale analytics ecosystems using Google Cloud and Looker. We focus on building solutions that are both powerful and efficient.": "Nuestro equipo tiene amplia experiencia diseñando, optimizando y manteniendo ecosistemas analíticos a escala empresarial usando Google Cloud y Looker. Nos enfocamos en construir soluciones potentes y eficientes.",
    "Automated Pipelines for Faster Time-to-Insight": "Pipelines Automatizados para Insights Más Rápidos",
    "We build self-service data platforms with automated ETL, dbt modeling, and orchestration — ensuring your team gets accurate insights faster, with less manual work.": "Construimos plataformas de datos self-service con ETL automatizado, modelado dbt y orquestación — asegurando que tu equipo obtenga insights precisos más rápido, con menos trabajo manual.",
    "Tailored for E-Commerce, SaaS & AdTech": "Adaptado para E-Commerce, SaaS & AdTech",
    "We understand the key metrics that drive performance — CAC, LTV, ROAS, conversion funnels, attribution models — and build custom dashboards to help you grow smarter.": "Entendemos las métricas clave que impulsan el rendimiento — CAC, LTV, ROAS, embudos de conversión, modelos de atribución — y construimos dashboards personalizados para ayudarte a crecer más inteligentemente.",
    "Proven Cost & Performance Optimization": "Optimización de Costos & Rendimiento Probada",
    "We've helped clients reduce BigQuery costs by up to 40%, cut dashboard load times by 3×, and eliminate repetitive reporting through intelligent data modeling and automation.": "Hemos ayudado a clientes a reducir costos de BigQuery hasta un 40%, reducir tiempos de carga de dashboards 3×, y eliminar reportes repetitivos a través de modelado de datos inteligente y automatización.",
    "Our Impact": "Nuestro Impacto",
    "Real results from enterprise-grade analytics engagements.": "Resultados reales de proyectos analíticos de nivel empresarial.",
    "-80% Report Prep Time": "-80% Tiempo de Preparación de Reportes",
    "Automated dashboards eliminate manual reporting": "Dashboards automatizados eliminan reportes manuales",
    "3× Faster Dashboard Load": "3× Carga de Dashboard Más Rápida",
    "Optimized queries and caching strategies": "Queries optimizados y estrategias de caché",
    "-40% BigQuery Cost": "-40% Costo BigQuery",
    "Smart partitioning and query optimization": "Particionado inteligente y optimización de queries",
    "+100% Data Adoption": "+100% Adopción de Datos",
    "Self-service BI drives org-wide engagement": "BI self-service impulsa compromiso en toda la organización",
    "These are typical outcomes we achieve with enterprise-grade analytics engagements.": "Estos son resultados típicos que logramos con proyectos analíticos de nivel empresarial.",
    "Methodology": "Metodología",
    "Our Approach to Client Partnerships": "Nuestro Enfoque para Asociaciones con Clientes",
    "At RavencoreX, we prioritize collaboration and transparency. Our tailored methodologies ensure that we meet your unique business needs.": "En RavencoreX, priorizamos la colaboración y transparencia. Nuestras metodologías personalizadas aseguran que cumplamos con tus necesidades empresariales únicas.",
    "Discovery Phase": "Fase de Descubrimiento",
    "We begin with a thorough analysis of your business goals and challenges.": "Comenzamos con un análisis exhaustivo de tus objetivos empresariales y desafíos.",
    "Implementation Phase": "Fase de Implementación",
    "Our team executes solutions quickly, ensuring agility and adaptability throughout the process.": "Nuestro equipo ejecuta soluciones rápidamente, asegurando agilidad y adaptabilidad durante todo el proceso.",
    "Ready to Transform Your Data?": "¿Listo para Transformar Tus Datos?",
    "Schedule a 30-minute discovery call to map your analytics roadmap. We'll discuss your data challenges, explore solutions, and outline how we can accelerate your path from raw data to business decisions.": "Agendá una llamada de descubrimiento de 30 minutos para mapear tu hoja de ruta analítica. Discutiremos tus desafíos de datos, exploraremos soluciones y delinearemos cómo podemos acelerar tu camino desde datos crudos hasta decisiones de negocio.",
    "Book Your Strategy Call": "Reservar Tu Llamada Estratégica",

    # Business Intelligence page specific
    "From Data Chaos to Clarity — Business Intelligence Done Right": "Del Caos de Datos a la Claridad — Business Intelligence Bien Hecho",
    "We design, build and optimize BI ecosystems using Google Cloud, Looker and BigQuery — empowering teams with trusted, real-time insights.": "Diseñamos, construimos y optimizamos ecosistemas BI usando Google Cloud, Looker y BigQuery — empoderando equipos con insights confiables en tiempo real.",
    "Explore BI Services": "Explorar Servicios BI",
    "What We Do in BI": "Lo Que Hacemos en BI",
    "Comprehensive Business Intelligence services powered by Google Cloud & Looker": "Servicios integrales de Business Intelligence potenciados por Google Cloud & Looker",
    "Data Modeling & Governance": "Modelado de Datos & Gobernanza",
    "Design robust LookML & dbt models with scalable data governance.": "Diseñamos modelos LookML & dbt robustos con gobernanza de datos escalable.",
    "Dashboard Design & Optimization": "Diseño de Dashboards & Optimización",
    "Build fast, intuitive dashboards that drive business decisions.": "Construimos dashboards rápidos e intuitivos que impulsan decisiones de negocio.",
    "Performance & Cost Monitoring": "Monitoreo de Rendimiento & Costos",
    "Improve dashboard load times × 3 and reduce BigQuery costs by up to 40%.": "Mejoramos tiempos de carga de dashboards × 3 y reducimos costos de BigQuery hasta un 40%.",
    "Migration & Integration": "Migración & Integración",
    "Migrate from Power BI or Tableau to Looker and integrate with existing systems.": "Migramos desde Power BI o Tableau a Looker e integramos con sistemas existentes.",
    "Data in Motion": "Datos en Movimiento",
    "See how our dashboards turn raw data into decisions.": "Mirá cómo nuestros dashboards convierten datos crudos en decisiones.",
    "A proven methodology for BI transformation": "Una metodología probada para transformación BI",
    "Discovery & Audit": "Descubrimiento & Auditoría",
    "Review your current BI environment and pain points. We analyze existing dashboards, data models and queries to identify optimization opportunities.": "Revisamos tu entorno BI actual y puntos de dolor. Analizamos dashboards existentes, modelos de datos y queries para identificar oportunidades de optimización.",
    "Optimization & Automation": "Optimización & Automatización",
    "Redesign models and dashboards for speed and scalability. We refactor LookML/dbt models, automate refreshes, and enhance UX.": "Rediseñamos modelos y dashboards para velocidad y escalabilidad. Refactorizamos modelos LookML/dbt, automatizamos actualizaciones y mejoramos UX.",
    "Delivery & Enablement": "Entrega & Habilitación",
    "Launch optimized dashboards and train your teams. We deploy the improved BI environment and ensure your team can maintain and extend it.": "Lanzamos dashboards optimizados y capacitamos a tus equipos. Desplegamos el entorno BI mejorado y aseguramos que tu equipo pueda mantenerlo y extenderlo.",
    "Visualise Your Insights": "Visualizá Tus Insights",
    "From pipelines to dashboards — every step visible.": "Desde pipelines hasta dashboards — cada paso visible.",
    "Why Choose RavencoreX for Your BI Projects?": "¿Por Qué Elegir RavencoreX para Tus Proyectos BI?",
    "-80% Report Preparation Time": "-80% Tiempo de Preparación de Reportes",
    "Automated data pipelines": "Pipelines de datos automatizados",
    "3× Faster Dashboard Performance": "3× Rendimiento de Dashboard Más Rápido",
    "Optimized queries & caching": "Queries optimizados & caché",
    "+100% Data Adoption Rate": "+100% Tasa de Adopción de Datos",
    "Intuitive, self-service BI": "BI intuitivo, self-service",
    "Our clients achieve measurable improvements in speed, efficiency and adoption through modern BI architecture on Google Cloud and Looker.": "Nuestros clientes logran mejoras medibles en velocidad, eficiencia y adopción a través de arquitectura BI moderna en Google Cloud y Looker.",
    "Frequently Asked Questions": "Preguntas Frecuentes",
    "Everything you need to know before starting your BI project.": "Todo lo que necesitás saber antes de iniciar tu proyecto BI.",
    "How long does it take to build a BI dashboard?": "¿Cuánto tiempo lleva construir un dashboard BI?",
    "Most projects are completed within 2–4 weeks, depending on the number of data sources, the complexity of the models, and the number of dashboards required. We work in agile sprints to deliver MVPs quickly and iterate based on feedback.": "La mayoría de los proyectos se completan en 2–4 semanas, dependiendo del número de fuentes de datos, la complejidad de los modelos y el número de dashboards requeridos. Trabajamos en sprints ágiles para entregar MVPs rápidamente e iterar basados en feedback.",
    "Can you integrate our existing data sources?": "¿Pueden integrar nuestras fuentes de datos existentes?",
    "Yes — we work with APIs, databases (PostgreSQL, MySQL, MongoDB), warehouses (BigQuery, Snowflake, Redshift), spreadsheets, CRMs (Salesforce, HubSpot), and ecommerce platforms (Shopify, WooCommerce). We build ETL pipelines to centralize all your data.": "Sí — trabajamos con APIs, bases de datos (PostgreSQL, MySQL, MongoDB), warehouses (BigQuery, Snowflake, Redshift), hojas de cálculo, CRMs (Salesforce, HubSpot) y plataformas ecommerce (Shopify, WooCommerce). Construimos pipelines ETL para centralizar todos tus datos.",
    "Do we need Google Cloud to use your BI solutions?": "¿Necesitamos Google Cloud para usar sus soluciones BI?",
    "Not necessarily. While we recommend Google Cloud and Looker for scalability and cost-efficiency, we can also work with other cloud providers (AWS, Azure) and BI tools (Tableau, Power BI, Metabase). Our expertise is cloud-agnostic, though we specialize in the Google ecosystem.": "No necesariamente. Aunque recomendamos Google Cloud y Looker por escalabilidad y eficiencia de costos, también podemos trabajar con otros proveedores cloud (AWS, Azure) y herramientas BI (Tableau, Power BI, Metabase). Nuestra experiencia es cloud-agnóstica, aunque nos especializamos en el ecosistema Google.",
    "Can you migrate our Power BI or Tableau dashboards?": "¿Pueden migrar nuestros dashboards Power BI o Tableau?",
    "Absolutely. We specialize in migrating legacy BI systems to modern cloud-based platforms. We'll audit your current dashboards, replicate the logic in Looker or your preferred tool, and improve performance along the way. Migration typically takes 3–6 weeks depending on complexity.": "Absolutamente. Nos especializamos en migrar sistemas BI legacy a plataformas cloud modernas. Auditaremos tus dashboards actuales, replicaremos la lógica en Looker o tu herramienta preferida y mejoraremos el rendimiento en el proceso. La migración típicamente lleva 3–6 semanas dependiendo de la complejidad.",
    "What happens after delivery?": "¿Qué pasa después de la entrega?",
    "We provide documentation, handoff training, and ongoing support options. You'll own all the code (LookML, dbt, SQL) and have full control. We also offer monthly retainers for continuous optimization, new dashboard creation, and technical support as your needs evolve.": "Proveemos documentación, capacitación de transferencia y opciones de soporte continuo. Serás dueño de todo el código (LookML, dbt, SQL) y tendrás control completo. También ofrecemos retainers mensuales para optimización continua, creación de nuevos dashboards y soporte técnico a medida que tus necesidades evolucionan.",
    "Ready to Optimize Your BI Environment?": "¿Listo para Optimizar Tu Entorno BI?",
    "Book a 30-minute strategy session to map your analytics roadmap.": "Reservá una sesión estratégica de 30 minutos para mapear tu hoja de ruta analítica.",

    # E-commerce page specific
    "E-Commerce Analytics & Automation": "Análisis E-Commerce & Automatización",
    "We connect Shopify, GA4, and Meta Ads in BigQuery — giving you dashboards that drive sales, not reports.": "Conectamos Shopify, GA4 y Meta Ads en BigQuery — dándote dashboards que impulsan ventas, no reportes.",
    "See Live Dashboard": "Ver Dashboard en Vivo",
    "Request Audit": "Solicitar Auditoría",
    "Why It Matters": "Por Qué Importa",
    "Faster Decisions": "Decisiones Más Rápidas",
    "Unified data across Shopify, Ads & Analytics delivers real-time insights when you need them most.": "Datos unificados entre Shopify, Ads & Analytics entrega insights en tiempo real cuando más los necesitás.",
    "Cost Control": "Control de Costos",
    "Track ROAS, CAC, and product margins in real time to maximize profitability across every campaign.": "Rastreá ROAS, CAC y márgenes de producto en tiempo real para maximizar rentabilidad en cada campaña.",
    "Growth Visibility": "Visibilidad de Crecimiento",
    "Know your winners and double down faster with crystal-clear performance metrics.": "Conocé tus ganadores y duplicá más rápido con métricas de rendimiento cristalinas.",
    "All your performance data in one dashboard.": "Todos tus datos de rendimiento en un dashboard.",
    "• From campaigns to conversions—centralize every metric": "• Desde campañas hasta conversiones—centralizá cada métrica",
    "• Live syncs, automated reporting, zero manual work": "• Sincronizaciones en vivo, reportes automatizados, cero trabajo manual",
    "Explore Demo": "Explorar Demo",
    "How We Build Your Data Engine": "Cómo Construimos Tu Motor de Datos",
    "Connect & Ingest": "Conectar & Ingerir",
    "GA4, Meta Ads, Shopify via APIs & Airbyte—automated pipelines bring all your data to BigQuery.": "GA4, Meta Ads, Shopify vía APIs & Airbyte—pipelines automatizados traen todos tus datos a BigQuery.",
    "Model & Automate": "Modelar & Automatizar",
    "dbt + BigQuery with scheduled syncs transform raw data into clean, analysis-ready tables.": "dbt + BigQuery con sincronizaciones programadas transforman datos crudos en tablas limpias y listas para análisis.",
    "Visualize & Grow": "Visualizar & Crecer",
    "Looker Studio / Looker dashboards put insights at your fingertips—track, optimize, scale.": "Dashboards Looker Studio / Looker ponen insights al alcance de tu mano—rastreá, optimizá, escalá.",
    "Real Results": "Resultados Reales",
    "See how data empowers next-level e-commerce growth.": "Mirá cómo los datos potencian el crecimiento e-commerce de siguiente nivel.",
    "30% ROAS Improvement": "30% Mejora en ROAS",
    "Average increase": "Aumento promedio",
    "40% Time Saved": "40% Tiempo Ahorrado",
    "On manual reports": "En reportes manuales",
    "100% Data Unification": "100% Unificación de Datos",
    "Marketing & sales aligned": "Marketing & ventas alineados",
    "Everything you need to know before starting your e-commerce analytics project.": "Todo lo que necesitás saber antes de iniciar tu proyecto de analítica e-commerce.",
    "How long does it take to build a first dashboard?": "¿Cuánto tiempo lleva construir un primer dashboard?",
    "A basic dashboard typically takes 2-3 weeks from data connection to deployment. Complex setups with multiple sources may take 4-6 weeks.": "Un dashboard básico típicamente lleva 2-3 semanas desde conexión de datos hasta despliegue. Configuraciones complejas con múltiples fuentes pueden llevar 4-6 semanas.",
    "Can you integrate our existing data sources (Shopify/GA4/Meta/ERP)?": "¿Pueden integrar nuestras fuentes de datos existentes (Shopify/GA4/Meta/ERP)?",
    "Yes, we connect to all major e-commerce platforms (Shopify, WooCommerce, Magento), analytics tools (GA4, Adobe Analytics), advertising platforms (Meta, Google Ads), and ERPs via APIs or Airbyte connectors.": "Sí, conectamos con todas las principales plataformas e-commerce (Shopify, WooCommerce, Magento), herramientas de analítica (GA4, Adobe Analytics), plataformas de publicidad (Meta, Google Ads) y ERPs vía APIs o conectores Airbyte.",
    "We primarily use Google Cloud (BigQuery + Looker), but can adapt to AWS, Azure, or Snowflake based on your existing infrastructure.": "Usamos principalmente Google Cloud (BigQuery + Looker), pero podemos adaptarnos a AWS, Azure o Snowflake basándonos en tu infraestructura existente.",
    "Can you migrate from Power BI / Tableau to Looker?": "¿Pueden migrar desde Power BI / Tableau a Looker?",
    "Absolutely. We offer migration services including dashboard recreation, data model optimization, and team training on the new platform.": "Absolutamente. Ofrecemos servicios de migración incluyendo recreación de dashboards, optimización de modelos de datos y capacitación del equipo en la nueva plataforma.",
    "What happens after delivery (handoff, training, retainers)?": "¿Qué pasa después de la entrega (transferencia, capacitación, retainers)?",
    "We provide full documentation, training sessions, and optional retainer support for ongoing maintenance, new dashboard creation, and data model updates.": "Proveemos documentación completa, sesiones de capacitación y soporte retainer opcional para mantenimiento continuo, creación de nuevos dashboards y actualizaciones de modelos de datos.",
    "Turn Your E-Commerce Data into Growth.": "Convertí Tus Datos E-Commerce en Crecimiento.",
    "Start making data-driven decisions today.": "Comenzá a tomar decisiones basadas en datos hoy.",

    # Additional common footer/navigation items
    "About Us": "Nosotros",
    "Contact Us": "Contactanos",

    # Additional About Us page items that were missed
    "Trusted Partnership:": "Asociación Confiable:",
    "Long-term relationships built on transparency and results.": "Relaciones a largo plazo construidas sobre transparencia y resultados.",
    "Technical Excellence:": "Excelencia Técnica:",
    "Certified Google Cloud & Looker expertise with proven delivery.": "Experiencia certificada en Google Cloud & Looker con entrega probada.",
    "Data-Driven Growth:": "Crecimiento Basado en Datos:",
    "Every solution designed to scale your analytics and business impact.": "Cada solución diseñada para escalar tu analítica e impacto empresarial.",

    # Web Design page specific
    "Modern Websites that Convert": "Sitios Web Modernos que Convierten",
    "We design and build high-performance websites with clean UX, speed, and SEO best practices.": "Diseñamos y construimos sitios web de alto rendimiento con UX limpia, velocidad y mejores prácticas SEO.",
    "See Portfolio": "Ver Portfolio",
    "Faster Load Times": "Tiempos de Carga Más Rápidos",
    "Lighthouse-friendly performance and Core Web Vitals optimization for instant page loads.": "Rendimiento optimizado para Lighthouse y Core Web Vitals para cargas de página instantáneas.",
    "Clear UX, Higher Conversions": "UX Clara, Mayores Conversiones",
    "Guided flows, crisp messaging, and frictionless forms that turn visitors into customers.": "Flujos guiados, mensajes claros y formularios sin fricción que convierten visitantes en clientes.",
    "SEO-Ready": "Listo para SEO",
    "Semantic HTML, structured data, and clean information architecture for better rankings.": "HTML semántico, datos estructurados y arquitectura de información limpia para mejores rankings.",
    "Design that Tells Your Story": "Diseño que Cuenta Tu Historia",
    "• Modular sections and consistent typography scale as you grow": "• Secciones modulares y tipografía consistente que escalan mientras crecés",
    "• Brand-aligned visuals with motion used sparingly for clarity": "• Visuales alineados a tu marca con movimiento usado moderadamente para claridad",
    "View Components": "Ver Componentes",
    "Performance": "Rendimiento",
    "Built for Speed & Maintainability": "Construido para Velocidad & Mantenibilidad",
    "• Best-practice HTML/CSS, image optimization, and caching": "• HTML/CSS de mejores prácticas, optimización de imágenes y caché",
    "• Accessible, lightweight animations; 'prefers-reduced-motion' compliant": "• Animaciones accesibles y livianas; compatibles con 'prefers-reduced-motion'",
    "See Performance Guidelines": "Ver Guías de Rendimiento",
    "Our Web Design Process": "Nuestro Proceso de Diseño Web",
    "Discovery & UX": "Descubrimiento & UX",
    "Goals, users, site map, and wireframes—laying the foundation for intuitive navigation.": "Objetivos, usuarios, mapa del sitio y wireframes—estableciendo la base para navegación intuitiva.",
    "Visual Design & Build": "Diseño Visual & Construcción",
    "Design system, components, responsive pages—bringing your brand to life with clean code.": "Sistema de diseño, componentes, páginas responsive—dando vida a tu marca con código limpio.",
    "Launch & Handoff": "Lanzamiento & Transferencia",
    "QA, analytics, SEO basics, documentation and training—empowering your team to succeed.": "QA, analítica, fundamentos SEO, documentación y capacitación—empoderando a tu equipo para tener éxito.",
    "Portfolio Showcase": "Muestra de Portfolio",
    "Real projects, real results—explore our recent work.": "Proyectos reales, resultados reales—explorá nuestro trabajo reciente.",
    "Analytics Portal": "Portal de Analítica",
    "Real-time dashboards & data visualization": "Dashboards en tiempo real & visualización de datos",
    "SaaS Landing": "Landing SaaS",
    "Conversion-focused design & copy": "Diseño & copy enfocado en conversión",
    "E-commerce Home": "Inicio E-commerce",
    "Product showcase & checkout flow": "Muestra de productos & flujo de checkout",
    "Typical results after a redesign with performance and UX improvements.": "Resultados típicos después de un rediseño con mejoras de rendimiento y UX.",
    "% Conversion Lift": "% Aumento en Conversión",
    "LCP on Key Pages": "LCP en Páginas Clave",
    "Lightning-fast loading": "Carga ultra-rápida",
    "Lighthouse Accessibility": "Accesibilidad Lighthouse",
    "Inclusive design": "Diseño inclusivo",
    "Everything you need to know before starting your website project.": "Todo lo que necesitás saber antes de iniciar tu proyecto de sitio web.",
    "How long does a typical website project take?": "¿Cuánto tiempo lleva un proyecto web típico?",
    "A standard website project takes 4–8 weeks from discovery to launch, depending on scope. Landing pages can be completed in 2–3 weeks, while full e-commerce sites may take 10–12 weeks.": "Un proyecto web estándar lleva 4–8 semanas desde el descubrimiento hasta el lanzamiento, dependiendo del alcance. Landing pages pueden completarse en 2–3 semanas, mientras que sitios e-commerce completos pueden llevar 10–12 semanas.",
    "Can you migrate our existing content and SEO?": "¿Pueden migrar nuestro contenido y SEO existente?",
    "Yes—we handle content migration, URL redirects, and preserve your SEO rankings. We'll audit your current site, set up 301 redirects, and ensure Google Search Console is properly configured.": "Sí—manejamos la migración de contenido, redirecciones de URL y preservamos tus rankings SEO. Auditaremos tu sitio actual, configuraremos redirecciones 301 y aseguraremos que Google Search Console esté correctamente configurado.",
    "Do you provide copy and brand assets?": "¿Proveen copy y assets de marca?",
    "We can work with your existing brand guidelines and copy, or provide strategic copywriting and design support. We partner with experienced copywriters and brand designers when needed.": "Podemos trabajar con tus guías de marca y copy existentes, o proveer soporte estratégico de copywriting y diseño. Nos asociamos con copywriters y diseñadores de marca experimentados cuando es necesario.",
    "How do you measure performance and conversions?": "¿Cómo miden el rendimiento y las conversiones?",
    "We set up Google Analytics 4, track Core Web Vitals with Lighthouse, and configure conversion goals (form submissions, purchases, etc.). You'll receive monthly performance reports.": "Configuramos Google Analytics 4, rastreamos Core Web Vitals con Lighthouse y configuramos objetivos de conversión (envíos de formularios, compras, etc.). Recibirás reportes mensuales de rendimiento.",
    "What happens after launch (support, iterations)?": "¿Qué pasa después del lanzamiento (soporte, iteraciones)?",
    "We provide 30 days of post-launch support for bug fixes and minor tweaks. After that, we offer monthly retainers for ongoing updates, A/B testing, and continuous optimization.": "Proveemos 30 días de soporte post-lanzamiento para correcciones de bugs y ajustes menores. Después de eso, ofrecemos retainers mensuales para actualizaciones continuas, testing A/B y optimización continua.",
    "Ready to Design a Website that Converts?": "¿Listo para Diseñar un Sitio Web que Convierte?",
    "Book a 30-minute strategy call to scope your redesign.": "Reservá una llamada estratégica de 30 minutos para definir el alcance de tu rediseño.",

    # Contact page specific
    "Get in Touch": "Ponete en Contacto",
    "Have a project in mind or looking to explore how technology can drive your business forward? We're here to help. Reach out to RavencoreX and let's build something extraordinary together.": "¿Tenés un proyecto en mente o buscás explorar cómo la tecnología puede impulsar tu negocio? Estamos acá para ayudar. Contactá a RavencoreX y construyamos algo extraordinario juntos.",
    "Contact": "Contacto",
    "We'd love to hear from you! Reach out today.": "¡Nos encantaría saber de vos! Contactanos hoy.",
    "Your company name": "Nombre de tu empresa",
    "How we can help?...Select an option": "¿Cómo podemos ayudar?...Seleccioná una opción",
    "Looker Support & Data Analytics": "Soporte Looker & Analítica de Datos",
    "Google Cloud Solutions": "Soluciones Google Cloud",
    "Ecommerce Solutions": "Soluciones E-commerce",
    "Web Design": "Diseño Web",
    "Other": "Otro",
    "Additional details here...": "Detalles adicionales acá...",
    "I agree to receive other communications from RavencoreX.": "Acepto recibir otras comunicaciones de RavencoreX.",
    "I agree to allow RavencoreX Group to store and process my personal data.": "Acepto permitir que RavencoreX Group almacene y procese mis datos personales.",
    "Send": "Enviar",
    "Thank you! We'll get back to you soon.": "¡Gracias! Te contactaremos pronto.",
    "Oops! Please try submitting again later.": "¡Ups! Por favor intentá enviar nuevamente más tarde.",
    "Please complete the reCAPTCHA verification.": "Por favor completá la verificación reCAPTCHA.",
    "Sending...": "Enviando...",
}

def translate_text_content(html_content):
    """
    Translate all visible text in HTML content
    Uses regex patterns to find and replace text between tags
    """
    content = html_content

    # Sort translations by length (longest first) to avoid partial replacements
    sorted_translations = sorted(TRANSLATIONS.items(), key=lambda x: len(x[0]), reverse=True)

    for english, spanish in sorted_translations:
        # Escape special regex characters
        english_escaped = re.escape(english)

        # Replace text between HTML tags
        # Pattern: >English text<
        content = re.sub(
            rf'>{english_escaped}<',
            f'>{spanish}<',
            content
        )

        # Replace text in title attributes
        content = re.sub(
            rf'title="{english_escaped}"',
            f'title="{spanish}"',
            content
        )

        # Replace text in aria-label attributes
        content = re.sub(
            rf'aria-label="{english_escaped}"',
            f'aria-label="{spanish}"',
            content
        )

        # Replace text in placeholder attributes
        content = re.sub(
            rf'placeholder="{english_escaped}"',
            f'placeholder="{spanish}"',
            content
        )

        # Replace text in value attributes for buttons
        content = re.sub(
            rf'value="{english_escaped}"',
            f'value="{spanish}"',
            content
        )

    return content

def translate_page(page_name):
    """Translate a single Spanish page"""
    print(f"\n📄 Translating {page_name}...")

    file_path = AR_DIR / page_name

    # Read the page
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Translate content
    original_content = content
    content = translate_text_content(content)

    # Count replacements
    changes = sum(1 for en in TRANSLATIONS.keys() if en in original_content)

    # Write back
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"  ✅ Translated {changes} phrases in {page_name}")

def main():
    """Translate all Spanish pages"""
    pages = [
        "index.html",
        "about-us.html",
        "cloud-solutions-devops.html",
        "data-analytics-business-intelligence.html",
        "ecommerce-development-optimization.html",
        "web-design.html",
        "contact-page.html"
    ]

    print("🌐 Starting content translation...")
    print("=" * 60)

    for page in pages:
        try:
            translate_page(page)
        except Exception as e:
            print(f"  ❌ Error translating {page}: {e}")

    print("\n" + "=" * 60)
    print("\n✅ Translation complete!")
    print(f"\n📁 Location: {AR_DIR}")
    print(f"📊 Pages translated: {len(pages)}")

if __name__ == "__main__":
    main()
