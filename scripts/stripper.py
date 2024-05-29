from models.modified_scrub import ScrubDub
        
# scrubber = Scrub()
scrubber = ScrubDub()

# Read the contents of the .txt file into a string variable
with open("_.txt", "r") as file:
    input_text = file.read()

# Call the scrub() method with the input text
scrubbed_text = scrubber.scrub(input_text)

# Save the output in a new file
with open("stripped_chat.txt", "w") as output_file:
    output_file.write(scrubbed_text)
