import re
import yaml

def parse_text_to_structure(text):
    # Regex to capture chapters (e.g., "Chapter 1", "CHAPTER I")
    chapter_pattern = re.compile(r"(?ms)^Chapter\s+(\d+|[IVXLC]+)\s*$([\s\S]*?)(?=^Chapter\s+(\d+|[IVXLC]+)\s*$|$)")

    story_structure = {}

    for chap_num, chap_content in chapter_pattern.findall(text):
        chapter_id = f"chapter_{chap_num}"

        # Extract choices within chapter (numbered or bullet choices)
        choice_pattern = re.compile(r"^(?:\d+|[-*])\s+(.*)", re.MULTILINE)
        choices_found = choice_pattern.findall(chap_content)

        # Extract narrative by removing choice lines
        narrative_lines = []
        for line in chap_content.split('\n'):
            if not re.match(r"^(?:\d+|[-*])\s+.*", line):
                narrative_lines.append(line.strip())
        narrative_text = "\n".join(narrative_lines).strip()

        # Build choices with placeholder outcome IDs
        choices = []
        for i, choice_text in enumerate(choices_found, 1):
            choices.append({
                'option': choice_text,
                'next': f"{chapter_id}_choice{i}"  # placeholder outcome ID
            })

        # Store chapter data
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
    with open('novel.txt', 'r', encoding='utf-8') as f:
        novel_text = f.read()
    story_data = parse_text_to_structure(novel_text)
    save_structure_as_yaml(story_data, 'story.yaml')
    print("YAML file created successfully.")
