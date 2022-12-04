# Easy Rider Bus Company

## Overview

This Python project is a comprehensive tool designed to validate a database of bus stops. It checks for both structural and logical inconsistencies in the data and ensures it adheres to specific formatting rules. These validations are crucial for maintaining a reliable and accurate transportation database.

## Features

- **Type and Required Field Validation:** Ensures the data types of each field are correct and checks the presence of required fields.
- **Format Validation:** Validates the formatting of stop names, stop types, and arrival times against predefined patterns.
- **Line Consistency Checks:** Verifies that each bus line has a start and an end stop, and there are no timing inconsistencies between consecutive stops.
- **Stop Classification:** Identifies start, finish, transfer, and on-demand stops within the dataset.
- **Error Reporting:** Clearly reports the number and type of errors found, providing guidance on what needs fixing.

## Requirements

- [Python 3](https://www.python.org/downloads/)

## Installation

This application is written in Python, so you'll need Python installed on your computer to run it. If you don't have Python installed, you can download it from [python.org](https://www.python.org/downloads/).

To install this project, clone the repository to your local machine:

```
git clone https://github.com/SonikSeven/easy-rider-bus-company.git
```

## Usage

1. Prepare your bus stop database in a JSON file format. Make sure it follows the expected schema:
   ```
   [
     {
       "bus_id": int,
       "stop_id": int,
       "stop_name": "string",
       "next_stop": int,
       "stop_type": "string",
       "a_time": "string"
     }
   ]
   ```
2. Open the command line and navigate to the directory where the script is located.

3. Run the tool, passing the path to your JSON file as input:
   ```
   python main.py <path_to_your_json_file>
   ```
4. Review the output for any reported errors or inconsistencies and adjust your database accordingly.

## License

This project is licensed under the [MIT License](LICENSE.txt).
