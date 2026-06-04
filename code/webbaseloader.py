import os
from langchain_community.document_loaders import WebBaseLoader

os.environ["USER_AGENT"] = "Gaurang-test-LangChain-Bot/1.0"

loader = WebBaseLoader(
    web_paths=("https://www.team-bhp.com/forum/official-new-car-reviews/308952-2026-honda-city-facelift-review.html",)
)

docs = loader.load()

print(f"Documents Loaded: {len(docs)}")
# print(docs)