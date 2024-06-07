import os
from src.mcqgnereator.logger import logging
from langchain_community.document_loaders import PyPDFLoader,TextLoader

def file_reader(file):
    """
    This function is utilising the langchain document loader support to load the documents

    return the document as a Document as of the output of documentloaders in langchain
    """
    logging.INFO('the file reader function is initiated')

    if file.name.endswith('.pdf'):
        try:
            doc=PyPDFLoader(file)
            document=doc.load()

            return document
        except Exception as e:
            raise Exception('error reading the pdf file')

    elif file.name.endswith('.txt'):
        try:
            text=TextLoader(file)
            textdoc=text.load()

            return textdoc
        
        except Exception as e:
            raise Exception('error reading the text file')
        
    else:
        raise Exception('Unsupported file type ,Only PDF and txt file supported')
    
    
        
