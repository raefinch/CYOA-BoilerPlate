from classes import StoryTree, GameSession, Character, SaveManager, FileParser

def main():
    # Load story from a formatted file (example JSON)
    with open("TestText.yaml", "r", encoding="utf-8") as f:
        file_content = f.read()

    story_tree = FileParser.parse_text_to_storytree(file_content)

    # Initialize character with default attributes
    main_character = Character(name="Hero", attributes={"health": 10, "Gold": 50})

    # Initialize game session with the tree and character
    session = GameSession(story_tree, main_character)

    # Start game at node 1 or designated starting node
    session.start(start_node_id="1")

    # Simple game loop
    while True:
        current_text = session.get_current_text()
        print("\n" + current_text + "\n")

        current_node = story_tree.get_node(session.current_node_id)
        if not current_node or not current_node.choices:
            print("The End.")
            break

        for idx, choice in enumerate(current_node.choices):
            print(f"{idx + 1}: {choice.description}")

        # Get user input for choice
        try:
            selected = int(input("Choose an option: ")) - 1
            if selected < 0 or selected >= len(current_node.choices):
                print("Invalid choice number. Try again.")
                continue
            session.choose(selected)
        except ValueError:
            print("Please enter a valid number.")
            continue

if __name__ == "__main__":
    main()
