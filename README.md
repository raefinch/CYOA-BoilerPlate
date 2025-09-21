# CYOA-Boilerplate
A boilerplate to help users easily create their own choose your own adventure app


### How To:
This application is designed to allow users to create and play interactive choose-your-own-adventure stories with ease. Follow these steps to get started:

Upload Your Story File
Upload a text file formatted according to the specified structure that defines story nodes, choices, and attribute impacts. This will be parsed into a tree structure for the app.

Set Main Character Attributes
Programmatically define your main character’s name and attributes such as health and mana. The attributes can be adjusted dynamically as story choices are made.

Navigate the Story
The app displays story text and presents choices at decision points. Selecting a choice updates the character’s attributes, progresses the story to the outcome node, and presents new choices.

Use Checkpoints
If the character fails or dies, the story will automatically return to the last checkpoint saved, allowing the user to try different choices.

Save and Load
Users can save their progress multiple times for different playthroughs and load them later to continue the story.

## Story Parser How to 
This script parses a plain text file, such as a novel or a story, and converts it into a structured YAML format. It uses regular expressions (re) to identify chapters and player choices within the text. The output is a YAML file that represents the story's flow, which can be useful for developing text-based adventure games or other interactive narrative applications.

**Script overview**

The script includes two main functions and an execution block:

parse_text_to_structure(text): This function takes the raw text of a novel as input. It finds all chapters and, for each chapter, identifies the main narrative block and any numbered or bulleted choices. It then organizes this data into a Python dictionary.

save_structure_as_yaml(structure, filename): This function takes the Python dictionary created by the parsing function and writes it to a YAML file with the specified filename.

### Technical details

**How text is parsed**

The script uses the following methods to identify and extract story elements:
Chapter recognition: It uses the regular expression to find chapter headings. This pattern can match "Chapter 1", "CHAPTER I", and other variations.

Text extraction: The content of each chapter is captured by the regex and is divided into narrative and choices.
Choice identification: The script uses the regex to find choices, which can be formatted with numbers (e.g., "1. Go left") or bullets (e.g., "- Go right").

Structure creation: The parsed data is organized into a nested Python dictionary. Each chapter is a top-level key (chapter_1, chapter_2, etc.), and its value is another dictionary containing the narrative text and a list of identified choices.

Outcome placeholders: For each choice, the script creates a placeholder next key (e.g., "next": "chapter_1_choice1") to indicate a future outcome, though it does not automatically link to the correct next chapter.

**YAML output structure**
The resulting YAML file will have the following structure for each chapter:

chapter_1:
  text: You awaken in a dense, mysterious forest. The morning mist conceals hidden dangers, but also whispers of adventure.
  
  choices:
 
  - option: Take the sword lying next to you.

    next: chapter1_sword
  
  - option: Cast a protective spell from your spellbook.

     next: chapter1_spell

chapter_2:
  text: Clutching your sword, you push forward through the thick underbrush. Shadows
    shift and unseen creatures watch.
  
  choices:
 
  - option: Follow the narrow path deeper into the woods.
 
    next: chapter2_woods
 
  - option: Climb a tree to survey your surroundings.
  
    next: chapter2_tree

chapter_3:
 
  text: You raise your hands and recite the incantation. A glow surrounds you, warming
    your spirit but draining your mana.
  
  choices:
 
  - option: Use the magic to illuminate the path

     next: chapter3_spell
 
  - option: Save your energy and tread carefully.
  
    next: chapter3_careful

  ... and so on for each chapter

# Next Section
