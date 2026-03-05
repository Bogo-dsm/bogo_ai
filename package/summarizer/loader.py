from langchain_community.document_loaders import PDFPlumberLoader

loader = PDFPlumberLoader("testpdf.pdf")

docs = loader.load()

texts = str()

for doc in docs:
    texts += doc.page_content
print(texts)

