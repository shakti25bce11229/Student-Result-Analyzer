import uuid

def generate_id():
    return str(uuid.uuid4())[:8]

def pause():
    input('\nPress Enter to continue...')
