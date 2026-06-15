from rag_pipeline import rag_pipeline

def llm_router(question, llm, db_chain, vectordb):

    router_prompt = f"""

    You are an AI router.

    Decide whether the question should use:

    SQL:
    - inventory
    - stock
    - quantity
    - price
    - structured data

    OR

    RAG:
    - recommendations
    - semantic meaning
    - descriptions
    - general understanding

    Return ONLY:
    SQL
    or
    RAG

    Question:
    {question}

    """

    route = llm.invoke(router_prompt).content.strip()

    print("Route Chosen:", route)

    
    if route.upper() == "SQL":

        response = db_chain.invoke({"query": question})

        return response["result"]

    
    else:

        response = rag_pipeline(

            question,

            vectordb,

            llm
        )

        return response