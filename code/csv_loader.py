from langchain_community.document_loaders import CSVLoader

loader = CSVLoader(file_path="csv_data.csv")
docs = loader.load()
print(docs)