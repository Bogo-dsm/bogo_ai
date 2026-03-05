from langchain_community.document_loaders import PDFPlumberLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

loader = PDFPlumberLoader("testpdf.pdf")
docs = loader.load()

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size = 300,
    chunk_overlap = 0
)

text = str()
for doc in docs:
    text += doc.page_content

import re

text = text.replace('\n\n','[[NEWLINE]]')
text = re.sub(r'\n\s*-\s*\d+\s*-\s*\n', '\n', text)
text = re.sub(r'(?<![.!?])\n', ' ', text)
text = text.replace('[[NEWLINE]]','\n\n')
text = re.sub(r' +', ' ', text)
text = text.strip()

recursive_text = text_splitter.split_text(text)

for i,chunk in enumerate(recursive_text):
    print(f"-----{i+1}번째 chunk-----")
    print(chunk, end='\n\n')

