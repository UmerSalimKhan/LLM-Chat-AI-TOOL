import re
from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline

history = []
close = ['quit', 'q', 'exit', 'x', 'bye']

llm = HuggingFacePipeline.from_model_id(  
    model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    pipeline_kwargs=dict(
        max_new_tokens = 100
    )
)

model = ChatHuggingFace(llm=llm)

while True:
    prompt = input("User: ")
    history.append(prompt)

    if prompt.lower() in close:
        break 

    result = model.invoke(prompt)

    # Extract answer after "<|assistant|>"
    match = re.search(r"<\|assistant\|>\s*(.*)", result.content, re.DOTALL)
    clean_answer = match.group(1).strip() if match else result.content
    history.append(clean_answer)

    print("AI:", clean_answer, "\n")  # Only print the relevant part
    
print(f"Chat History: {history}")