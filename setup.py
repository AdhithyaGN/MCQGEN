from setuptools import setup,find_packages


setup(
    name='mcqgenrator',
    version='0.0.1',
    author='Adhithya G Nair',
    author_email='adhithyagnair97@gmail.com',
    install_requires=["openai","langchain","streamlit","python-dotenv","PyPDF2"],
    packages=find_packages()
)

  