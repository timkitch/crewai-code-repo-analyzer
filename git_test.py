from git import Repo

from langchain_community.document_loaders.generic import GenericLoader
from langchain_community.document_loaders.parsers import LanguageParser
from langchain_text_splitters import Language

import os
import json

# Clone
repo_path = "/home/timkitch/ai-projects/crewai-code-repo-analyzer/remote_repo/confluence_rag_app"
if not os.path.exists(repo_path):
    repo = Repo.clone_from("https://github.com/timkitch/confluence_rag_app.git", to_path=repo_path)
else:
    print("Local repo path already exists")

# Load
loader = GenericLoader.from_filesystem(
    repo_path,
    glob="**/*",
    suffixes=[".py"],
    exclude=["**/non-utf8-encoding.py"],
    parser=LanguageParser(language=Language.PYTHON, parser_threshold=200),
)
documents = loader.load()
print(len(documents))

document_dicts = []
for document in documents:
    parsed_dict = {}
    parsed_dict['source_filename'] = document.metadata['source']
    parsed_dict['programming_language'] = document.metadata['language'].value
    parsed_dict['source_file_contents'] = document.page_content
    document_dicts.append(parsed_dict)
    
total_size = sum(sum(len(str(value)) for value in dict_.values()) for dict_ in document_dicts)
print(f"Total size of all documents: {total_size}")
    
code_as_json = json.dumps(document_dicts)

with open('output.json', 'w') as f:
    f.write(code_as_json)
f.close()

# print(code_as_json)

# for doc in documents:
#     print(doc.page_content)