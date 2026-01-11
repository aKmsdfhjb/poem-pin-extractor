def pin_extractor(poems):
    secret_codes = []
    for poem in poems:
        secret_code = ''
        lines = poem.split('\n')
        for line_index, line in enumerate(lines):
            words = line.split()
            if len(words) > line_index:
                secret_code += str(len(words[line_index]))
            else:
                secret_code += '0'
        secret_codes.append(secret_code)
    return secret_codes

def main():
    user_inputs = []
    print("--- Text-to-PIN Generator ---")
    
    while True:
        print("\nEnter your text/poem (use '\\n' for new lines):")
        text_input = input("> ")
        formatted_text = text_input.replace('\\n', '\n')
        user_inputs.append(formatted_text)
        
        choice = input("Add another entry? (y/n): ").lower()
        if choice != 'y':
            break

    results = pin_extractor(user_inputs)
    print("\nGenerated Codes:", results)

if __name__ == "__main__":
    main()
