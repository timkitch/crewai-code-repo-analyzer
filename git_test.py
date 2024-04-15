from git import Repo

from langchain_community.document_loaders.generic import GenericLoader
from langchain_community.document_loaders.parsers import LanguageParser
from langchain_text_splitters import Language

import os

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

# for doc in documents:
#     print(doc.page_content)