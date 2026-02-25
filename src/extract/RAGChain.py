from langchain_openai import ChatOpenAI
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