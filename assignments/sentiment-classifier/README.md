# 📘 Assignment: Beginner Sentiment Classifier

## 🎯 Objective

Build a simple rule-based text classifier in Python that labels short sentences as positive, negative, or neutral. Practice string processing, lists, functions, conditionals, and loops while exploring how keyword-based classification works and where it can fail.

## 📝 Tasks

### 🛠️ Count Sentiment Words

#### Description
Create lists of positive and negative words, then count how many words from each list appear in a sentence. Treat words without regard to capitalization.

#### Requirements
Completed program should:

- Define lists of positive and negative words
- Define a function that takes a sentence and returns the positive and negative match counts
- Match words regardless of capitalization
- Avoid counting a word that is only part of a longer word


### 🛠️ Classify a Sentence

#### Description
Use the match counts to decide whether a sentence is positive, negative, or neutral. If both counts are equal, classify the sentence as neutral.

#### Requirements
Completed program should:

- Define a function that returns `"positive"`, `"negative"`, or `"neutral"`
- Return `"positive"` when the positive count is higher
- Return `"negative"` when the negative count is higher
- Return `"neutral"` when the counts are equal, including when neither list matches


### 🛠️ Try and Reflect

#### Description
Let a user enter several sentences and display each classification. Try sentences with mixed or unfamiliar wording and consider why a keyword-based classifier may get them wrong.

#### Requirements
Completed program should:

- Repeatedly ask for a sentence until the user enters `quit`
- Display the classification for each sentence
- Include at least three test sentences with different expected classifications
- Describe one limitation of using word lists to understand sentiment