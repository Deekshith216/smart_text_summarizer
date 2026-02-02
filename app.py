from summarizer.openai_summarizer import OpenAISummarizer

def main():
    text = input("Enter text to summarize:\n")
    summary_type = input("Summary type (short / bullets / key-points): ")

    summarizer = OpenAISummarizer()
    summary = summarizer.summarize(text, summary_type)

    print("\n--- SUMMARY ---")
    print(summary)

if __name__ == "__main__":
    main()
