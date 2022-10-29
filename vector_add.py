import pinecone
import itertools
pinecone.init(api_key="53c7dfa5-b733-4da8-ab20-c08300657746", environment="us-west1-gcp")
pinecone.delete_index('books')
pinecone.create_index('books', 768, pod_type='p1.x1')
def get_valid_data():
    import pandas as pd
    fileId = "15deeuLoKCo8xQNw9XcMwVi0sF2_bJMUH"
    df = pd.read_json(
        f"https://www.googleapis.com/drive/v3/files/{fileId}?alt=media&key=AIzaSyAYoL3_dwzxfmdYcNrTmaux8umwwdxYyfM")
    new_data = []
    for data in df['vectors']:
        new_data.append((data['id'], data['values']))

    return new_data

def chunks(iterable, batch_size=100):
    it = iter(iterable)
    chunk = tuple(itertools.islice(it, batch_size))
    while chunk:
        yield chunk
        chunk = tuple(itertools.islice(it, batch_size))

with pinecone.Index('books', pool_threads=30) as index:
    async_results = [
        index.upsert(vectors=ids_vectors_chunk, async_req=True)
        for ids_vectors_chunk in chunks(get_valid_data(), batch_size=100)
    ]
    [async_result.get() for async_result in async_results]