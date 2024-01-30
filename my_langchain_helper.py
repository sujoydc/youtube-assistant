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

    return db

def get_response_from_query(db, query, k=4):
    # Model gpt-4-0613 can handle 8,192 tokens
    docs = db.similarity_search(query, k=k)
    docs_page_content = " ".join([d.page_content for d in docs])

    llm = OpenAI(model="gpt-3.5-turbo")

    prompt = PromptTemplate(
        input_variables=["questions", "docs"],
        template="""
        Act as a YouTube assistant that can answer questions about
        videos based on the video's transcript.

        Answer the following question: {question}
        By searching the following video transcript: {docs}

        Only use the factual information from the transcript to answer the question. 

        If you feel like you don't have enough information to answer the question, 
        say "I don't know".

        Your answer should be detailed. 
        """
    )

    chain = LLMChain(llm=llm, prompt=prompt)

    response = chain.run(question=query, docs=docs_page_content)
    response = response.replace("\n", "")


if __name__ == "__main__":
    print(create_vector_db_from_youtube_link(mylink))
    


