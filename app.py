
# app.py
from flask import Flask, request, jsonify
from flask_cors import CORS
from image_analysis import read_image, get_hash_similarity, get_structural_similarity, detect_editing_artifacts

app = Flask(_name_)
CORS(app)

@app.route('/analyze', methods=['POST'])
def analyze_images():
    if 'image1' not in request.files or request.files['image1'].filename == '':
        return jsonify({'error': 'Imagem 1 não foi enviada corretamente'}), 400

    if 'image2' not in request.files or request.files['image2'].filename == '':
        return jsonify({'error': 'Imagem 2 não foi enviada corretamente'}), 400

    img1 = read_image(request.files['image1'])
    img2 = read_image(request.files['image2'])

    hash_sim = get_hash_similarity(img1, img2)
    ssim_val = get_structural_similarity(img1, img2)
    edit1, prob1 = detect_editing_artifacts(img1)
    edit2, prob2 = detect_editing_artifacts(img2)

    response = {
        "hash_similarity": round(hash_sim, 2),
        "structural_similarity": round(ssim_val, 2),
        "possible_edits": {
            "image1": {"edited": edit1, "confidence": prob1},
            "image2": {"edited": edit2, "confidence": prob2}
        },
        "conclusion": "Semelhança alta" if hash_sim > 85 and ssim_val > 80 else "Diferença significativa detectada"
    }

    return jsonify(response)

if _name_ == '_main_':
    app.run(debug=True, host='0.0.0.0', port=8000)