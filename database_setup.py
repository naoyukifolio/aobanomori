import sqlite3

# データベースファイルに接続（ファイルが存在しなければ新規作成されます）
conn = sqlite3.connect('equipment_management.db')
cursor = conn.cursor()

# テーブルを作成（初めて作成する場合のみ）
cursor.execute('''
    CREATE TABLE IF NOT EXISTS equipment (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        location TEXT NOT NULL,
        installation_date TEXT NOT NULL,
        maintenance_interval INTEGER NOT NULL
    )
''')

# 変更を保存して接続を閉じる
conn.commit()
conn.close()

print("データベースとテーブルが作成されました。")
