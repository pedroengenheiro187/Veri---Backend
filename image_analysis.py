
from PIL import Image
import imagehash
from skimage.metrics import structural_similarity as ssim
import numpy as np
import io

# Função para ler a imagem a partir do arquivo enviado
def read_image(file_storage):
    image = Image.open(file_storage).convert('RGB')
    return image

# Função de similaridade de hash perceptual (pHash)
def get_hash_similarity(img1, img2):
    hash1 = imagehash.phash(img1)
    hash2 = imagehash.phash(img2)
    # Quanto menor a diferença, mais parecidas são
    similarity = (1 - (hash1 - hash2) / len(hash1.hash) ** 2) * 100
    return similarity

# Função de similaridade estrutural (SSIM)
def get_structural_similarity(img1, img2):
    img1_resized = img1.resize((256, 256))
    img2_resized = img2.resize((256, 256))
    img1_gray = np.array(img1_resized.convert('L'))
    img2_gray = np.array(img2_resized.convert('L'))
    score, _ = ssim(img1_gray, img2_gray, full=True)
    similarity = score * 100
    return similarity

# Função "fake" de detecção de edição (só placeholder para manter o contrato da API)
def detect_editing_artifacts(image):
    # Como placeholder, vamos sempre retornar que não há edição
    return False, 0.0