def read_icms_file(file_path):
    try:
        with open(file_path, 'r') as file:
            data = file.read()
        return data
    except Exception as e:
        print(f"Error reading file: {e}")
        return None

def convert_icms_to_text(icms_data):
    lines = icms_data.split('\n')
    text_output = ""
    for line in lines:
        if line.strip():
            text_output += f"{line}\n"
    return text_output

def convert(file_path):
    icms_data = read_icms_file(file_path)
    if icms_data:
        text_output = convert_icms_to_text(icms_data)
        print("Converted Output:\n")
        print(text_output)


file_path = 'test01.icms' # replace the file name chosen here
convert(file_path)
