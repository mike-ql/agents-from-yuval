from langchain_text_splitters import RecursiveCharacterTextSplitter
import extract_pdf


def prepare_agent():
    doc_texts = extract_pdf.extract_all_docs()
    all_chunks = make_chunks(doc_texts)
    print(f"Created {len(all_chunks)} chunks")
    print(all_chunks[0])



def make_chunks(list_of_texts):
    # Simple chunking
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    # Split all documents
    all_chunks = []
    for text in list_of_texts:
        chunks = text_splitter.split_text(text)
        all_chunks.extend(chunks)

    return all_chunks


prepare_agent()