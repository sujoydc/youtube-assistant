from langchain_openai import OpenAI
from langchain_openai import OpenAIEmbeddings
from langchain_community.document_loaders import YoutubeLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_community.vectorstores.faiss import FAISS

from dotenv import load_dotenv

# This loads the .env file which has the API Key
load_dotenv()

embeddings = OpenAIEmbeddings()


mylink = "https://www.youtube.com/watch?v=bEcSogiDwTw"

def create_vector_db_from_youtube_link(link: str) -> FAISS:
    video_loader = YoutubeLoader.from_youtube_url(link)
    video_transcript = video_loader.load()

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000,
                                                   chunk_overlap=100
                                                   )
    
    docs = text_splitter.split_documents(video_transcript)

    db = FAISS.from_documents(docs, embeddings)

    return docs # db
    

if __name__ == "__main__":
    print(create_vector_db_from_youtube_link(mylink))
    


