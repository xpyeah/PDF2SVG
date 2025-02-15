# PDF to SVG Converter

This is a simple Python script that leverages the PyMuPDF library to convert each page of a PDF file into an independent SVG file.

## Install Dependencies

Before running this script, you need to install the `PyMuPDF` library. You can install it using `pip`:

```bash
pip install PyMuPDF
```

## Usage

### 1. Preparation
Save the script as a Python file, for example, `pdf_to_svg.py`.

### 2. Basic Command
Run the script in the command line and specify the path of the PDF file to be converted. You can optionally specify the output folder. If not specified, the SVG files will be saved in the current directory by default.

```bash
python pdf_to_svg.py "path/to/your/pdf/file.pdf" -o "path/to/output/folder"
```

### 3. Parameter Explanation

#### Required Parameter
- `pdf_path`: The full path of the PDF file to be converted. For example: `"algorithm_2-2.pdf"` or `"/home/user/documents/report.pdf"`.

#### Optional Parameter
- `-o` or `--output_folder`: Specify the path of the output folder where the SVG files will be saved. If this parameter is not provided, the current directory will be used by default. For example: `-o "./output"` or `--output_folder "/home/user/output"`.

### 4. Example
Suppose you have a PDF file named `example.pdf` and you want to convert it into SVG files and save them in the `./output` folder. You can use the following command:

```bash
python pdf_to_svg.py "example.pdf" -o "./output"
```

### 5. Output Results
After the conversion is completed, each page of the PDF will be saved as an independent SVG file. The file name format is `{original PDF file name}_page_{page number}.svg`. For example, if the original PDF file is named `example.pdf`, the converted SVG files may be `example_page_1.svg`, `example_page_2.svg`, etc.

## Error Handling
If an error occurs during the conversion process (such as file opening failure, folder creation failure, etc.), the script will output the corresponding error message. Please check the file path, permissions, etc. according to the error prompt.

## Notes
- Please ensure that the input PDF file path and output folder path are correct, and you have the corresponding read and write permissions.
- The conversion process may take some time depending on the size and complexity of the PDF file. Please be patient. 