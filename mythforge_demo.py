import json

class MythForge:
    def __init__(self):
        self.content_modules = {}

    def add_module(self, module_name, module_data):
        """Adds a new content module to the platform."""
        self.content_modules[module_name] = module_data
        print(f"Module '{module_name}' added.")

    def get_module(self, module_name):
        """Retrieves a specific content module."""
        return self.content_modules.get(module_name)

    def generate_project_overview(self, project_name):
        """Generates a high-level overview of a project by combining module data."""
        overview = f"Project: {project_name}\n\n" # Project name is a core element

        # Example of integrating different content types
        if 'story' in self.content_modules:
            story_data = self.content_modules['story']
            overview += f"Storyline:\n - Title: {story_data.get('title', 'N/A')}\n - Genre: {story_data.get('genre', 'N/A')}\n\n"

        if 'code_snippets' in self.content_modules:
            code_data = self.content_modules['code_snippets']
            overview += f"Key Code Components:\n - Language: {code_data.get('language', 'N/A')}\n - Description: {code_data.get('description', 'N/A')}\n\n"

        if 'art_assets' in self.content_modules:
            art_data = self.content_modules['art_assets']
            overview += f"Visual Elements:\n - Style: {art_data.get('style', 'N/A')}\n - Assets: {', '.join(art_data.get('assets', []))}\n"

        return overview

# --- Demonstration ---
if __name__ == "__main__":
    mythforge = MythForge()

    # Adding a 'story' module
    story_module = {
        "title": "The Last Starship",
        "genre": "Sci-Fi Adventure",
        "plot_summary": "A lone explorer seeks a legendary artifact across the galaxy."
    }
    mythforge.add_module("story", story_module)

    # Adding a 'code_snippets' module
    code_module = {
        "language": "Python",
        "description": "Core logic for ship navigation and AI interaction.",
        "snippets": [
            "def navigate_to(destination): ...",
            "def engage_ai(query): ..."
        ]
    }
    mythforge.add_module("code_snippets", code_module)

    # Adding an 'art_assets' module
    art_module = {
        "style": "Cyberpunk",
        "assets": ["spaceship_model.glb", "alien_creature_concept.png", "cityscape_background.jpg"]
    }
    mythforge.add_module("art_assets", art_module)

    print("\n--- Generating Project Overview ---")
    project_overview = mythforge.generate_project_overview("Project Nebula")
    print(project_overview)

    # Retrieving a specific module
    retrieved_story = mythforge.get_module("story")
    print(f"\nRetrieved Story Module: {json.dumps(retrieved_story, indent=2)}")
