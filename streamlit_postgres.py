import streamlit as st
import psycopg2

# Configuration de la connexion PostgreSQL
DB_HOST = "postgres-service"
DB_NAME = "testdb"
DB_USER = "admin"
DB_PASS = "password"

# Connexion à la base de données
def get_connection():
    return psycopg2.connect(
        host=DB_HOST, 
        dbname=DB_NAME, 
        user=DB_USER, 
        password=DB_PASS
    )

# Création de la table si elle n'existe pas
def init_db():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS messages (
            id SERIAL PRIMARY KEY,
            content TEXT NOT NULL
        )
    """)
    conn.commit()
    cur.close()
    conn.close()

# Interface utilisateur avec Streamlit
st.title("Interface PostgreSQL avec Streamlit")
init_db()

# Ajouter un message
message = st.text_area("Ajouter un message")
if st.button("Enregistrer"):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO messages (content) VALUES (%s)", (message,))
    conn.commit()
    cur.close()
    conn.close()
    st.success("Message enregistré !")

# Afficher les messages enregistrés
conn = get_connection()
cur = conn.cursor()
cur.execute("SELECT * FROM messages")
rows = cur.fetchall()
cur.close()
conn.close()

st.subheader("Messages enregistrés")
for row in rows:
    st.write(f"{row[0]} - {row[1]}")

