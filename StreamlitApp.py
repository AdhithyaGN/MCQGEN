import os
import streamlit as st
from src.mcqgnereator.utils import file_reader
from src.mcqgnereator.mcqapp import generate_evaluate_chain
import traceback
import json
from src.mcqgnereator.logger import logging

with open("C:/Users/S K E F/Desktop/GenAI/projects/MCQGEN/Response.json",'r') as file:
    RESPONSE_JSON=json.load(file)

logging.INFO('response_json has fetched succesfully')

st.title('MCQ Generator App with LangChain')

with st.form('user_inputs'):
    upload_file=st.file_uploader('Upload a file :Pdf/txt file')

    mcq_count=st.number_input('No: of MCQs',min_value=3,max_value=50)

    subject=st.text_input('Insert Subject',max_chars=20)

    tone=st.text_input('Complexity level of Questions',max_chars=20,placeholder='Simple')

    button=st.form_submit_button('Create MCQs')

logging.INFO('streamlit form has defined')

if button and upload_file is not None and mcq_count and subject and tone :

    with st.spinner('loading'):
        try:
            text=file_reader(upload_file)
            response=generate_evaluate_chain({

            
                'text':text,
                'number':mcq_count,
                'subject':subject,
                'tone':tone,
                'response_json':json.dumps(RESPONSE_JSON) 
                }


            )
        except Exception as e:
            traceback.print_exception(type(e),e,e.__traceback__)


        else:
            quiz=response['quiz']

            if quiz is not None:
                st.write(quiz)

                st.text_area(level='Review',value=response['review'])
            else:
                st.error('Error in Response')


