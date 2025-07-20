# Conpanio - Console Assistant

A simple but powerful console assistant bot for managing your contacts.

## Installation

Navigate to the project's root directory and run the following command. This will install the application and all necessary dependencies, making the `conpanio` command available in your terminal.

```bash
pip install .
```

## Usage

After installation, you can run the assistant from anywhere in your system by simply typing:

```bash
conpanio
```

## Commands
- `hello`: Greet the assistant. 
- `birthdays [days]`: Show upcoming birthdays. 

#### Contact Management
- `all`: Show all contacts in a table. 
- `add <name> <phone>`: Add a new contact with a name and phone number. 
- `change <name>`: Interactively edit a contact's fields. 
- `delete <name>`: Delete a contact. 
- `find <name>`: Find a contact by name. 

#### Note & Tag Management
- `add-note <name> <text>`: Add a note to an existing contact. You can add tags to the note interactively. 
- `edit-note <name>`: Edit the text or tags of a specific note for a contact. 
- `find-notes <text>`: Search for contacts by note content. 
- `find-tag <tag>`: Search for contacts by a tag in notes.
- `tags`: Show all unique tags and list contacts for a selected tag. 
 
#### Other Commands
- `help`: Display the list of commands. 
- `exit, close`: Save data and exit the assistant.

