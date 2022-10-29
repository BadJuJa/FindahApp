from sentence_transformers import SentenceTransformer

def search_vector(sentence):
    model = SentenceTransformer('sentence-transformers/stsb-xlm-r-multilingual')

    import pinecone
    pinecone.init(api_key='53c7dfa5-b733-4da8-ab20-c08300657746', environment='us-west1-gcp')

    index = pinecone.Index('books')

    query_sentence = sentence if sentence is not None else ""
    xq = model.encode(query_sentence).tolist()

    result = index.query(xq, top_k=20, includeMetadata=True)
    return result