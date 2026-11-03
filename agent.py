import os
from dotenv import load_dotenv
from openai import OpenAI
from db import get_schema , run_query

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

MODEL = "gemini-flash-lite-latest"


def generate_sql(question):
    schema = get_schema()

    system_prompt = f"""You are an expert SQLite assistant.
Given the database schema below, write one SQLite SELECT query that answers the user's question.
Return only the SQL query, with no explanation and no markdown.

Important: all text values stored in the database are in English (for example city names like 'Tehran' and product names like 'Laptop'). The user may ask in Persian, so translate any Persian value to its English form before using it in the query.

Schema:
{schema}"""

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": question},
        ],
        temperature=0,
    )

    sql = response.choices[0].message.content
    return sql.replace("```sql", "").replace("```", "").strip()


def answer_in_words(question, columns, rows):
    prompt = f"""The user asked: {question}
The database returned these columns: {columns}
and these rows: {rows}
Answer the user's question in Persian, in one or two short, clear sentences."""

    response = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}],
        temperature=0,
    )
    return response.choices[0].message.content.strip()


if __name__ == "__main__":
    print("AskMyDB is ready. Type 'exit' to quit.")

    while True:
        question = input("\nAsk a question: ").strip()

        if question.lower() == "exit":
            break
        if not question:
            continue

        try:
            sql = generate_sql(question)
            print("SQL:", sql)
            columns, rows = run_query(sql)
            print("Answer:", answer_in_words(question, columns, rows))
        except Exception as error:
            print("Sorry, something went wrong:", error)