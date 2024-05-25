from git import Repo

from langchain_community.document_loaders.generic import GenericLoader
from langchain_community.document_loaders.parsers import LanguageParser
from langchain_text_splitters import Language

from langchain.tools import tool

from crewai_tools import BaseTool

import os
import json

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
        
        return code_as_json
            
