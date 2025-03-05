import re
import streamlit as st
from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline

st.header('Query Solver')

st.markdown("""
### About the Model  
This app uses **TinyLlama-1.1B-Chat**, a compact **Llama-based** model fine-tuned for chat applications.  
It retains the **same architecture and tokenizer as Llama 2**, making it efficient for low-compute environments.  
The model is fine-tuned using the **UltraChat** dataset (ChatGPT-generated dialogues) and the **UltraFeedback** dataset (GPT-4-ranked responses).  
With **only 1.1B parameters**, it delivers quality responses while being lightweight.  

🔗 [TinyLlama GitHub](https://github.com/jzhang38/TinyLlama)
""")

history = []
close = ['quit', 'q', 'exit', 'x', 'bye']

llm = HuggingFacePipeline.from_model_id(  
    model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    pipeline_kwargs=dict(
        max_new_tokens = 512
    )
)

model = ChatHuggingFace(llm=llm)

prompt = st.text_input("Enter your question")
history.append(prompt)

if st.button("Answer"):
    if prompt.lower() in close:
        st.write("Good Bye!!! Take care, ask question freely whenever needed.")

    result = model.invoke(prompt)
     # Extract answer after "<|assistant|>"
    match = re.search(r"<\|assistant\|>\s*(.*)", result.content, re.DOTALL)
    clean_answer = match.group(1).strip() if match else result.content
    history.append(clean_answer)
    
    st.write(clean_answer)

if st.button("Reset"):
    st.write("")

