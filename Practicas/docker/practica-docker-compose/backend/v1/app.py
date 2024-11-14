from flask import Flask, jsonify, request, redirect, url_for
import os
import mysql.connector
import logging
import random
import string

app = Flask(__name__)

# Configurar el nombre de la aplicación y el nivel de registro
app_name = os.getenv("APP_NAME", "Nuestra primera aplicación desplegada en k8s")
log_level = os.getenv("LOG_LEVEL", "INFO").upper()
external_api_url = os.getenv("EXTERNAL_API_URL", "https://default-url.com")

# Configurar el nivel de registro
logging.basicConfig(level=getattr(logging, log_level, logging.INFO))
logger = logging.getLogger(__name__)

# Función para establecer la conexión con la base de datos MySQL
def get_db_connection():
    conn = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")
    )
    return conn

# Función para generar un nombre y una edad aleatorios
def generate_random_user():
    name = ''.join(random.choices(string.ascii_letters, k=5))
    age = random.randint(18, 100)  # Edad aleatoria entre 18 y 100
    return name, age

@app.route('/')
def home():
    logger.info(f"Accessing the home route of {app_name}")
    # Mostrar las variables de entorno en la pantalla web y un botón para añadir un usuario
    return (
        f"<h1>Hola. Es la version: v1!</h1>"
        f"<h1>Welcome to {app_name}!</h1>"
        f"<p>Log Level: {log_level}</p>"
        f"<p>External API URL: {external_api_url}</p>"
    )


@app.route('/usuario', methods=['GET', 'POST'])
def add_user():
    try:
        # Generar un nombre y una edad aleatorios
        name, age = generate_random_user()

        # Conectar a la base de datos e insertar un usuario aleatorio
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (name, age) VALUES (%s, %s);", (name, age))
        conn.commit()
        cursor.close()
        conn.close()

        logger.info(f"Usuario {name} de {age} años añadido con éxito a la base de datos.")
        return (
        f"<h1>Usuario aleatorio creado!</h1>"
        )

    except Exception as e:
        logger.error(f"Error al añadir un usuario: {e}")
        return str(e), 500

@app.route('/data')
def get_data():
    try:
        # Conectar a la base de datos y ejecutar una consulta
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users;")  # Asegúrate de que la tabla se llama 'users'
        rows = cursor.fetchall()
        cursor.close()
        conn.close()

        # Devuelve los datos como JSON
        return jsonify(rows)
    except Exception as e:
        return str(e), 500

@app.route('/health')
def health():
    return "OK"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)