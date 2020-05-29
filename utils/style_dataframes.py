def get_cell_styles(color):
    return 'background-color: %s; font-size: %s; font-weight: %s;' % (color, '1.2em', 'bold')

def get_column_color(column_name):
    if (column_name in ['FULL_PROJECT_NUM', 'CORE_PROJECT_NUM']):
        return get_cell_styles('#ff677d')
    elif (column_name in ['ACTIVITY', 'ADMINISTERING_IC', 'APPLICATION_TYPE', 'SERIAL_NUMBER', 'SUPPORT_YEAR']):
        return get_cell_styles('#30e3ca')
    return ''

def highlight_project_numbers(val):
    return [get_column_color(column_name) for column_name in list(val.index)]