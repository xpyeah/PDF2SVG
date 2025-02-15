# PDF 转 SVG 工具

这是一个使用 Python 编写的简单脚本，借助 PyMuPDF 库将 PDF 文件的每一页转换为独立的 SVG 文件。

## 安装依赖库

在运行此脚本之前，你需要安装 `PyMuPDF` 库。可以使用 `pip` 进行安装：

```bash
pip install PyMuPDF
```

## 使用方法

### 1. 准备工作
将脚本保存为一个 Python 文件，例如 `pdf_to_svg.py`。

### 2. 基本命令
在命令行中运行脚本，指定要转换的 PDF 文件路径。你可以选择指定输出文件夹，如果不指定，默认将 SVG 文件保存到当前目录。

```bash
python pdf_to_svg.py "path/to/your/pdf/file.pdf" -o "path/to/output/folder"
```

### 3. 参数说明

#### 必需参数
- `pdf_path`：要转换的 PDF 文件的完整路径。例如：`"算法2 - 2.pdf"` 或 `"/home/user/documents/report.pdf"`。

#### 可选参数
- `-o` 或 `--output_folder`：指定保存 SVG 文件的输出文件夹路径。如果不提供此参数，默认使用当前目录。例如：`-o "./output"` 或 `--output_folder "/home/user/output"`。

### 4. 示例
假设你有一个名为 `example.pdf` 的 PDF 文件，你想将其转换为 SVG 文件并保存到 `./output` 文件夹中，可以使用以下命令：

```bash
python pdf_to_svg.py "example.pdf" -o "./output"
```

### 5. 输出结果
转换完成后，每个 PDF 页面将被保存为一个独立的 SVG 文件，文件名格式为 `{原 PDF 文件名}_page_{页码}.svg`。例如，如果原 PDF 文件名为 `example.pdf`，那么转换后的 SVG 文件可能会是 `example_page_1.svg`、`example_page_2.svg` 等。

## 错误处理
如果在转换过程中出现错误（例如文件打开失败、文件夹创建失败等），脚本会输出相应的错误信息。请根据错误提示检查文件路径、权限等问题。

## 注意事项
- 请确保输入的 PDF 文件路径和输出文件夹路径是正确的，并且你有相应的读写权限。
- 转换过程可能会根据 PDF 文件的大小和复杂度花费一定的时间，请耐心等待。