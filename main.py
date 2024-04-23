# Python Proofreading from freeCodeCamp
# pip install lmproof
import lmproof

# Function to check the text, returning a correction
def proofread(text):
    proofread = lmproof.load("en")
    correction = proofread.proofread(text)
    print("Original: {}".format(text))
    print("Correction: {}".format(correction))

# Run proofread function
proofread("Your Text")