import os
from src.mcqgenerator.logger import logging
from langchain.prompts import PromptTemplate
from langchain_community.llms import Ollama
from langchain.chains import LLMChain
from langchain.chains.sequential import SequentialChain


logging.info("starting the mcqapp before loading")


llm = Ollama(
    model="llama3")
logging.info("Ollama Model llama3 has been defined ")


template1="""
Text:{text}
You are an expert MCQ maker.Given the above text,it is your job to \
create a quiz of {number} multiple choice questions for {subject} students in {tone} tone.
Make sure the questions are not repeated and check all the questions to be conforming he text as well.
make sure to format your response like RESPONSE_JSON below and use it as a guide.\
Ensure to make {number} MCQs.
###Response Json
{response_json}    """

logging.info("main template is defined")


quiz_generation_prompt=PromptTemplate(input_variables=['text','number','subject','tone','response_json'],template=template1)
logging.info('quiz generation_prompt object of PromptTemplate class is created')

chain1=LLMChain(llm=llm,prompt=quiz_generation_prompt,output_key='quiz',verbose=True)
logging.info("chain 1 consist of llm ,quiz generaion prompt is defined ")


template2="""
You are an expert english grammarian and writer .Given a multiple choice Quiz for {subject} students.\
You need to evaluate the complexity of the question and give a complete analysis of the quiz.Only use at max 50 words for complexity.
if the quiz is not at per with the cognitive and analytical abilities of the students ,\
update the quiz questions which needs to be changed  and change the tone such that it perfectly fits the student abilities
Quiz_MCQs:
{quiz}
check from an expert Engish Writer of the above quiz """
logging.info("template2 is defined")


quiz_evaluation_prompt=PromptTemplate(input_variables=['subject','quiz'],template=template2)
logging.info("quiz evaluation prompt is created")


chain2=LLMChain(llm=llm,prompt=quiz_evaluation_prompt,output_key='review',verbose=True)
logging.info('chain2 with llm and quiz evaluation prompt is created')

generate_evaluate_chain=SequentialChain(chains=[chain1,chain2],input_variables=['text','number','subject','tone','response_json'],output_variables=['quiz','review'],verbose=True)
logging.info('the sequential chain object is defined')
