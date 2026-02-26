import chromadb
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_core.prompts import PromptTemplate
from langchain_classic.retrievers import ContextualCompressionRetriever

class RAGChain:

    llm = ChatOpenAI(model="gpt-4o-mini")

    def __init__(
        self,
        # LLM that will be used to answer RAG related queries
        llm: ChatOpenAI,
        retriever: ContextualCompressionRetriever,
        prompt: PromptTemplate
    ):  
        self.llm = llm
        self.retriever = retriever
        self.prompt = prompt

    def initVectorStore():

        embeddings = OpenAIEmbeddings(model="text-embedding-3-large")

        vector_store = chromadb(
            collection_name="test_collection",
            embedding_function=embeddings
        )