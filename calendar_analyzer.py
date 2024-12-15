import sys, argparse, csv
import petl as etl
from petl import appendcsv
from datetime import datetime
import plotly.express as px

def main():

    args_main = parsing_func()
    print('argparse arguments: ', args_main)

    if args_main.quickview:
        calendar_details = read_csv()
        quickview(calendar_details)

    if args_main.nrows:
        calendar_details = read_csv()
        print(count_rows(calendar_details))

    if args_main.new_calendar:
        calendar_details = read_csv()
        modified_columns = modify_table_columns(calendar_details)
        updated_table = add_remove_columns(modified_columns)
        append_csv(updated_table)

    if args_main.modify_table_columns:
        calendar_details = read_csv()
        modified_columns = modify_table_columns(calendar_details)
        updated_table = add_remove_columns(modified_columns)
        write_csv(updated_table)
    
    if args_main.monthly_activity:
        calendar_details = read_csv()
        monthly_activity_bar_chart(calendar_details)
    
    if args_main.average_meeting:
        calendar_details = read_csv()
        average_meeting_bar_chart(calendar_details)

    if args_main.time_stats:
        calendar_details = read_csv()
        time_stats(calendar_details)

def read_csv():

    '''Creates a petl table abstraction from the csv'''

    calendar_details = etl.io.csv.fromcsv('/Users/ralphcorey/outlook_analyzer/' + sys.argv[2])
    return calendar_details

def write_csv(calendar_details):

    '''Writes the petl table abstraction to a new csv file'''

    with open('/Users/ralphcorey/Desktop/Programming Work/calendar_analyzer/calendar_details.csv', 'w', newline='') as calendar:
        writer = csv.writer(calendar)
        writer.writerows(calendar_details)

def quickview(calendar_details):

    '''Takes in user input for the number of rows and then returns a customized table of significant information from the calendar'''

    num_rows = int(input("How many rows? "))

    quickview = etl.cut(calendar_details, 0, "Start_Date", "Length_of_Time")
    print(quickview.look(num_rows))

def append_csv(new_calendar_details):

    '''Performs the same updates as modify table column and ppends a new file to the existing dataset'''

    appendcsv(new_calendar_details, '/Users/ralphcorey/Desktop/Programming Work/calendar_analyzer/calendar_details.csv') 

def count_rows(calendar_details):

    '''Counts the total rows in the calendar table'''

    return f'file rows: {calendar_details.nrows()}'

def modify_table_columns(calendar_details):

    '''Performs updates to the Start, End, date and times, add columns for Month, and length of time and writes the output to a new csv'''

    modify_headers = etl.rename(calendar_details, 
           {'Start Date':'Start_Date',
           'End Date':'End_Date',
           'Start Time':'Start_Time',
           'End Time':'End_Time'
           })
    modify_start_date = etl.convert(modify_headers, 'Start_Date', lambda d: datetime.strptime(d, '%m/%d/%Y'))
    modify_end_date = etl.convert(modify_start_date, 'End_Date', lambda d: datetime.strptime(d, '%m/%d/%Y'))
    modify_start_time = etl.convert(modify_end_date, "Start_Time", lambda row: datetime.strptime(row, '%I:%M:%S %p'))
    modify_end_time = etl.convert(modify_start_time, "End_Time", lambda row: datetime.strptime(row, '%I:%M:%S %p'))

    return modify_end_time

def add_remove_columns(calendar_details):

    '''Performs updates to add the month and length of a meeting and remove several unneeded columns'''

    add_month_column = etl.addfield(calendar_details, 'Month', lambda row: row['Start_Date'])
    updated_table = etl.convert(add_month_column, 'Month', lambda mon: int(mon.month))
    sorted_table = etl.sort(updated_table, 'Month')
    add_length_of_time = etl.addfield(sorted_table, "Length_of_Time", lambda row: row["End_Time"] - row["Start_Time"])
    convert_times = etl.convert(add_length_of_time, "Length_of_Time", lambda row: row.total_seconds() / 60)
    remove_zero_times = etl.select(convert_times, "Length_of_Time", lambda rmv: rmv != 0.0)
    final_table = etl.cutout(remove_zero_times, *range(10, 13))

    return final_table

def monthly_activity_bar_chart(calendar_details):
    
    '''Generates a plotly bar chart that depicts the number of meetings in the classroom month over month'''

    monthly_activity_levels = etl.aggregate(calendar_details, 'Month', len)
    convert_month = etl.convert(monthly_activity_levels, 'Month', int)
    sorted_table = etl.sort(convert_month)
    fig = px.bar(sorted_table, 
                 x=0, y=1, 
                 labels= {'x':'Month', 'y':'# of Meetings'},
                 title= 'Number of Meetings by Month')

    return fig.show()

def average_meeting_bar_chart(calendar_details):

    '''Generates a plotly bar chart that depicts the average length of meetings month over month'''

    initial_table = etl.cut(calendar_details, 'Month', 'Length_of_Time')
    convert_time_column = etl.convert(initial_table, 'Length_of_Time', float)
    sum_meeting_times = etl.aggregate(convert_time_column, 'Month', sum, 'Length_of_Time')

    monthly_activity_levels = etl.valuecounter(calendar_details, 'Month')
    sorted_monthly_activity = dict(sorted(monthly_activity_levels.items()))

    monthly_count_list = [list(sorted_monthly_activity.values())]
    monthly_count_table = etl.fromcolumns(monthly_count_list)
    monthly_values_column = [row[0] for row in etl.data(monthly_count_table)]

    sum_meeting_times_updated = etl.addcolumn(sum_meeting_times, '# of Meetings', monthly_values_column)

    avg_meeting_times = etl.addfield(sum_meeting_times_updated, 'Avg_Mtg_Length', lambda row: row['value'] // row['# of Meetings'])
    convert_month = etl.convert(avg_meeting_times, 'Month', int)
    sorted_table = etl.sort(convert_month)
    #print(sorted_table.lookall())

    fig = px.bar(sorted_table, 
                 x=0, y=3, 
                 labels= {'x':'Month', 'y':'Avg Mtg Length (Min)'}, 
                 title= 'Avg Meeting Times (Min)')

    return fig.show()

def time_stats(calendar_details):

    '''Generates the overall stats for classroom time usage'''

    return print(etl.stats(calendar_details, "Length_of_Time")) 

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

if __name__ == '__main__':
    main()