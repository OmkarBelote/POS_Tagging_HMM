def preprocess_conllu(input_file, output_file):
    """
    Preprocesses a CoNLL-U formatted file into word_tag format.
    """
    with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
        sentence = []
        for line in infile:
            line = line.strip()
            if not line or line.startswith("#"):
                if sentence:
                    outfile.write(" ".join(sentence) + "\n")
                sentence = []
                continue
            parts = line.split("\t")
            if len(parts) > 3:
                word = parts[1]
                tag = parts[3]
                sentence.append(f"{word}_{tag}")
        if sentence:
            outfile.write(" ".join(sentence) + "\n")

if __name__ == "__main__":
    input_path = r"C:\Users\omkar_zu2lrhd\OneDrive\Desktop\Projects\POS_Tagging_HMM\data\en_ewt-ud-train.conllu"
    output_path = r"C:\Users\omkar_zu2lrhd\OneDrive\Desktop\Projects\POS_Tagging_HMM\data\corpus.txt"
    preprocess_conllu(input_path, output_path)
    print(f"Preprocessing complete. Output saved to {output_path}.")
