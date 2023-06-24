class DataError(Exception):
    pass

class CalculationError(Exception):
    pass

def get_number_list (file_name : str) -> list:
    try:
        with open(file_name, "r") as datafile:
            lines = datafile.readlines()
            return lines
    except FileNotFoundError:
        error_message = "Could Not Found The File"
    except PermissionError:
        error_message = "Don't open Now"
        raise DataError(error_message)
    except OSError:
        error_message = "Could not read the file due to an error"
        raise DataError(error_message)

def calculate_sum(number_list : list) -> int:
    total = 0
    try:
        for number in number_list:
            total += int(number)
        return total
    except ValueError:
        raise CalculationError("incorrect value found")

try:
    file_name ="datafile.txt"
    numbers = get_number_list(file_name)
    total = calculate_sum(numbers)
    print(f"sum : {total}")
except DataError as d_err:
    print(d_err)
except CalculationError as c_err:
    print(c_err)








