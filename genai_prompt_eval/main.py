def evaluate_prompt_response(prompt, response):
    # Simulate evaluation based on dummy rubrics
    print(f"Prompt: {prompt}")
    print(f"Response: {response}")
    print("Evaluation: ✅ Instruction Followed, ✅ Relevance, ✅ Tone")

if __name__ == "__main__":
    prompt = "Explain the greenhouse effect to a 10-year-old."
    response = "The greenhouse effect is like a blanket around the Earth..."
    evaluate_prompt_response(prompt, response)
