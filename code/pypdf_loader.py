from langchain_community.document_loaders import PyPDFLoader
loader = PyPDFLoader("docklink.pdf")

docs = loader.load()

# print(docs)
# print(type(docs))
# print(docs[0].page_content)
print(docs[0].metadata)
