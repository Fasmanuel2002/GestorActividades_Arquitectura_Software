# GestorActividades_Arquitectura_Software

Aplicación web desarrollada con Django para la asignatura de Arquitectura de Software. El sistema permite gestionar actividades, usuarios y monitores, incluyendo filtros mediante parámetros GET.

---

# Requisitos

- Python 3.10+
- pip
- virtualenv (recomendado)
- Django (incluido en requirements.txt)

---

# Instalación

## 1. Clonar el repositorio

```bash
git clone https://github.com/tuusuario/GestorActividades_Arquitectura_Software.git
cd GestorActividades_Arquitectura_Software
```

## 2. Crear entorno virtual
```bash
python -m venv venv
venv\Scripts\activate
```

## 3. Instalar dependencias
```bash
pip install -r requirements.txt
```

## 4. Migraciones de base de datos
```bash
python manage.py makemigrations
python manage.py migrate
```

## 5. Ejecutar servidor
```bash
python manage.py runserver
```

# Endpoints del proyecto

---

## Inicio

- `GET /gestion/` → Página de inicio
---

## Actividades

- `GET /gestion/actividades/` → Listar actividades (con filtros GET)
- `GET /gestion/actividades/?tipo=danza` → Filtrar por tipo
- `GET /gestion/actividades/?monitor=3` → Filtrar por monitor
- `GET /gestion/actividades/<int:actividad_id>/` → Obtener actividad por ID
- `POST /gestion/actividades/registrar/` → Crear actividad (JSON)
- `POST /gestion/crear_actividad_formulario/` → Crear actividad (formulario HTML)
- `PUT /gestion/actividades/<int:actividad_id>/editar/` → Actualizar actividad
- `DELETE /gestion/actividades/<int:actividad_id>/eliminar/` → Eliminar actividad

---

## Usuarios

- `GET /gestion/usuarios/` → Listar usuarios
- `GET /gestion/usuarios/?actividad=5` → Filtrar usuarios por actividad
- `GET /gestion/usuarios/<int:usuario_id>/` → Obtener usuario por ID
- `POST /gestion/usuarios/registrar/` → Crear usuario (JSON)
- `POST /gestion/usuarios_inscritos/nuevo/` → Crear usuario (formulario HTML)
- `PUT /gestion/usuarios/<int:usuario_id>/editar/` → Actualizar usuario
- `DELETE /gestion/usuarios/<int:usuario_id>/eliminar/` → Eliminar usuario

---

##  Monitores

- `GET /gestion/monitores/` → Listar monitores
- `GET /gestion/monitores/<int:monitor_id>/` → Obtener monitor por ID
- `POST /gestion/monitores/registrar/` → Crear monitor (JSON)
- `POST /gestion/crear_monitor_formulario/` → Crear monitor (formulario HTML)
- `PUT /gestion/monitores/<int:monitor_id>/editar/` → Actualizar monitor
- `DELETE /gestion/monitores/<int:monitor_id>/eliminar/` → Eliminar monitor

---

## Salas

- `GET /gestion/salas/` → Listar salas
- `GET /gestion/salas/<int:sala_id>/` → Obtener sala por ID
- `POST /gestion/salas/registrar/` → Crear sala (JSON)
- `POST /gestion/crear_sala_formulario/` → Crear sala (formulario HTML)
- `PUT /gestion/salas/<int:sala_id>/editar/` → Actualizar sala
- `DELETE /gestion/salas/<int:sala_id>/eliminar/` → Eliminar sala

---

## Responsables de sala

- `GET /gestion/responsables_sala/<int:responsable_sala_id>/` → Obtener responsable por ID
- `POST /gestion/responsables_sala/registrar/` → Crear responsable (JSON)
- `POST /gestion/crear_responsable_sala_formulario/` → Crear responsable (formulario HTML)
- `PUT /gestion/responsables_sala/<int:responsable_sala_id>/editar/` → Actualizar responsable
- `DELETE /gestion/responsables_sala/<int:responsable_sala_id>/eliminar/` → Eliminar responsable

---
## Inscripciones
- `GET /gestion/actividades/<int:actividad_id>/inscripciones/` → Ver usuarios inscritos en una actividad
- `POST /gestion/actividades/<int:actividad_id>/inscribir/` → Inscribir usuario en actividad
- `POST /gestion/actividades/<int:actividad_id>/inscripciones/<int:usuario_id>/eliminar/` → Eliminar inscripción
---
