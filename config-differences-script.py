import os

# Define file paths
preferred_file_path = r"/path/to/preferred/config/preferred-config.txt"
comparison_folder_path = r"/path/to/test/configs/folder/configs-to-be-compared"
output_folder_path = r"/path/to/config/differences/output/config-differences"


# Ensure output folder exists
if not os.path.exists(output_folder_path):
    os.makedirs(output_folder_path)

# Read the content of the preferred config
with open(preferred_file_path, 'r', encoding='utf-8', errors='ignore') as file:
    preferred_config = file.readlines()

# Loop over all files in the comparison folder
for comparison_file_name in os.listdir(comparison_folder_path):
    comparison_file_path = os.path.join(comparison_folder_path, comparison_file_name)
    
    with open(comparison_file_path, 'r', encoding='utf-8', errors='ignore') as file:
        comparison_config = file.readlines()
    
    # Compare the two configurations
    missing_lines = [line for line in preferred_config if line not in comparison_config]
    
    # Create output file name
    output_file_name = os.path.splitext(comparison_file_name)[0] + "_config-differences.txt"
    output_file_path = os.path.join(output_folder_path, output_file_name)
    
    if missing_lines:
        # Write missing lines to the output file
        with open(output_file_path, 'w', encoding='utf-8') as file:
            file.writelines(missing_lines)
        
        print(f"Missing lines for {comparison_file_name} have been written to {output_file_path}.")
    else:
        print(f"No lines are missing for {comparison_file_name}.")

print("Comparisons finished.")
