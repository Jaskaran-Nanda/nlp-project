import SemanticSimilarity

def grader(question,answer,answers):
    semantic_sim = SemanticSimilarity.SemanticSimilarity(question,answer,answers)
    return semantic_sim




#Testset

'''question = "How many models can I host on HuggingFace?"
answer_1 = "All plans come with unlimited private models and datasets."
answer_2 = "AutoNLP is an automatic way to train and deploy state-of-the-art NLP models, seamlessly integrated with the Hugging Face ecosystem."
answer_3 = "Based on how much training data and model variants are created, we send you a compute cost and payment link - as low as $10 per job."
grader(question,"infinte",[answer_1,answer_2,answer_3])'''