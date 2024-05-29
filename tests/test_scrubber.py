from models.modified_scrub import ScrubDub
from models.flagger import TextFlagging

scrubber = ScrubDub()
flagger = TextFlagging()

# Define test cases
def test_clean_text_removes_name():
    input_text = "My name is Rofiatu"
    expected_cleaned_text = "My name is [REDACTED]"
    scrubbed_text = scrubber.scrub(input_text)
    assert scrubbed_text == expected_cleaned_text

def test_clean_text_removes_email():
    input_text = "My email is john.doe@example.com"
    expected_cleaned_text = "My email is [REDACTED]"
    scrubbed_text = scrubber.scrub(input_text)
    assert scrubbed_text == expected_cleaned_text

def test_clean_text_removes_phone_number():
    input_text = "My phone number is 555-555-5555"
    expected_cleaned_text = "My phone number is [REDACTED]"
    scrubbed_text = scrubber.scrub(input_text)
    assert scrubbed_text == expected_cleaned_text

def test_flag_text_with_keywords():
    input_text = "I live in a big city and earn a good salary."

    expected_keywords = ["live", "earn", "money"]
    expected_portions = []

    # Iterate over expected keywords
    for keyword in expected_keywords:
        # Check if keyword is present in the input text
        if keyword in input_text:
            # If keyword is present, add the corresponding portion to the expected portions list
            expected_portions.append(input_text)

    flagged_portions = flagger.flag_text_with_keywords(input_text)

    # Print debug information
    print("Flagged portions:", flagged_portions)
    print("Expected portions:", expected_portions)

    # Assert that flagged portions match expected portions
    assert flagged_portions == expected_portions

def test_clean_text_does_not_modify_non_pii_text():
    input_text = "This is a test without any PII."
    expected_cleaned_text = "This is a test without any PII."
    scrubbed_text = scrubber.scrub(input_text)
    assert scrubbed_text == expected_cleaned_text

def test_clean_text_handles_empty_string_input():
    input_text = ""
    expected_cleaned_text = ""
    scrubbed_text = scrubber.scrub(input_text)
    assert scrubbed_text == expected_cleaned_text

# Run the tests
if __name__ == "__main__":
    import pytest
    pytest.main()

