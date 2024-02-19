def clean_and_format_data(input_filepath, final_output_filepath):
    start_storing = False
    lineformats = []
    try:
        with open(input_filepath, 'r') as file:
            for line in file:
                if 'iso3' in line and 'year' in line and not start_storing:
                    start_storing = True
                    lineformat = process_line(line, is_header=True)
                    lineformats.append(lineformat + '\n')
                    continue
                if start_storing:
                    if '"' in line:
                        break
                    if line.strip() == "":
                        continue
                    lineformat = process_line(line)
                    lineformats.append(lineformat + '\n')
        with open(final_output_filepath, 'w') as file:
            file.writelines(lineformats)
    except Exception as e:
        print(f"An error occurred: {e}")
def process_line(line, is_header=False):
    if is_header:
        return ','.join(line.strip().split())
    parts = line.strip().split()
    if not parts:
        return ""
    excluded_words = ["and", "the", "of)", "New", "Nam"]
    lineformat = parts[0]
    triggerfound = False
    for part in parts[1:]:
        if len(part) == 3 and not triggerfound and part not in excluded_words:
            triggerfound = True
            lineformat += ',' + part
        elif triggerfound:
            lineformat += ',' + part
        else:
            lineformat += ' ' + part
    return lineformat
input_filepath = "./data/WHO_COVID_Excess_Deaths_EstimatesByCountry.txt"
final_output_filepath = "./data/clean_data.csv"
clean_and_format_data(input_filepath, final_output_filepath)
