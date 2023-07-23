from langchain.llms import OpenAI
from langchain import PromptTemplate, LLMChain

template = """
Description: {description}

I will give an easy description for description an object in image, rephrase the description into keywords as you are trying to buy the object on internet.
Please try to limit the object into single item and be specific, also ignore the information of environment.
Then translate the keyword into Traditional Chinese.

Translated_keyword:
"""



class KeywordGenerator:
    def __init__(self, key:str):
        self.llm = OpenAI(openai_api_key=key)
        self.prompt = PromptTemplate(template=template, input_variables=["description"])
        self.llm_chain = LLMChain(prompt=self.prompt, llm=self.llm)
        
    def generate(self, caption):
        return self.llm_chain.run(caption)