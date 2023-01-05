import subprocess # module to run processes in the command line

# Get all the metadata of an image using ExifTool
def get_all_metadata(img_path):

    # Run ExifTool like you would in the command prompt
    output = subprocess.check_output(["exiftool", img_path])

    # Parse ExifTool output and store data in a dictionary
    results = output.decode().split("\r\n")
    data = {}
    for i, line in enumerate(results):
        if i < len(results)-1:
            s = line.split(":")
            s_key = s[0].rstrip()
            s_val = s[1]
            data[s_key] = s_val

    return data

def get_subset_data(data, params):

    # Extracts select metadata keys and vals from a dict (data) and
    # stores them into a new dictionary
    # Params is a list containing the select metadata keys
    subset_data = {}
    for key, val in data.items():
        if key in params:
            subset_data[key] = val
    
    return subset_data

#TODO: Write a function to match the recipe data to a recipe in my camera.