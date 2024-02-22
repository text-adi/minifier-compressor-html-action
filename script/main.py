import os
import shutil
import minify_html


def minify_file(file_path: str):
    with open(file_path, "r") as f:
        source_code = f.read()
        minified = minify_html.minify(
            source_code,
            keep_closing_tags=False,
            keep_comments=False,
            keep_html_and_head_opening_tags=False,
            keep_input_type_text_attr=False,
            keep_ssi_comments=False,
            minify_css=True,
            minify_js=True,
            preserve_brace_template_syntax=False,
            preserve_chevron_percent_template_syntax=False,
            remove_bangs=False,
            remove_processing_instructions=False,
        )
    with open(file_path, "w") as f:
        f.write(minified)


class Tools:

    def copy_files(self, src_dir, dest_dir):
        # Перевіряємо чи існує каталог призначення, якщо ні - створюємо
        if not os.path.exists(dest_dir):
            os.makedirs(dest_dir)

        # Перебираємо файли та підкаталоги в початковому каталозі
        for item in os.listdir(src_dir):
            # Формуємо повні шляхи до кожного об'єкту
            src_item_path = os.path.join(src_dir, item)
            dest_item_path = os.path.join(dest_dir, item)

            if os.path.isdir(src_item_path):
                # Якщо це каталог, рекурсивно копіюємо відповідний каталог
                self.copy_files(src_item_path, dest_item_path)
            else:
                # Якщо це файл, просто копіюємо його в новий каталог
                shutil.copy2(src_item_path, dest_item_path)  # shutil.copy2 копіює метадані файлу

    def get_all_file_in_dir(self, path_to_dir: str, type_file: str = 'po'):
        """Рекурсивний пошук файлів в каталозі"""
        for root, dirs, files in os.walk(path_to_dir):
            for file in files:
                if '.' in file and type_file == file.split('.')[-1]:
                    yield root, file

                for dir_name in dirs:
                    self.get_all_file_in_dir(dir_name)


class Basic:

    @staticmethod
    def title_msg():
        return """

     ___ __ __      ________      ___   __       ________      ______     __  __         ___   ___      _________   ___ __ __      __          
    /__//_//_/\    /_______/\    /__/\ /__/\    /_______/\    /_____/\   /_/\/_/\       /__/\ /__/\    /________/\ /__//_//_/\    /_/\         
    \::\| \| \ \   \__.::._\/    \::\_\\  \ \   \__.::._\/    \::::_\/_  \ \ \ \ \      \::\ \\  \ \   \__.::.__\/ \::\| \| \ \   \:\ \        
     \:.      \ \     \::\ \      \:. `-\  \ \     \::\ \      \:\/___/\  \:\_\ \ \      \::\/_\ .\ \     \::\ \    \:.      \ \   \:\ \       
      \:.\-/\  \ \    _\::\ \__    \:. _    \ \    _\::\ \__    \:::._\/   \::::_\/       \:: ___::\ \     \::\ \    \:.\-/\  \ \   \:\ \____  
       \. \  \  \ \  /__\::\__/\    \. \`-\  \ \  /__\::\__/\    \:\ \       \::\ \        \: \ \\::\ \     \::\ \    \. \  \  \ \   \:\/___/\ 
        \__\/ \__\/  \________\/     \__\/ \__\/  \________\/     \_\/        \__\/         \__\/ \::\/      \__\/     \__\/ \__\/    \_____\/ 
                                                                                                                                                                                                        
    """

    @staticmethod
    def line_msg():
        return 29 * '-'


def main():
    print(Basic.title_msg())

    print(Basic.line_msg())
    print("Start minifier-compressor-html-action...")
    print(Basic.line_msg())

    print("Get source path...")
    source_dir: str = os.environ.get('DIR', None)
    if source_dir is None:
        raise ValueError("No DIR change set. Check the environment value settings")

    current_directory: str = os.getcwd()
    source_path = os.path.join(current_directory, source_dir)
    if not os.path.exists(source_path):
        print("Directory not found in file system. Exit...")
        return

    destination_dir: str | None = os.environ.get('DESTINATION_DIR', None)

    if destination_dir is not None and source_dir != destination_dir:
        print()
        print(f'DESTINATION_DIR is set. The process of copying the directory will take place')

        destination_path = os.path.join(current_directory, destination_dir)

        print(f'Copy directory from {source_path} to {destination_path}...')
        Tools().copy_files(source_path, destination_path)
        print('The copy process completed successfully')
        source_path = destination_path
    else:
        print(f'DESTINATION_DIR is not set. Skipping the process of copying from source directory')
    print()

    print(f"Starting html minification process in {source_dir}...")
    for path_to_file, file in Tools().get_all_file_in_dir(source_path, 'html'):
        file_path = os.path.join(path_to_file, file)
        print(f"Minify {file_path}")
        minify_file(file_path)
    print()
    print("Success.")


if __name__ == '__main__':
    main()