# Boilerplate Flask

## Tablas

- Usuarios (users)

| columna   | tipo         | opciones      |
| --------- | ------------ | ------------- |
| id        | SERIAL       | PRIMARY KEY   |
| name      | VARCHAR(120) | NOT NULL      |
| last_name | VARCHAR(150) | NOT NULL      |
| username  | VARCHAR(80)  | UNIQUE        |
| password  | VARCHAR(255) | NOT NULL      |
| email     | VARCHAR(160) | UNIQUE        |
| rol_id    | INT          | FOREIGN KEY   |
| status    | BOOLEAN      | DEFAULT(true) |

- Roles (roles)

| columna | tipo        | opciones      |
| ------- | ----------- | ------------- |
| id      | SERIAL      | PRIMARY KEY   |
| name    | VARCHAR(30) | NOT NULL      |
| status  | BOOLEAN     | DEFAULT(true) |

## Caracteristicas

1. Login
   - [] Integrar JWT
   - [] Validar el hash de las contraseñas
2. Registro
   - [] Encriptacion Contraseñas (bcrypt)
3. Reseteo Contraseña
   - [] Enviar un correo con la contraseña nueva, en un template (HTML)
4. CRUD para cada Tabla
   - [] Listado con paginación
   - [] Obtener un registro por ID
   - [X] Creación de un registro
   - [] Actualzación de un registro por ID
   - [] Eliminar un registro por ID (Soft Delete)
5. Decoderadores
   - [] Proteger las rutas por autenticación
   - [] Proteger las rutas por rol
6. Documentación
   - [X] Swagger OpenAPI
7. Despliegue
   - [] Render (PAAS)

## MVC (Modelo - Vista - Controlador)

Se utiliza para separar responsabilidades de una aplicación.

1. Modelo (Model)

   - Representa a **la logica de negocio**, y a **los datos** de la aplicacion.
   - Se encarga de la logica interna, como las interacciones con la BD, **validaciones** y **reglas de negocio**.

2. Vista (View)

   - Es la interfaz de usuario que muestra los datos provenientes del modelo.
   - Se encarga de la presentación, de como visualiza los datos el usuario final.

3. Controlador (Controller)
   - Actua como un intermediario entre el modelo y la vista.
   - Contiene la logica que responde a la accion del usuario.

### Flujo de trabajo MVC en un API REST

```curl
POST http://miapi.com.pe/users
```

1. El controlador recibe la solicitud HTTP del cliente.
2. El controlador interactuar con el modelo, para obtener los datos solicitados
3. El controlador formatea la respuesta obtenida del modelo, y la devuelve en formato JSON (Este es la vista en un contexto de una API REST).
4. El cliente (Frontend) recibe la respuesta en formato, y la procesa de acuerdo a su necesidad.

## PIP

```sh
pip install Flask Flask-SQLAlchemy psycopg2-binary python-dotenv sqlalchemy_mixins Flask-Migrate
```

## .env

```py
FLASK_APP='main.py'
FLASK_RUN_HOST=127.0.0.1
FLASK_RUN_PORT=5000
FLASK_DEBUG=True

DATABASE_URI='postgresql://username:password@ip_server:port/database_name'
```

## Documentación

- SQLAlchemy
  - [Metodos](https://docs.sqlalchemy.org/en/14/orm/query.html#sqlalchemy.orm.Query.all)
  - [Tipo de Datos](https://docs.sqlalchemy.org/en/14/core/types.html)
  - [Metodos Optimos](https://github.com/absent1706/sqlalchemy-mixins/blob/master/README.md)
- FlaskRestX
  - [Campos Esquema (Validaciones)](https://flask-restx.readthedocs.io/en/latest/_modules/flask_restx/fields.html)
  - [Swagger](https://flask-restx.readthedocs.io/en/latest/swagger.html)

## Migraciones

- Iniciar alembic (se ejecuta una sola vez, solo si no existe una carpeta **migrations**)

```ssh
flask db init
```

- Generar una migración (cuando se crea o se modifica un modelo, se debe ejecutar el comando)

```ssh
flask db migrate -m "comentario"
```

- Ejecutar migraciones

```ssh
flask db upgrade
```