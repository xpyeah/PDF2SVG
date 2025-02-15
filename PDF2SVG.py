import fitz  # PyMuPDF 库
import os
import argparse

def pdf_to_svg(pdf_path, output_folder):
    try:
        # 打开 PDF 文件
        pdf_document = fitz.open(pdf_path)

        # 确保输出文件夹存在
        os.makedirs(output_folder, exist_ok=True)

        # 获取 PDF 文件名（不包含扩展名）
        pdf_name = os.path.splitext(os.path.basename(pdf_path))[0]

        # 遍历 PDF 的每一页
        for page_num in range(pdf_document.page_count):
            page = pdf_document.load_page(page_num)

            # 输出当前转换的页码
            print(f"正在转换第 {page_num + 1} 页...")

            # 将页面转换为 SVG 格式
            svg_data = page.get_svg_image()

            # 生成 SVG 文件名，保留原 PDF 名并加上页码
            svg_filename = os.path.join(output_folder, f"{pdf_name}_page_{page_num + 1}.svg")
            with open(svg_filename, 'w', encoding='utf-8') as svg_file:
                svg_file.write(svg_data)

        pdf_document.close()
        print(f"PDF 已成功转换为 SVG, 并保存到文件夹: {output_folder}")
    except Exception as e:
        print(f"转换过程中出现错误: {e}")

if __name__ == "__main__":
    # 创建命令行参数解析器
    parser = argparse.ArgumentParser(description="将 PDF 文件转换为 SVG 文件")

    # 添加 PDF 文件路径参数
    parser.add_argument("pdf_path", type=str, help="要转换的 PDF 文件的路径")

    # 添加输出文件夹参数
    parser.add_argument("-o", "--output_folder", type=str, default="./", help="保存 SVG 文件的文件夹，默认为当前目录")

    # 解析命令行参数
    args = parser.parse_args()

    # 调用转换函数
    pdf_to_svg(args.pdf_path, args.output_folder)