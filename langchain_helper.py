from langchain.prompts import PromptTemplate
from langchain.chains import SequentialChain

from langchain.chains import LLMChain
from langchain_community.llms.openai import OpenAI
import environment_keys as env
import os

os.environ["OPEN_API_KEY"] = "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"

llm = OpenAI(temperature=0.6, openai_api_key="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")


def generate_restaurent_name_and_items(cuisine):
    prompt_template_resName = PromptTemplate(
        input_variables=["cuisine"],
        template="I want to open a restaurent for {cuisine} food.Can you suggest any fancy name for this."
    )
    name_chain = LLMChain(llm=llm, prompt=prompt_template_resName, output_key="restaurant_name")
    prompt_template_items = PromptTemplate(
        input_variables=["restaurant_name"],
        template="What are the items present at {restaurant_name}, return as comma seperated list"
    )
    item_chain = LLMChain(llm=llm, prompt=prompt_template_items, output_key="items")
    from langchain.chains import SequentialChain
    chain = SequentialChain(
        chains=[name_chain, item_chain],
        input_variables=['cuisine'],
        output_variables=['restaurant_name', 'items']
    )
    return chain({'cuisine': cuisine})


if __name__ == "__main__":
    print(generate_restaurent_name_and_items('Italian'))
