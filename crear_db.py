import os
import sqlite3
from config import DATABASE, DATA_DIR


def crear_directorio():
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)
        
        
def crear_bases_datos():
    crear_directorio()
    conexion = sqlite3.connect(DATABASE)
    cursor = conexion.cursor()
    
    cursor.execute("""
            CREATE TABLE IF NOT EXISTS espacios(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                codigo TEXT NOT NULL UNIQUE,
                nombre TEXT NOT NULL,
                tipo TEXT NOT NULL,
                capacidad INTEGER NOT NULL,
                ubicacion TEXT,
                estado TEXT NOT NULL 
            )
    """)
    
    conexion.commit()
    conexion.close()
    
    
def insertar_datos_prueba():
    conexion = sqlite3.connect(DATABASE)
    cursor = conexion.cursor()
    cursor.execute("SELECT COUNT(*) FROM espacios")
    cantidad = cursor.fetchone()[0]
    
    if cantidad == 0:
        espacios = [
            (
                "LAB-01",
                "Laboratorio de cómputo 1",
                "Laboratorio",
                30,
                "Edificio A - Nivel 1", 
                "DISPONIBLE"
            ),
            (
                "SUM-01",
                "Salón de usos múltiples",
                "Auditorio",
                100,
                "Edificio Principal", 
                "DISPONIBLE"
            ),
            (
                "SUM-02",
                "Salón de instrumentos",
                "Música",
                50,
                "Edificio Central", 
                "DISPONIBLE"
            )
        ]
        
        cursor.executemany("""
            INSERT INTO espacios(
                codigo, nombre, tipo, capacidad, 
                ubicacion, estado
            )
            VALUES (?,?,?,?,?,?)
        """, espacios)
        
        conexion.commit()
        print("Datos de prueba insertados correctamente")
        
    else: 
        print("La base ya contiene espacios")
        
    conexion.close()
    
    
def main():
    crear_bases_datos()
    insertar_datos_prueba()
    
    print()
    print("Base de datos creada correctamente")
    print(f"Ubicacion: {DATABASE}")
    
if __name__ == "__main__":
    main()