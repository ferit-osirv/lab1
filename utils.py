import numpy as np

def print_matrix_operation(f, g, result, operator):
    # Convert arrays to strings
    f_str = np.array2string(f, separator=' ')
    g_str = np.array2string(g, separator=' ')
    result_str = np.array2string(result, separator=' ')

    # Split the string representations into lines
    f_lines = f_str.split('\n')
    g_lines = g_str.split('\n')
    result_lines = result_str.split('\n')

    # Determine the maximum width of the matrices for alignment
    max_width = max(len(line) for line in f_lines + g_lines + result_lines)

    # Print the matrices side by side
    for i, (f_line, g_line, result_line) in enumerate(zip(f_lines, g_lines, result_lines)):
        print(f"{f_line:<{max_width}} {operator if i == 0 else ' '} {g_line:<{max_width}}  {'=' if i == 0 else ' '} {result_line}")

def print_image_matrix(image):        
    for i, row in enumerate(image):
        formatted_row = ''
        for pixel in row:
            formatted_row += '['
            channel_count = len(pixel)
            for i in range(channel_count):
                formatted_row += f'{pixel[i]:3d}'
                if i < channel_count - 1:
                    formatted_row += ''
            formatted_row += ']'
        print(formatted_row)