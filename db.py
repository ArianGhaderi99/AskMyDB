import sqlite3


def get_schema(db_path="shop.db"):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tables = [row[0] for row in cur.fetchall()]

    lines = []
    for table in tables:
        cur.execute(f"PRAGMA table_info({table})")
        columns = [f"{col[1]} ({col[2]})" for col in cur.fetchall()]
        lines.append(f"Table {table}: " + ", ".join(columns))

    conn.close()
    return "\n".join(lines)


def run_query(sql, db_path="shop.db"):
    if not sql.strip().lower().startswith("select"):
        raise ValueError("Only SELECT queries are allowed.")

    conn = sqlite3.connect(f"file:{db_path}?mode=ro", uri=True)
    cur = conn.cursor()
    cur.execute(sql)
    columns = [col[0] for col in cur.description]
    rows = cur.fetchall()
    conn.close()
    return columns, rows


if __name__ == "__main__":
    print(get_schema())
    print(run_query("SELECT * FROM customers"))