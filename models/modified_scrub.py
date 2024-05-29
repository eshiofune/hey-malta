from scrubadubdub import Scrub
import re

class ScrubDub(Scrub):
    def __init__(self):
        super().__init__()
        self.patterns.update(
            phone2= r"@(\+\d+|\d+)",
            phone3= r"\+?\d{1,3}\s?\(?\d{1,4}\)?[-\s]?\d{1,4}[-\s]?\d{1,4}"
        )

    def scrub_text(self, text: str) -> str:
        scrubbed_text = text
        for category, pattern in self.patterns.items():
            if category == "phone2" or category == "phone3":
                matches = re.finditer(pattern, scrubbed_text)
                for match in matches:
                    matched_phone = match.group(0)

                    # Remove parentheses from matched phone numbers
                    matched_phone = re.sub(r"^\((\d{3})\)$", r"\1", matched_phone)
                    scrubbed_text = scrubbed_text.replace(matched_phone, "[REDACTED]")
            else:
                scrubbed_text = re.sub(pattern, "[REDACTED]", scrubbed_text)
        
        scrubbed_text = self.scrub_pii_with_nlp(scrubbed_text)
        return scrubbed_text