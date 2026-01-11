Poem PIN Extractor

📖 Description

The Poem PIN Extractor is a Python-based utility that generates unique numerical security codes (PINs) from strings of text or poetry. This tool analyzes the structure of a poem—specifically word lengths at increasing line indices—to create a distinct digital signature.

How it Works

The tool processes text line-by-line following a diagonal extraction logic:

Line 1 (Index 0): Measures the length of the 1st word.

Line 2 (Index 1): Measures the length of the 2nd word.

Line 3 (Index 2): Measures the length of the 3rd word, and so on.

If a line does not have enough words to match the required index, it defaults to 0. This creates a consistent, reproducible PIN for any given text.

🚀 Features

Dynamic Input: Allows users to input multiple text blocks in one session.

Error Handling: Built-in support for short lines or empty inputs using 0 placeholders.

Clean Formatting: Outputs results as a list of strings for easy data processing.

🛠️ Usage

1. Clone the repository

git clone [https://github.com/aKmsdfhjb/poem-pin-extractor.git](https://github.com/aKmsdfhjb/poem-pin-extractor.git)


2. Run the generator

python pin_extractor.py


3. Logic Example

Input Text:

"The sky is blue"

"Birds fly high"

"Nature is quite beautiful"

Extraction:

Line 0, Word 0: "The" (Length 3)

Line 1, Word 1: "fly" (Length 3)

Line 2, Word 2: "quite" (Length 5)

Resulting PIN: 335

🧪 Function Signature

def pin_extractor(poems):
    """
    Args:
        poems (list): List of multi-line strings.
    Returns:
        list: List of numerical strings.
    """


📄 License

MIT License

Copyright (c) 2026 aKmsdfhjb

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
