from langchain_community.llms import Ollama

def chat(question: str):
  llm = Ollama(model="llama3:8b")
  # return llm.invoke(question)

  result = ""
  response = llm.stream(question)
  print(response)
  for res in response:
    print(res, end="")
    result += res

  return result