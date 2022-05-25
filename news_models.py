from db import get_db

# ambil semua data news
def get_news():
    db = get_db()
    cursor = db.cursor()
    #SELECT
    query = "SELECT id, title, content, datetime FROM tbl_news_0432"
    cursor.execute(query)
    columns = [column[0] for column in cursor.description] #ambil nama kolom
    result = []
    
    for row in cursor.fetchall():
        result.append(dict(zip(columns, row))) #konversi ke dictionary
        
    return result

# ambil data news berdasarkan id
def get_news_by_id(id):
    db = get_db()
    cursor = db.cursor()
    #SELECT
    query = "SELECT id, title, content, datetime FROM tbl_news_0432 WHERE id = ?"
    cursor.execute(query, [id])
    columns = [column[0] for column in cursor.description] #ambil nama kolom
    result = []
    result.append(dict(zip(columns, cursor.fetchone()))) #konversi ke dictionary
        
    return result

# menambahkan data news
def insert_news(title, content, datetime):
    db = get_db()
    cursor = db.cursor()
    query = "INSERT INTO tbl_news_0432(title, content, datetime) VALUES (?,?,?)"
    cursor.execute(query, [title, content, datetime])
    db.commit()
    return True
    

# mengubah data news
def update_news(id, title, content, datetime):
    db = get_db()
    cursor = db.cursor()
    query = "UPDATE tbl_news_0432 SET id = ?, title = ?, content = ?, datetime = ? WHERE id = ?"
    cursor.execute(query, [id, title, content, datetime, id])
    db.commit()
    return True

# menghapus data news
def delete_news(id):
    db = get_db()
    cursor = db.cursor()
    query = "DELETE FROM tbl_news_0432 WHERE id = ?"
    cursor.execute(query, [id])
    db.commit()
    return True
