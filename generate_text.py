#save it as a txt file


#available models
#https://huggingface.co/models?pipeline_tag=text-generation
generator = pipeline('text-generation', model = 'gpt2')
prompt = "The animal penguins are motivational because"
text_results = generator(prompt, max_length = 70, temperature=0.9,
    do_sample=True, top_k=50)
print(text_results[0]['generated_text'])