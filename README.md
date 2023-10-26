# Parsing .xls into csv

# Data Conversion Script

Overview
This Python script is designed to convert data from a text file with a specific format into a CSV file. It filters the data based on certain conditions and organizes it into a structured CSV format. This README provides information on how to use the script and describes its functionality.

## Usage

Usage
Prerequisites: Ensure you have Python installed on your system.

File Preparation:

Place the text file (forParsing_task.xls) you want to convert in the same directory as the script, or specify the file path in the script.
Verify that the text file follows a specific format where each line is divided into 12 fields separated by the '|' character, and lines containing ' Stat' should be skipped.
Running the Script:

Execute the Python script.
The script will read the input text file, filter the data, and convert it into a CSV format.
Output:

The script will generate a sample.csv file in the same directory as the script, containing the converted data.
Customization
If your input file is not located in the same directory as the script, you can specify the full file path by modifying the file_path variable in the script.

You can adjust the filtering conditions or the column names used in the CSV file by modifying the code as needed.

Error Handling
If the script encounters any issues, it may print error messages or raise exceptions. Ensure that the input file format and path are correct.
License
This script is provided under an open-source license. You are free to modify and distribute it as needed.

Contact
If you have any questions or encounter issues, feel free to contact RAMANATHAN-19 at ramanathanthedeveloper@gmail.com.
