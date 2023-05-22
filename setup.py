from setuptools import setup

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='seabornai',
    version='0.0.2',
    packages=['seabornai'],
    install_requires=[
        'openai',
        'seaborn',
    ],
    author="Tripathi Aditya Prakash",                     # Full name of the author
    description="seabornai is a Python library that leverages the OpenAI ChatGPT API to generate Seaborn graphs based on supplied data and prompts/questions.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/aditya0072001/seabornai',
        classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],                                      # Information to filter the project on PyPi website
    python_requires='>=3.6',                # Minimum version requirement of the package
    project_urls={
        'Download Statistics': 'https://pepy.tech/project/seabornai/month',
    },
)
