def repair_mojibake_robust(input_file, output_file):
    try:
        # Read the file using ISO-8859-1, which maps every byte to a character.
        # This prevents the initial read from failing.
        with open(input_file, 'r', encoding='iso-8859-1') as f:
            content = f.read()

        # Step 1: Convert string to bytes using ISO-8859-1 (reconstructs the raw bytes)
        raw_bytes = content.encode('iso-8859-1')

        # Step 2: Decode as UTF-8, but use 'replace' for any bytes that don't fit 
        # the UTF-8 pattern. This ensures the script doesn't crash.
        fixed_content = raw_bytes.decode('utf-8', errors='replace')

        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(fixed_content)
            
        print(f"Repaired file saved as: {output_file}")
        
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the updated function
repair_mojibake_robust('SingleLettersRemoved.txt', 'Fixed_UTF8_Letters.txt')