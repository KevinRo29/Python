import re
from collections import Counter

def analyze_text(text):
    # Counting words
    words = text.split()
    word_count = len(words)

    # Counting sentences
    sentences = re.split(r'[.!?]', text)
    sentence_count = len([s for s in sentences if s.strip()])

    # Counting paragraphs
    paragraphs = text.split('\n\n')
    paragraph_count = len(paragraphs)

    # Calculating keyword frequency
    keywords = ['the', 'be', 'to', 'of', 'and', 'a', 'in', 'that', 'have', 'I', 'it', 'for', 'not', 'on', 'with', 'he']
    keyword_counts = Counter() # initialize a counter object
    for keyword in keywords:
        keyword_counts[keyword] = text.lower().count(keyword.lower()) # case insensitive

    return {
        'word_count': word_count,
        'sentence_count': sentence_count,
        'paragraph_count': paragraph_count,
        'keyword_frequency': keyword_counts
    }

def main():
    input_text = input("Enter the text to analyze:\n")
    analysis_result = analyze_text(input_text)

    print("\nText Analysis Results:")
    print(f"Word Count: {analysis_result['word_count']}")
    print(f"Sentence Count: {analysis_result['sentence_count']}")
    print(f"Paragraph Count: {analysis_result['paragraph_count']}")
    print("Keyword Frequency:")
    for keyword, count in analysis_result['keyword_frequency'].items():
        print(f"{keyword}: {count}")

if __name__ == "__main__":
    main()
