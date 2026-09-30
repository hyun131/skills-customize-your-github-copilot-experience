positive_words = ["happy", "great", "love", "excellent", "fun"]
negative_words = ["sad", "bad", "hate", "awful", "boring"]


def count_sentiment_words(sentence):
    """Return the number of positive and negative words in a sentence."""
    words = sentence.lower().split()
    positive_count = 0
    negative_count = 0

    # TODO: Count matching words from each list.
    return positive_count, negative_count


def classify_sentence(sentence):
    """Return 'positive', 'negative', or 'neutral' for a sentence."""
    positive_count, negative_count = count_sentiment_words(sentence)

    # TODO: Compare the counts and return a label.
    return "neutral"


def main():
    while True:
        sentence = input("Enter a sentence (or 'quit' to stop): ")
        if sentence.lower() == "quit":
            break

        print(classify_sentence(sentence))


if __name__ == "__main__":
    main()