from app.database.connection import get_connection

def crear_tabla_faq():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS faq (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            pregunta TEXT,
            respuesta TEXT
        );
    """)
    conn.commit()
    conn.close()

def insertar_faq(pregunta, respuesta):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO faq (pregunta, respuesta) VALUES (?,?)", (pregunta, respuesta))
    conn.commit()
    conn.close()

def obtener_faqs():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, pregunta, respuesta FROM faq")
    data = cur.fetchall()
    conn.close()
    return data
