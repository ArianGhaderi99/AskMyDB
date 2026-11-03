# AskMyDB 🗄️🤖

**Ask your database questions in plain language (English or Persian) and get answers in Persian.**
**از دیتابیس‌ات به زبان ساده سؤال بپرس و جواب فارسی بگیر.**

[English](#-english) | [فارسی](#-فارسی)

---

## 🇬🇧 English

### What is AskMyDB?

AskMyDB is a small **Text-to-SQL agent** written in Python. You type a question like *"How many orders has each customer placed?"* (in English or Persian), and the app:

1. reads the database schema,
2. asks an LLM (Google Gemini) to write a SQL query,
3. runs the query safely on a **read-only** database,
4. turns the raw result into a short, natural answer in Persian.

### How it works

```
Question → Schema + Question → LLM → SQL → Safe execution (read-only) → Raw result → LLM → Persian answer
```

### Features

- 💬 Natural-language questions in English or Persian
- 🔒 **Two safety layers**: only `SELECT` queries are accepted, and the database is opened in read-only mode, so the model can never change or delete data
- 🧠 Schema-aware prompting, so the model knows your tables and columns
- 🌐 Persian answers generated from the query result
- 🛡️ Error handling: a wrong query never crashes the app
- 🔑 API key kept out of the code (`.env` file)

### Tech stack

- Python 3
- SQLite
- Google Gemini API (through the OpenAI-compatible endpoint, using the `openai` library)
- `python-dotenv`

### Project structure

```
AskMyDB/
├── agent.py            # Talks to the LLM: generates SQL and writes the final answer
├── db.py               # Reads the schema and runs read-only queries
├── create_db.py        # Creates the sample shop database
├── .env                # Your API key (not uploaded to GitHub)
├── .gitignore
└── README.md
```

### Getting started

**1. Clone the project**

```bash
git clone https://github.com/ArianGhaderi99/AskMyDB.git
cd AskMyDB
```

**2. Create and activate a virtual environment**

```bash
python -m venv .venv
.venv\Scripts\activate        # Windows
source .venv/bin/activate     # macOS / Linux
```

**3. Install the dependencies**

```bash
pip install openai python-dotenv
```

**4. Add your API key**

Get a free key from [Google AI Studio](https://aistudio.google.com), then create a `.env` file in the project folder:

```
GEMINI_API_KEY=your_key_here
```

**5. Create the sample database**

```bash
python create_db.py
```

**6. Run the app**

```bash
python agent.py
```

### Example

```
Ask a question: هر مشتری چندتا سفارش داده؟
SQL: SELECT c.name, COUNT(o.id) FROM customers c LEFT JOIN orders o ON c.id = o.customer_id GROUP BY c.id, c.name
Answer: تعداد سفارش‌های هر مشتری به این صورت است: علی ۲ سفارش، و سارا، رضا و مینا هر کدام ۱ سفارش ثبت کرده‌اند.
```

### Sample database

The demo database (`shop.db`) has three tables: `customers`, `products`, and `orders`. You can point the app to your own SQLite file by changing `db_path` in `db.py`.


### Author

**Arian Ghaderi** — [GitHub: @ArianGhaderi99](https://github.com/ArianGhaderi99)

---

## 🇮🇷 فارسی

<div dir="rtl">

### AskMyDB چیست؟

AskMyDB یک **ایجنت Text-to-SQL** کوچک است که با پایتون نوشته شده. شما یک سؤال مثل «هر مشتری چند سفارش داده؟» را (به فارسی یا انگلیسی) می‌نویسید و برنامه:

۱. ساختار دیتابیس را می‌خواند،
۲. از یک مدل زبانی (Google Gemini) می‌خواهد کوئری SQL بنویسد،
۳. کوئری را روی دیتابیسِ **فقط‌خواندنی** با امنیت اجرا می‌کند،
۴. نتیجه‌ی خام را به یک جواب کوتاه و روان فارسی تبدیل می‌کند.

### نحوه‌ی کار

```
سؤال ← ساختار دیتابیس + سؤال ← مدل ← SQL ← اجرای امن (فقط‌خواندنی) ← نتیجه‌ی خام ← مدل ← جواب فارسی
```

### ویژگی‌ها

- 💬 پرسیدن سؤال با زبان طبیعی، فارسی یا انگلیسی
- 🔒 **دو لایه‌ی امنیتی**: فقط کوئری‌های `SELECT` پذیرفته می‌شوند و دیتابیس در حالت فقط‌خواندنی باز می‌شود، پس مدل هرگز نمی‌تواند داده‌ای را تغییر دهد یا پاک کند
- 🧠 آگاه به ساختار دیتابیس، تا مدل جدول‌ها و ستون‌ها را بشناسد
- 🌐 جواب فارسی بر اساس نتیجه‌ی کوئری
- 🛡️ مدیریت خطا: یک کوئری اشتباه برنامه را از کار نمی‌اندازد
- 🔑 کلید API بیرون از کد و در فایل `.env` نگهداری می‌شود

### تکنولوژی‌ها

- پایتون ۳
- SQLite
- Google Gemini API (از طریق endpoint سازگار با OpenAI و کتابخانه‌ی `openai`)
- `python-dotenv`

### ساختار پروژه

</div>

```
AskMyDB/
├── agent.py            # ارتباط با مدل: ساخت SQL و نوشتن جواب نهایی
├── db.py               # خواندن ساختار دیتابیس و اجرای کوئری فقط‌خواندنی
├── create_db.py        # ساخت دیتابیس نمونه‌ی فروشگاه
├── .env                # کلید API شما (در گیت‌هاب آپلود نمی‌شود)
├── .gitignore
└── README.md
```

<div dir="rtl">

### راه‌اندازی

**۱. کلون کردن پروژه**

</div>

```bash
git clone https://github.com/ArianGhaderi99/AskMyDB.git
cd AskMyDB
```

<div dir="rtl">

**۲. ساخت و فعال‌سازی محیط مجازی**

</div>

```bash
python -m venv .venv
.venv\Scripts\activate        # Windows
source .venv/bin/activate     # macOS / Linux
```

<div dir="rtl">

**۳. نصب کتابخانه‌ها**

</div>

```bash
pip install openai python-dotenv
```

<div dir="rtl">

**۴. اضافه کردن کلید API**

یک کلید رایگان از [Google AI Studio](https://aistudio.google.com) بگیرید و در پوشه‌ی پروژه فایل `.env` بسازید:

</div>

```
GEMINI_API_KEY=your_key_here
```

<div dir="rtl">

**۵. ساخت دیتابیس نمونه**

</div>

```bash
python create_db.py
```

<div dir="rtl">

**۶. اجرای برنامه**

</div>

```bash
python agent.py
```

<div dir="rtl">

### نمونه‌ی اجرا

</div>

```
Ask a question: هر مشتری چندتا سفارش داده؟
SQL: SELECT c.name, COUNT(o.id) FROM customers c LEFT JOIN orders o ON c.id = o.customer_id GROUP BY c.id, c.name
Answer: تعداد سفارش‌های هر مشتری به این صورت است: علی ۲ سفارش، و سارا، رضا و مینا هر کدام ۱ سفارش ثبت کرده‌اند.
```

<div dir="rtl">

### دیتابیس نمونه

دیتابیس دمو (`shop.db`) سه جدول دارد: `customers`، `products` و `orders`. می‌توانید با تغییر `db_path` در فایل `db.py` برنامه را به فایل SQLite خودتان وصل کنید.


### سازنده

**آرین قادری** — [گیت‌هاب: @ArianGhaderi99](https://github.com/ArianGhaderi99)

</div>
