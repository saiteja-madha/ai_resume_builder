from setuptools import setup, find_packages

setup(
    name='lib_resume_builder_AIHawk',
    version='0.1',
    description='A package to generate AI-assisted resumes using GPT models',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='feder-cr',
    author_email='federico.elia.majo@gmail.com',
    url='https://github.com/feder-cr/lib_resume_builder_AIHawk',
    packages=find_packages(),
    install_requires=[ 
        'langchain',
        'langchain-anthropic',
        'langchain-community',
        'langchain-core',
        'langchain-google-genai',
        'langchain-huggingface',
        'langchain-ollama',
        'langchain-openai',
        'langchain-text-splitters',
        'langsmith',
        'openai',
        'pydantic',
        'pydantic[email]',
        'regex',
        'selenium',
        'webdriver-manager',
        'inquirer',
        'faiss-cpu',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.9',  
    include_package_data=True,  # Include altri file indicati nel MANIFEST.in
)
