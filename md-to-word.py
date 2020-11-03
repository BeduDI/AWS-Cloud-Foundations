import glob
import os
import zipfile
import zlib

import pypandoc


def transform():
    origin_ext = 'md'
    output_ext = "docx"
    directories_in_curdir = filter(os.path.isdir, os.listdir(os.curdir))
    for directory in [_ for _ in directories_in_curdir if len(_) > 10]:
        with zipfile.ZipFile(f'{directory}.zip', 'w', zipfile.ZIP_DEFLATED, compresslevel=9) as zip_obj:
            for name in glob.glob(f'{directory}/*.{origin_ext}'):
                output_file_name = f"{name.replace(origin_ext,'')}{output_ext}"
                print(output_file_name)
                output = pypandoc.convert_file(name, output_ext, outputfile=output_file_name,
                                               extra_args=['-V', 'geometry:margin=0.5cm', "--resource-path", directory])
                zip_obj.write(output_file_name)


if __name__ == "__main__":
    transform()
