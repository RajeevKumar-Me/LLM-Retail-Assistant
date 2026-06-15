from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

products = [

    "Nike breathable running t-shirt for summer workouts",

    "Adidas lightweight gym wear for hot weather",

    "Levi heavy cotton winter hoodie",

    "Nike stretchable sports t-shirt for training",

    "Adidas moisture-wicking fitness wear",

    "Van Huesen formal white office shirt",

    "Black cotton hoodie for winter",

    "Blue oversized casual t-shirt",

    "Sweat resistant gym t-shirt",

    "Comfortable clothes for rainy season"

]

embedding_function = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vectordb = Chroma.from_texts(

    texts=products,

    embedding=embedding_function,

    persist_directory="./chroma_db"
)

print("ChromaDB Created Successfully")