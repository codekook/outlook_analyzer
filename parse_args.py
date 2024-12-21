import argparse

def parsing_func():

    '''Creates a command line parser object and arguments to be passed for the application's functionality'''

    parser = argparse.ArgumentParser()

    parser.add_argument('-nc', '--new_calendar', 
                        required=False, 
                        help='Accepts the file name of a new calendar in csv format, performs the modify table columns actions and appends the result to the existing dataset')
    
    parser.add_argument('-r', '--nrows',
                        required=False,
                        help='Returns the number of rows in the table')
    
    parser.add_argument('-mc', '--modify_table_columns',
                        required=False,
                        help='Takes in a calendar.csv, modifies the columns and writes it to a new csv')
    
    parser.add_argument('-ma', '--monthly_activity',
                        required=False,
                        help='Returns a plotly bar chart that depicts the monthly number of meetings in the classroom')
    
    parser.add_argument('-am', '--average_meeting',
                        required=False,
                        help='Returns a plotly bar chart that depicts the average meeting length month over month')
    
    parser.add_argument('-s', '--time_stats',
                        required=False,
                        help='Generates stats for the "Length of Time" column in the calendar csv')
    
    parser.add_argument('-q', '--quickview',
                        required=False,
                        help='Prints the number rows of a customized table for quick review')
    
    args = parser.parse_args()
    return args