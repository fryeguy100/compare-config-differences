# compare-config-differences
Compare config differences between routers, switches, etc. Compares configs against a "preferred config".

Config Differences Comparison Script
This script helps identify the missing lines between a "preferred" configuration file and one or more test/comparison configuration files. It then outputs these missing lines into individual "config differences" files, making it easier to spot discrepancies.

Features:
Compares a preferred configuration against multiple test/comparison configurations.
Outputs config differences to separate files.
Automatically ensures the output directory exists.
Supports UTF-8 encoded files, gracefully handling decoding errors.


How to Use

Clone this repository:

gh repo clone fryeguy100/compare-config-differences


Edit the script to specify the paths to your configurations:

preferred_file_path = r"/path/to/preferred/config/preferred-config.txt"
comparison_folder_path = r"/path/to/test/configs/folder/configs-to-be-compared"
output_folder_path = r"/path/to/config/differences/output/config-differences"

Run the script:

python3 <script-name>.py
Check the specified output_folder_path for difference files. These files will indicate which lines from the preferred configuration are missing in the test configurations.

Requirements:

Python 3.x
Ensure your configurations are UTF-8 encoded for best results.
Make sure that all files that need to be compared are in the "configs-to-be-compared" folder.
This script loops through each file in the "configs-to-be-compared" directory so it can compare many configs at once. "config-differences" will be appended to the end of the original config names for each comparison file.

Contributing:

Feel free to fork this repository, make your improvements, and submit a pull request. Feedback and contributions are always welcome.
