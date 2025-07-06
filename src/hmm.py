class HMM:
    def __init__(self, corpus_path):
        self.transition_probs = {}
        self.emission_probs = {}
        self.tags = set()
        self.words = set()
        self.tag_counts = {}
        self.train(corpus_path)

    def train(self, corpus_path):
        word_tag_counts = {}
        tag_bigram_counts = {}

        with open(corpus_path, 'r', encoding='utf-8') as file:
            for line in file:
                tokens = line.strip().split()
                prev_tag = None
                for token in tokens:
                    word, tag = token.rsplit('_', 1)
                    self.words.add(word)
                    self.tags.add(tag)

                    # Count tags and word-tag pairs
                    self.tag_counts[tag] = self.tag_counts.get(tag, 0) + 1
                    word_tag_counts[(word, tag)] = word_tag_counts.get((word, tag), 0) + 1

                    # Count tag bigrams
                    if prev_tag:
                        tag_bigram_counts[(prev_tag, tag)] = tag_bigram_counts.get((prev_tag, tag), 0) + 1
                    prev_tag = tag

        # Calculate probabilities with Laplace smoothing
        total_tags = sum(self.tag_counts.values())
        for t1 in self.tags:
            for t2 in self.tags:
                count = tag_bigram_counts.get((t1, t2), 0)
                self.transition_probs[(t1, t2)] = (count + 1) / (self.tag_counts[t1] + len(self.tags))

        for word in self.words:
            for tag in self.tags:
                count = word_tag_counts.get((word, tag), 0)
                self.emission_probs[(word, tag)] = (count + 1) / (self.tag_counts[tag] + len(self.words))

    def get_emission_prob(self, word, tag):
        if word not in self.words:  # Handle unseen words
            if word[0].isupper():  # Capitalized words are likely proper nouns
                return 1 if tag == 'PROPN' else 0
            return 1 / (self.tag_counts[tag] + len(self.words))  # Default smoothing
        return self.emission_probs.get((word, tag), 0)
