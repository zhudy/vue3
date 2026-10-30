import asyncio
from langchain_deepseek import ChatDeepSeek
# from pydantic import SecretStr
from langchain.agents import create_agent
# from agent_schema import NameSchema, NameResultSchema

llm = ChatDeepSeek(
    model = "deepseek-chat",
    # DEEPSEEK_API_KEY = SecretStr("sk-634a417d3be949b990e27d5037940cc7"),
    api_key = "sk-634a417d3be949b990e27d5037940cc7",
    temperature = 0.8
)

systemprompt = """
你是一个相声演员
"""

# responseFormat = 
agent = create_agent(
    model=llm, 
    system_prompt=systemprompt,
    # response_format=NameResultSchema
)

async def generate_names():
    prompt = f"请写一个关于共享单车的小笑话"
    result = await agent.ainvoke({
        "messages": [{"role": "user", "content": prompt}]
    })
    print(result)


if __name__ == "__main__":
    asyncio.run(generate_names())