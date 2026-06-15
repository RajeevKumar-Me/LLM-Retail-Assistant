from dotenv import load_dotenv
import os

from langchain_google_genai import ChatGoogleGenerativeAI

from langchain_community.utilities import SQLDatabase
from sql_chain import create_sql_chain

from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

from router import llm_router

load_dotenv()

api_key = os.getenv("api_key")

db_user = os.getenv("db_user")
db_password = os.getenv("db_password")
db_host = os.getenv("db_host")
db_name = os.getenv("db_name")

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=api_key,
    temperature=0.7
)

db = SQLDatabase.from_uri(
    f"mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_name}",
    sample_rows_in_table_info=3
)

db_chain = create_sql_chain(
    llm,
    db
)

embedding_function = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vectordb = Chroma(
    persist_directory="./chroma_db",
    embedding_function=embedding_function
)

def main(question):

    response = llm_router(
        question,
        llm,
        db_chain,
        vectordb
    )
    return response

if __name__ == "__main__":
    question = "Which clothes are good for summer workouts?"
    answer = main(question)
    print("\nFinal Answer:\n")
    print(answer)
