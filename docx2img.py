# Import Section
from docx import Document

# Load the document
doc = Document('Document.docx')

# Extract text from paragraphs
text = []
for paragraph in doc.paragraphs:
    text.append(paragraph.text)

# Join the list into a single string, if needed
full_text = '\n'.join(text)

# Print the extracted text
print(full_text)


