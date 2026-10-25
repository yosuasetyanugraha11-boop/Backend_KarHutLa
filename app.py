import os
from flask import Flask, jsonify, request
from flask_cors import CORS
import psycopg2
from psycopg2.extras import RealDictCursor

app = Flask(__name__)
CORS(app)

# Fungsi helper untuk koneksi ke Database (misal: Supabase / Neon PostgreSQL)
def get_db_connection():
    conn = psycopg2.connect(
        os.environ.get("DATABASE_URL"),
        cursor_factory=RealDictCursor
    )
    return conn

@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "API Sistem Informasi Kebakaran Aktif",
        "endpoints": [
            "GET /laporan",
            "POST /laporan",
            "PUT /laporan/<id>",
            "DELETE /laporan/<id>"
        ]
    })

# 1. GET: Mengambil semua data laporan kebakaran beserta relasinya
@app.route("/laporan", methods=["GET"])
def get_laporan():
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("""
            SELECT l.id_laporan, p.nama AS pelapor, w.nama_wilayah, l.deskripsi, l.status, l.tanggal_lapor 
            FROM laporan_kebakaran l
            JOIN pengguna p ON l.id_pengguna = p.id_pengguna
            JOIN wilayah w ON l.id_wilayah = w.id_wilayah
            ORDER BY l.tanggal_lapor DESC;
        """)
        laporan = cur.fetchall()
        cur.close()
        conn.close()
        return jsonify({"status": "success", "data": laporan}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# 2. POST: Menambah laporan kebakaran baru
@app.route("/laporan", methods=["POST"])
def add_laporan():
    data = request.get_json()
    
    # Validasi input sederhana
    if not data or not data.get("id_pengguna") or not data.get("id_wilayah") or not data.get("deskripsi"):
        return jsonify({"error": "Field id_pengguna, id_wilayah, dan deskripsi wajib diisi"}), 400

    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(
            """
            INSERT INTO laporan_kebakaran (id_pengguna, id_wilayah, deskripsi, status)
            VALUES (%s, %s, %s, %s) RETURNING id_laporan, deskripsi, status, tanggal_lapor;
            """,
            (data["id_pengguna"], data["id_wilayah"], data["deskripsi"], data.get("status", "Pending"))
        )
        new_laporan = cur.fetchone()
        conn.commit()
        cur.close()
        conn.close()
        return jsonify({"message": "Laporan kebakaran berhasil ditambahkan", "data": new_laporan}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# 3. PUT: Mengubah status atau data laporan berdasarkan ID
@app.route("/laporan/<int:id_laporan>", methods=["PUT"])
def update_laporan(id_laporan):
    data = request.get_json()
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        
        # Cek apakah data ada
        cur.execute("SELECT * FROM laporan_kebakaran WHERE id_laporan = %s", (id_laporan,))
        existing = cur.fetchone()
        if not existing:
            cur.close()
            conn.close()
            return jsonify({"error": "Laporan tidak ditemukan"}), 404

        deskripsi = data.get("deskripsi", existing["deskripsi"])
        status = data.get("status", existing["status"])

        cur.execute(
            """
            UPDATE laporan_kebakaran 
            SET deskripsi = %s, status = %s 
            WHERE id_laporan = %s RETURNING id_laporan, deskripsi, status;
            """,
            (deskripsi, status, id_laporan)
        )
        updated = cur.fetchone()
        conn.commit()
        cur.close()
        conn.close()
        return jsonify({"message": "Laporan berhasil diperbarui", "data": updated}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# 4. DELETE: Menghapus laporan kebakaran
@app.route("/laporan/<int:id_laporan>", methods=["DELETE"])
def delete_laporan(id_laporan):
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        
        cur.execute("SELECT * FROM laporan_kebakaran WHERE id_laporan = %s", (id_laporan,))
        if not cur.fetchone():
            cur.close()
            conn.close()
            return jsonify({"error": "Laporan tidak ditemukan"}), 404

        cur.execute("DELETE FROM laporan_kebakaran WHERE id_laporan = %s", (id_laporan,))
        conn.commit()
        cur.close()
        conn.close()
        return jsonify({"message": "Laporan berhasil dihapus"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)