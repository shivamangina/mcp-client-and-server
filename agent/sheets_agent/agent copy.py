from langgraph.prebuilt import RunnableWithMessageHistory
from langchain_core.chat_history import ChatMessageHistory
from langchain_core.runnables import Runnable
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.chat_models import ChatPerplexity

# Setup prompt
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    ("human", "{input}")
])

# Use Perplexity model (make sure PERPLEXITY_API_KEY is set in env)
model = ChatPerplexity(model="mistral-7b-instruct", temperature=0.7)

# Chain: prompt -> model -> parser
chain: Runnable = prompt | model | StrOutputParser()

# Wrap with message history (in-memory for dev)
graph = RunnableWithMessageHistory(
    chain,
    get_session_history=lambda session_id: ChatMessageHistory(),
    input_messages_key="input",
    history_messages_key="messages",
)
