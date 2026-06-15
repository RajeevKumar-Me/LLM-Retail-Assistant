def rag_pipeline(query, vectordb, llm):

    docs = vectordb.similarity_search(

        query,

        k=2
    )

    context = "\n".join(

        [doc.page_content for doc in docs]
    )

    prompt = f"""

    Use the context below to answer the question.

    Context:
    {context}

    Question:
    {query}

    """

    response = llm.invoke(prompt)

    return response.content