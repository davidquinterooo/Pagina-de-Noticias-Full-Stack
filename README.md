<<<<<<< HEAD
# Nuxt Minimal Starter

Look at the [Nuxt documentation](https://nuxt.com/docs/getting-started/introduction) to learn more.

## Setup

Make sure to install dependencies:

```bash
# npm
npm install

# pnpm
pnpm install

# yarn
yarn install

# bun
bun install
```

## Development Server

Start the development server on `http://localhost:3000`:

```bash
# npm
npm run dev

# pnpm
pnpm dev

# yarn
yarn dev

# bun
bun run dev
```

## Production

Build the application for production:

```bash
# npm
npm run build

# pnpm
pnpm build

# yarn
yarn build

# bun
bun run build
```

Locally preview production build:

```bash
# npm
npm run preview

# pnpm
pnpm preview

# yarn
yarn preview

# bun
bun run preview
```

Check out the [deployment documentation](https://nuxt.com/docs/getting-started/deployment) for more information.
=======
# Mi Periódico — Página de Noticias Full Stack

Aplicación web de noticias con panel de administración propio. Proyecto full stack desarrollado con asistencia de herramientas de vibecoding (OpenCode / Antigravity).

## Stack tecnológico

| Capa | Tecnología |
|---|---|
| Backend | Django + Django REST Framework |
| Frontend | Nuxt 3 (Vue) + Bootstrap |
| Base de datos (desarrollo) | PostgreSQL vía Docker |
| Base de datos (producción) | PostgreSQL administrado por Supabase |
| Autenticación | JWT (`djangorestframework-simplejwt`) |
| Editor de contenido | TipTap (guarda el cuerpo de la noticia como HTML) |
| Estado global (frontend) | Pinia |

## Alcance del MVP

**Incluido en v1:**
- Feed público de noticias (home) con paginación, sin categorías
- Página de detalle de cada noticia
- Buscador simple por título/contenido
- Panel de administración privado para crear, editar, eliminar y publicar/despublicar noticias
- Login de un único usuario admin

**Fuera del MVP (backlog):**
- Categorías y etiquetas
- Comentarios de lectores
- Cuentas de lectores / newsletter
- Múltiples redactores y roles

## Estructura del repositorio

```
mi-periodico/
├── backend/          # Proyecto Django (API REST)
│   ├── config/        # Configuración del proyecto (settings, urls)
│   ├── noticias/       # App principal: modelo Noticia, admin, API
│   └── media/          # Imágenes subidas (solo en local, ignorado en git)
├── frontend/         # Proyecto Nuxt 3
├── docker-compose.yml  # Postgres local para desarrollo
├── AGENTS.md          # Contexto del proyecto para herramientas de IA/vibecoding
└── README.md
```

## Modelo de datos

Un único modelo `Noticia` (app `noticias`):

| Campo | Tipo | Descripción |
|---|---|---|
| `titulo` | CharField | Título de la noticia |
| `slug` | SlugField | URL amigable, autogenerado del título |
| `resumen` | CharField | Texto corto para el feed y SEO |
| `contenido` | TextField | Cuerpo de la noticia en **HTML** (generado por TipTap) |
| `imagen_portada` | ImageField | Imagen principal |
| `imagen_portada_alt` | CharField | Texto alternativo de la imagen |
| `estado` | CharField (choices) | `borrador` o `publicado` |
| `fecha_publicacion` | DateTimeField | Se completa automáticamente al publicar |
| `fecha_creacion` | DateTimeField | Automático |
| `fecha_actualizacion` | DateTimeField | Automático |

No hay modelo de usuario personalizado: se usa el sistema de autenticación por defecto de Django, con un único superusuario administrador.

## Requisitos previos

- Python 3.11+
- Node.js LTS
- Docker Desktop
- Git

## Puesta en marcha en local

### 1. Base de datos

```bash
docker compose up -d
```

### 2. Backend

```bash
cd backend
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt

cp .env.example .env            # y completa las variables

python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Backend disponible en `http://localhost:8000`. Panel de administración en `http://localhost:8000/admin/`.

### 3. Frontend

```bash
cd frontend
npm install

cp .env.example .env            # y completa las variables

npm run dev
```

Frontend disponible en `http://localhost:3000`.

## Variables de entorno

### `backend/.env`

```env
DEBUG=True
SECRET_KEY=
DATABASE_URL=postgresql://noticias_user:noticias_pass@localhost:5432/noticias_db
```

### `frontend/.env`

```env
NUXT_PUBLIC_API_BASE=http://localhost:8000/api
```

> Ningún archivo `.env` se sube al repositorio (ver `.gitignore`). Se incluyen archivos `.env.example` como plantilla, sin valores reales.

## Roadmap

- [x] Definición del MVP
- [x] Modelo de datos `Noticia`
- [x] Configuración del entorno de desarrollo
- [x] Modelo en Django + Django Admin
- [ ] Serializers y API REST (Django REST Framework)
- [ ] Frontend: feed, detalle de noticia, buscador
- [ ] Panel de administración en el frontend
- [ ] Migración a Supabase (producción)
- [ ] Despliegue (backend + frontend)

## Licencia

Proyecto personal — sin licencia definida aún.
>>>>>>> 2f39e594c9da97592f07f69a0006861c0bfdd7bc
