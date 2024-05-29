import spacy

class TextFlagging:
    def __init__(self):
        # Load spaCy English language model
        self.nlp = spacy.load("en_core_web_sm")

        # Define target words and their synonyms
        self.target_words = {
            "live": {"reside", "dwell", "inhabit"},
            "earn": {"make", "receive", "gain"},
            "money": {"wealth", "income", "currency"}
        }

    def flag_text_with_keywords(self, text: str) -> list:
        """
        Flag portions of text containing specific keywords and their synonyms.
        
        Args:
        - text (str): The input text to analyze.
        
        Returns:
        - flagged_portions (list): A list of portions of text containing the flagged keywords.
        """
        # Process the text with spaCy
        doc = self.nlp(text)

        # Extract flagged portions of text
        flagged_portions = []
        for token in doc:
            if token.pos_ == "VERB":
                lemma = token.lemma_
                if lemma in self.target_words:
                    flagged_portions.append(token.sent.text)

        return flagged_portions