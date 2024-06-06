#!/bin/bash

rm -r mockup_folder

# Create folders.
create_directories() {
  local parent_folder=$1  # The first argument is the parent folder
  shift  # Remove the first argument, leaving the rest as subfolders
  local subfolders=("$@")  # The remaining arguments are the subfolders

  # Create each subfolder inside the parent folder
  for subfolder in "${subfolders[@]}"; do
    mkdir -p "$parent_folder/$subfolder"
  done
}

parent_folder="mockup_folder"
subfolders=(
    "example_dir1/code"
    "example_dir1/results/tables"
    "example_dir1/results/figures"
    "example_dir2/code"
    "example_dir2/results"
    "downloads"
    "send2/"
)
create_directories "$parent_folder" "${subfolders[@]}"
echo "Directories created successfully."



# Create input files.
create_files() {
    local files=("$@")  # Accept an array of files as arguments

    # Loop through the array and create directories and files
    for file in "${files[@]}"; do
        # Extract the directory path from the file path
        dir=$(dirname "$file")
        # Create the directory if it doesn't exist
        mkdir -p "$dir"
        # Create the file
        touch "$file"
    done
}

files=(
    "mockup_folder/downloads/test_file1.R"
    "mockup_folder/downloads/test_file2.R"
    "mockup_folder/downloads/test_file.do"
)
create_files "${files[@]}"
echo "input files created successfully."


# Create output files.
files=(
    "mockup_folder/example_dir1/results/tables/descriptives.csv"
    "mockup_folder/example_dir1/results/figures/figure.png"
    "mockup_folder/example_dir2/results/collapse.dta"
)
create_files "${files[@]}"
echo "Output files created successfully."

# Create request.json
echo '[
    {
        "id": "5a5a1e0c-849c-4d3b-a26a-1dbead5a844d",
        "input_files": ["mockup_folder/example_dir1/code/test_file1.R", "mockup_folder/example_dir1/code/test_file2.R"],
        "output_files": ["mockup_folder/example_dir1/results/tables/descriptives.csv", "mockup_folder/example_dir1/results/figures/figure.png"]
    },
    {
        "id": "1c8406e9-ff40-4714-bebf-84b7c6d27838",
        "input_files": ["mockup_folder/example_dir2/code/test_file.do"],
        "output_files": ["mockup_folder/example_dir2/results/collapse.dta"]
    }
]' > mockup_folder/downloads/request.json
echo "request.json created successfully."