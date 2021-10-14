from project.cars.utils import refactor_arduino_sketch, compile_arduino_sketch, download_arduino_sketch


def process_arduino_sketch(filepath, bin_path):
    refactor_arduino_sketch(filepath)
    error_code, compile_result = compile_arduino_sketch(filepath, bin_path)
    if error_code:
        return compile_result

    download_arduino_sketch(bin_path)
