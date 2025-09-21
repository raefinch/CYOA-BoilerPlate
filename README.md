# CYOA-Boilerplate
A boilerplate to help users easily create their own choose your own adventure app


How to Use
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



Story Parser How to Use
This Python script converts a plain text novel file into a structured YAML file that represents the interactive story as chapters with choices. The YAML output can then be used to build the tree-based adventure in your app.

Prerequisites
Python 3.x installed
PyYAML package installed 

Steps
Prepare your novel text file
Format your novel so that chapters begin with a heading like Chapter 1 or CHAPTER I.
Choices inside chapters should be listed as numbered or bulleted lines (e.g., 1. Choice text, - Choice text).

Place the novel file
Put your novel text file in the project directory, e.g., novel.txt.

Run the script
Execute the provided Python script:

bash
python parse_novel_to_yaml.py
The script will parse chapters and choices, and output story.yaml file in the same directory.

Check the output YAML
Open story.yaml to verify the structure. You should see sections for each chapter with narrative text and a list of choices.

Integrate YAML into your app
Use the generated YAML file as input to your app’s parser, which transforms it into the node-based tree structure for gameplay.

Customization
If your novel’s formatting differs, adjust the regex patterns in the script accordingly (e.g., chapter headings or choice formats).

Add attribute effects, outcomes linking, or checkpoints manually or extend the script to parse those from your novel.

Example Output Snippet
text
chapter_1:
  text: "You awaken in a dark forest. What do you do?"
  choices:
    - option: "Use the sword"  -> chapter_1_choice1
    - option: "Cast magic" -> chapter_1_choice2
    
This guide helps users quickly understand how to run your script, prepare input files, and how the output fits into the overall app development workflow.
