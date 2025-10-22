# 🚀 Proyecto Auralink2

_Auralink2_ es un proyecto desarrollado en **Python 3 y Django**, pensado para funcionar como una aplicación web modular y escalable.  
Este repositorio contiene el código fuente, las dependencias necesarias y la configuración básica para ejecutarlo en un entorno local.

---

## 📦 Requisitos previos

Antes de ejecutar el proyecto, asegúrate de tener instalado en tu sistema:

- [Python 3.10 o superior](https://www.python.org/downloads/)
- [Git](https://git-scm.com/downloads)
- Un editor de código (recomendado: [Visual Studio Code](https://code.visualstudio.com/))
- (Opcional) [GitHub CLI](https://cli.github.com/)

---

## ⚙️ Instalación y configuración

Sigue estos pasos para clonar y ejecutar el proyecto en tu equipo local:

### 1️⃣ Clonar el repositorio

Abre tu terminal y ejecuta:

```bash
git clone https://github.com/DanielOteroU/Auralink2.git
cd Auralink2
```

---

### 2️⃣ Crear un entorno virtual

Crea y activa el entorno virtual para aislar las dependencias del proyecto:

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Linux / macOS:**
```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 3️⃣ Instalar dependencias

Instala las librerías requeridas usando `requirements.txt`:

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Configurar base de datos

El proyecto usa **SQLite3** (archivo `db.sqlite3`) por defecto.  
Si es la primera vez que lo ejecutas o no tienes el archivo, crea la base de datos inicial con:

```bash
python manage.py migrate
```

---

### 5️⃣ Ejecutar el servidor de desarrollo

Para iniciar el servidor de Django:

```bash
python manage.py runserver
```

Luego abre tu navegador en:

👉 http://127.0.0.1:8000/

---

## 🧩 Estructura del proyecto

```
Auralink2/
│
├── core/                  # Aplicaciones y configuración principal de Django
├── auralink_new/          # Módulos adicionales o nuevas funcionalidades
├── media/                 # Archivos subidos (imágenes, etc.)
├── tools/                 # Scripts o herramientas adicionales
│
├── manage.py              # Script principal de Django
├── db.sqlite3             # Base de datos local
├── requirements.txt       # Dependencias del proyecto
└── README.md              # Documentación del proyecto
```

---

## 🧱 Variables de entorno (opcional)

Si el proyecto usa credenciales, crea un archivo `.env` en la raíz del proyecto con tus configuraciones, por ejemplo:

```
SECRET_KEY=tu_clave_secreta
DEBUG=True
DATABASE_URL=sqlite:///db.sqlite3
```

> ⚠️ **Nunca subas tu archivo `.env` a GitHub.** Mantén tus claves privadas en tu máquina local.

---

## 🧰 Comandos útiles

| Acción                          | Comando                                   |
|---------------------------------|-------------------------------------------|
| Crear migraciones               | `python manage.py makemigrations`         |
| Aplicar migraciones             | `python manage.py migrate`                |
| Crear superusuario admin        | `python manage.py createsuperuser`        |
| Ejecutar servidor               | `python manage.py runserver`              |
| Salir del entorno virtual       | `deactivate`                              |

---

## 🤝 Contribuciones

Si deseas contribuir al proyecto, crea una rama con tus cambios:

```bash
git checkout -b nombre-rama
git add .
git commit -m "Descripción de los cambios"
git push origin nombre-rama
```

Luego abre un **Pull Request** en GitHub.

---

## 🧾 Licencia

Este proyecto es de uso interno y privado.  
No está destinado a distribución pública sin autorización del autor.

---

## 💬 Autor

**Daniel Otero & Constanza Cabello**  
📧 [daniel.otero@inacapmail.cl](mailto:daniel.otero@inacapmail.cl)  
👨‍💻 [Perfil en GitHub](https://github.com/DanielOteroU)  
💼 Estudiante de Ingeniería Informática
