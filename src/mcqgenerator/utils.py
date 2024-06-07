import os
from src.mcqgenerator.logger import logging
from pypdf import PdfReader
from langchain_community.document_loaders import PyPDFLoader,TextLoader

def file_reader(file):
    """
    This function is utilising the langchain document loader support to load the documents

    return the document as a Document as of the output of documentloaders in langchain
    """
    logging.info('the file reader function is initiated')

    if file.name.endswith('.pdf'):
        try:
            pdfreader=PdfReader(file)
            text=""
            for page in pdfreader.pages:
                text+=page.extract_text()
            return text
            logging.info('Pdf file read succesfully')
        except Exception as e:
            raise Exception('pdf file is not read succesfully')
    elif file.name.endswith('.txt'):
        return file.read().decode('utf-8')
        logging.info('text file read succesfully')
        
    else:
        raise Exception("Unsupported file type ,Only Pdf or txt file is supported")

    

        
