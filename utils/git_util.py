from git import Repo
from langchain_community.document_loaders.generic import GenericLoader
from langchain_community.document_loaders.parsers import LanguageParser
import os
import re
import json

def clone_repo(remote_repo_url):
    repo_path = "./repos"
    if not os.path.exists(repo_path):
        os.makedirs(repo_path)
    
    """
    Clones a remote Git repository to a local path.
    
    Args:
        remote_repo_url (str): The URL of the remote Git repository to clone.
    
    Returns:
        str: The local path where the repository was cloned.
    """
    # Use a regular expression to extract the last part of the URL path
    match = re.search(r"([^/]+)\.git$", remote_repo_url)
    if match:
        repo_name = match.group(1)
    else:
        print("Could not extract repo name from URL")
        exit(1)
    
    local_repo_path = repo_path + "/" + repo_name
    
    # check if local_repo_path exists
    if os.path.exists(local_repo_path):
        print("Local repo path already exists. Not cloning.")
    else:
        print(f"Cloning repo {remote_repo_url} to {local_repo_path}...")
        Repo.clone_from(remote_repo_url, to_path=local_repo_path)
        
    return local_repo_path
        
def load_repo(repo_path):
    """
    Loads a repository from the file system and returns the documents.
    
    Args:
        repo_path (str): The path to the repository on the file system.
    
    Returns:
        List[Document]: A list of documents loaded from the repository.
    """
    loader = GenericLoader.from_filesystem(
        repo_path,
        glob="**/*",
        suffixes=[".java", ".py", ".go", ".c", ".cpp", ".h", ".cs", ".php", ".js"],
        # exclude=["**/non-utf8-encoding.py"],
        parser=LanguageParser(parser_threshold=500),
        # NOTE: the parser may perform better for certain languages if the language is specified.
        # parser=LanguageParser(language=Language.PYTHON, parser_threshold=500),
    )
    documents = loader.load()
    document_dicts = []
    for document in documents:
        parsed_dict = {}
        parsed_dict['source_filename'] = document.metadata['source']
        parsed_dict['programming_language'] = document.metadata['language']
        parsed_dict['source_file_contents'] = document.page_content
        document_dicts.append(parsed_dict)
        
    total_size = sum(sum(len(str(value)) for value in dict_.values()) for dict_ in document_dicts)
    print(f"Total size of all documents: {total_size}")
        
    code_as_json = json.dumps(document_dicts)
    
    return code_as_json
