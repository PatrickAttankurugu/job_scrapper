import json

def save_data(data, filename):
    # Convert the data to JSON and save it to a file
    with open(filename, 'w') as f:
        json.dump(data, f)
