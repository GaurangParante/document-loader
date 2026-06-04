from langchain_community.document_loaders import DirectoryLoader,PyPDFLoader

loader = DirectoryLoader('data_fol',glob="*.pdf",loader_cls=PyPDFLoader)

docs = loader.lazy_load()

for document in docs:
    print(document.metadata)