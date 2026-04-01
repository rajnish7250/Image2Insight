from src.ocr.ocr_engine import extract_text
from src.preprocessing.clean_text import clean_text
from src.preprocessing.remove_stopwords import remove_stopwords
from src.nlp.sentiment import analyze_sentiment

def main():
    image_path = "data/input_images/test5.png"

    print("🔍 Extracting text from image...")
    text = extract_text(image_path)

    if not text.strip():
        print("No text extracted. Check Tesseract or image.")
        return
    print("\nRaw Text:\n", text)

    cleaned = clean_text(text)
    filtered = remove_stopwords(cleaned)

    print("\nProcessed Text:\n", filtered)

    result = analyze_sentiment(filtered)

    print("\n📊 Sentiment Result:")
    print(result)

if __name__ == "__main__":
    main()