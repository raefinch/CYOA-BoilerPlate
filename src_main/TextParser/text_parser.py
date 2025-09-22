import re
import yaml

def parse_text_to_structure(text):
    # Split text into parts using chapter headers as separators
    parts = re.split(r'(?m)^Chapter\s+\d+|[IVXLC]+\s*$', text)
    # Find chapter numbers to match sections extracted
    chapter_nums = re.findall(r'(?m)^Chapter\s+(\d+|[IVXLC]+)', text)
    
    story_structure = {}
    
    # Zip chapter numbers with content parts (skip the first part before first chapter)
    for chap_num, chap_content in zip(chapter_nums, parts[1:]):
        chapter_id = f"chapter_{chap_num}"
        
        # Extract narrative lines (all except numbered or bulleted choices)
        narrative_lines = []
        for line in chap_content.split('\n'):
            if not re.match(r"^(?:\d+\.\s*|[-*]\s+).*", line):
                narrative_lines.append(line.strip())
        narrative_text = "\n".join(narrative_lines).strip()
        
        # Extract choices using regex matching digits + dot or bullets
        
        choice_pattern = re.compile(r"^(?:\d+\.\s*|[-*]\s+)(.*?)(?:\s*\(([^)]+)\))?$", re.MULTILINE)

        choices_found = choice_pattern.findall(chap_content)

        choices = []
        for i, (option_text, next_node) in enumerate(choices_found, 1):
            next_id = next_node if next_node else f"{chapter_id}_choice{i}"
            choices.append({
                'option': option_text.strip(),
                'next': next_id.strip()
            })

        story_structure[chapter_id] = {
            'text': narrative_text,
            'choices': choices
        }
       
    return story_structure

def save_structure_as_yaml(structure, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        yaml.dump(structure, file, sort_keys=False, allow_unicode=True)

# Usage example
if __name__ == "__main__":
    with open('C:/Users/byrds/CYOA App/CYOA-Boilerplate/src_main/TextParser/text_files/TestText.txt', 'r', encoding='utf-8') as f:
        novel_text = f.read()
    story_data = parse_text_to_structure(novel_text)
    save_structure_as_yaml(story_data, 'yaml_files/TestText.yaml')
    print("YAML file created successfully.")
