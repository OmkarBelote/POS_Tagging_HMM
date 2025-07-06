from flask import Flask, request, render_template, jsonify
from hmm import HMM
from viterbi import viterbi

app = Flask(__name__)

# Use raw string to fix path issue
corpus_path = r"C:\Users\omkar_zu2lrhd\OneDrive\Desktop\Projects\POS_Tagging_HMM\data\corpus.txt"
hmm_model = HMM(corpus_path)

@app.route('/', methods=['GET', 'POST'])
def index():
    tagged_sentence = ""
    return render_template('index.html', tagged_sentence=tagged_sentence)

# Add a JSON API endpoint for AJAX requests
@app.route('/api/tag', methods=['POST'])
def api_tag():
    data = request.json
    sentence = data.get('sentence', '')
    
    tagged = viterbi(sentence.lower(), hmm_model)
    
    # Format the result for the frontend
    result = [{"word": word, "tag": tag} for word, tag in tagged]
    
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
