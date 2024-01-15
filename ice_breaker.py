from langchain.prompts import PromptTemplate
from langchain_community.chat_models import ChatOpenAI
from langchain.chains import LLMChain

if __name__ == "__main__":
    print("Hello LangChain")

    information = """ 
Yann André LeCun[1] (/ləˈkʌn/ lə-KUN, French: [ləkœ̃];[2] originally spelled Le Cun;[2] born 8 July 1960) is a Turing Award winning French computer scientist working primarily in the fields of machine learning, computer vision, mobile robotics and computational neuroscience. He is the Silver Professor of the Courant Institute of Mathematical Sciences at New York University and Vice-President, Chief AI Scientist at Meta.[3][4]
He is well known for his work on optical character recognition and computer vision using convolutional neural networks (CNN), and is a founding father of convolutional nets.[5][6] He is also one of the main creators of the DjVu image compression technology (together with Léon Bottou and Patrick Haffner). He co-developed the Lush programming language with Léon Bottou.
LeCun received the 2018 Turing Award (often referred to as the "Nobel Prize of Computing"), together with Yoshua Bengio and Geoffrey Hinton, for their work on deep learning.[7] The three are sometimes referred to as the "Godfathers of AI" and "Godfathers of Deep Learning"
    """

    summary_template = """ 
    given the information {information} about a person, 
    I would like you to please create:
        1. a short summary
        2. two interesting facts about that person.
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )

    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

    chain = LLMChain(llm=llm, prompt=summary_prompt_template)

    print(chain.run(information=information))
