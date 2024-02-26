import json
import os
import shutil
import minify_html

PARAM = "PARAM_"


def param_env(name_param: str) -> bool:
    if name_param.startswith(PARAM):
        new_param: str = name_param.split(PARAM)[-1]
        return str(os.environ.get(new_param, False)).lower() in ['true', '1']
    return False


settings_minify = dict(
    keep_closing_tags=param_env(PARAM + 'KEEP_CLOSING_TAGS'),
    keep_comments=param_env(PARAM + 'KEEP_COMMENTS'),
    keep_html_and_head_opening_tags=param_env(PARAM + 'KEEP_HTML_AND_HEAD_OPENING_TAGS'),
    keep_input_type_text_attr=param_env(PARAM + 'KEEP_INPUT_TYPE_TEXT_ATTR'),
    keep_ssi_comments=param_env(PARAM + 'KEEP_SSI_COMMENTS'),
    minify_css=param_env(PARAM + 'MINIFY_CSS'),
    minify_js=param_env(PARAM + 'MINIFY_JS'),
    preserve_brace_template_syntax=param_env(PARAM + 'PRESERVE_BRACE_TEMPLATE_SYNTAX'),
    preserve_chevron_percent_template_syntax=param_env(PARAM + 'PRESERVE_CHEVRON_PERCENT_TEMPLATE_SYNTAX'),
    remove_bangs=param_env(PARAM + 'REMOVE_BANGS'),
    remove_processing_instructions=param_env(PARAM + 'REMOVE_PROCESSING_INSTRUCTIONS'),
)


def minify_file(file_path: str):
    with open(file_path, "r") as f:
        source_code = f.read()
        minified = minify_html.minify(
            source_code,
            **settings_minify
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
            \::\| \| \ \   \__.::._\/    \::\_\\\  \ \   \__.::._\/    \::::_\/_  \ \ \ \ \      \::\ \\\  \ \   \__.::.__\/ \::\| \| \ \   \:\ \        
             \:.      \ \     \::\ \      \:. `-\  \ \     \::\ \      \:\/___/\  \:\_\ \ \      \::\/_\ .\ \     \::\ \    \:.      \ \   \:\ \       
              \:.\-/\  \ \    _\::\ \__    \:. _    \ \    _\::\ \__    \:::._\/   \::::_\/       \:: ___::\ \     \::\ \    \:.\-/\  \ \   \:\ \____  
               \. \  \  \ \  /__\::\__/\    \. \`-\  \ \  /__\::\__/\    \:\ \       \::\ \        \: \ \\\::\ \     \::\ \    \. \  \  \ \   \:\/___/\ 
                \__\/ \__\/  \________\/     \__\/ \__\/  \________\/     \_\/        \__\/         \__\/ \::\/      \__\/     \__\/ \__\/    \_____\/ 
                                                                                                                                                                                                                
                """

    @staticmethod
    def line_msg(s='-'):
        return 29 * s

    @staticmethod
    def watch_settings():
        print("Basic param:")
        for key, value in settings_minify.items():
            print(f"{key} - {value}")


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

    print(Basic.line_msg('%'))
    print()
    Basic.watch_settings()
    print()
    print(Basic.line_msg('%'))
    print()

    print(f"Starting html minification process in {source_path}...")

    for path_to_file, file in Tools().get_all_file_in_dir(source_path, 'html'):
        file_path = os.path.join(path_to_file, file)
        print(f"Minify {file_path}")
        minify_file(file_path)
    print()
    print("Success.")


if __name__ == '__main__':
    main()
