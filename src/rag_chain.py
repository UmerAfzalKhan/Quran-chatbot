from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

def setup_rag_chain(vectorstore, api_key: str):
    def format_docs(docs):
        return "\n\n".join([doc.page_content for doc in docs])
    
    template = """You are a knowledgeable Islamic scholar assistant. Answer the question based on the provided Quranic verses.
Always provide the reference (Surah name and Ayah number) for each verse you mention.
Be respectful and accurate in your answers.

Context from Quran:
{context}

Question: {question}

Answer with references:"""
    
    prompt = ChatPromptTemplate.from_template(template)
    
    llm = ChatGroq(
        api_key=api_key,
        model="llama-3.1-8b-instant",
        temperature=0.3,
        max_tokens=500
    )
    
    retriever = vectorstore.as_retriever(search_kwargs={"k": 5})
    
    rag_chain = (
        {"context": retriever | format_docs, "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )
    
    def get_response(query):
        try:
            result = rag_chain.invoke(query)
            docs = retriever.invoke(query)
            return {
                'result': result,
                'source_documents': docs
            }
        except Exception as e:
            return {
                'result': f"Error: {str(e)}",
                'source_documents': []
            }
    
    return get_response