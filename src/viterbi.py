def viterbi(sentence, hmm):
    words = sentence.split()
    n = len(words)
    tags = list(hmm.tags)

    dp = [{} for _ in range(n)]
    backpointer = [{} for _ in range(n)]

    # Initialization step
    for tag in tags:
        dp[0][tag] = hmm.get_emission_prob(words[0], tag) * hmm.transition_probs.get(('<s>', tag), 0.01)
        backpointer[0][tag] = None

    # Recursion step
    for i in range(1, n):
        for curr_tag in tags:
            max_prob, best_prev_tag = max(
                (
                    dp[i - 1][prev_tag] * hmm.transition_probs.get((prev_tag, curr_tag), 0.01) *
                    hmm.get_emission_prob(words[i], curr_tag),
                    prev_tag,
                )
                for prev_tag in tags
            )
            dp[i][curr_tag] = max_prob
            backpointer[i][curr_tag] = best_prev_tag

    # Termination step
    best_final_prob, best_final_tag = max((dp[n - 1][tag], tag) for tag in tags)

    # Backtrace to find the best sequence of tags
    best_tags = [best_final_tag]
    for i in range(n - 1, 0, -1):
        best_tags.insert(0, backpointer[i][best_tags[0]])

    return list(zip(words, best_tags))
