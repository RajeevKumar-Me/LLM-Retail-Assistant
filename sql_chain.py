from langchain_experimental.sql import SQLDatabaseChain

def create_sql_chain(llm, db):

    db_chain = SQLDatabaseChain.from_llm(

        llm,

        db,

        verbose=True,
        return_direct = False
    )

    return db_chain