from git import Repo

from langchain_community.document_loaders.generic import GenericLoader
from langchain_community.document_loaders.parsers import LanguageParser
from langchain_text_splitters import Language

from langchain.tools import tool

from crewai_tools import BaseTool

import os

class GitRepoFetchTools(BaseTool):
    name: str =  "Git Repo Fetcher Tool"
    description: str = "Useful to retrieve the content of a git repository."
    
    def _run(self, repository_url: str) -> str:
   
        print(f"Fetching the repository content for URL {repository_url}...")

        # Clone
        repo_path = "./remote_repo"
        if not os.path.exists(repo_path):
            repo = Repo.clone_from(repository_url, to_path=repo_path)
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
        # print(len(documents))
        
        source_code = ""

        for doc in documents:
            source_code += doc.page_content + "\n"
        #     print(doc.page_content)
        
        return source_code
        
