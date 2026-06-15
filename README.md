# Retail AI Assistant

An intelligent retail analytics assistant that combines SQL-based inventory querying with Retrieval-Augmented Generation (RAG) to provide accurate, context-aware responses to natural language questions.

## Overview

Retail AI Assistant is a hybrid AI system designed to answer both structured and semantic retail queries.

The application uses a routing layer powered by Google's Gemini model to determine the most appropriate retrieval strategy:

* **SQL Pipeline** for inventory, stock, pricing, and structured business data
* **RAG Pipeline** for semantic search, product recommendations, and contextual information

This architecture ensures that factual inventory questions are answered directly from the database while recommendation-style questions leverage vector search and embeddings.

---

## Key Features

### Natural Language to SQL

Ask business questions in plain English:

* How many Nike small t-shirts are available?
* What products currently have discounts?
* Show Adidas inventory levels.

### Retrieval-Augmented Generation (RAG)

Retrieve semantically relevant product information using vector embeddings.

Examples:

* Which clothes are suitable for summer workouts?
* Recommend products for hot weather.
* What apparel is best for rainy days?

### Intelligent Query Routing

The application automatically decides whether a query should be answered using:

* MySQL Database
* ChromaDB Vector Store

No manual selection is required.

### Interactive Web Interface

Built with Streamlit for a simple and responsive user experience.

---

## System Architecture

User Query
↓
Gemini Router
↓
┌──────────────┬──────────────┐
│              │              │
SQL Pipeline   RAG Pipeline
│              │
MySQL          ChromaDB
│              │
└──── Gemini Response ────┘
↓
Final Answer

---

## Technology Stack

| Component    | Technology                     |
| ------------ | ------------------------------ |
| LLM          | Gemini 2.5 Flash               |
| Framework    | LangChain                      |
| Database     | MySQL                          |
| Vector Store | ChromaDB                       |
| Embeddings   | HuggingFace (all-MiniLM-L6-v2) |
| Frontend     | Streamlit                      |
| Language     | Python                         |

---

## Project Structure

```text
Retail-AI-Assistant/

├── app.py
├── main.py
├── router.py
├── sql_chain.py
├── rag_pipeline.py
├── create_vectorDB.py
├── retail_shop.sql
├── README.md
└── LLM project.ipynb
```

## Installation

### Clone Repository

```bash
git clone <your-repository-url>
cd Retail-AI-Assistant
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment Variables

Create a `.env` file:

```env
api_key=YOUR_GEMINI_API_KEY

db_user=root
db_password=YOUR_PASSWORD
db_host=localhost
db_name=retail_shop
```

### Create Database

Run:

```sql
SOURCE retail_shop.sql;
```

### Build Vector Database

```bash
python create_vectorDB.py
```

### Launch Application

```bash
streamlit run app.py
```

---

## Example Queries

### Inventory Analytics

* How many Nike small t-shirts are available?
* What is the total stock of Adidas products?
* Which products have active discounts?

### Product Discovery

* Recommend clothes for summer workouts.
* Which products are comfortable for hot weather?
* What apparel works best during rainy seasons?

---

## Skills Demonstrated

* Retrieval-Augmented Generation (RAG)
* Large Language Models (LLMs)
* Natural Language to SQL
* Vector Databases
* Embedding Models
* Semantic Search
* AI Routing Systems
* Streamlit Application Development
* Data Pipeline Design

---

## Future Enhancements

* PDF-based document retrieval
* Customer review analysis
* Advanced recommendation engine
* FastAPI deployment
* Cloud deployment
* Multi-agent architecture

---

## Author

Rajeev Kumar

Data Science & AI Enthusiast
