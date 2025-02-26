from sentence_transformers import SentenceTransformer,util
import warnings,math

def accuracy(ref_answer,answer):
    #Ignore all warnings
    warnings.filterwarnings('ignore')
    #Get Similarity from model
    similarity = A2A(ref_answer,answer)
    final_similarity = (1 - 1 / math.exp(3*similarity))*100
    if final_similarity < 0:
        final_similarity = 0 

    return final_similarity


model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
def A2A(ref_ans,ans):
    #Importing pre-trained model from hugging face
    
    
    #Converting reference answer to 384 dimensions vectors
    ref_embedding = model.encode(ref_ans, convert_to_tensor=True)
    ans_embedding = model.encode(ans, convert_to_tensor=True)
    ans_similarity = float(util.pytorch_cos_sim(ref_embedding, ans_embedding))

    return ans_similarity