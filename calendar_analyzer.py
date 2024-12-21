import helpers
from parse_args import parsing_func

def main():

    args_main = parsing_func()
    print('argparse arguments: ', args_main)

    if args_main.quickview:
        calendar_details = helpers.read_csv()
        helpers.quickview(calendar_details)

    if args_main.nrows:
        calendar_details = helpers.read_csv()
        print(helpers.count_rows(calendar_details))

    if args_main.new_calendar:
        calendar_details = helpers.read_csv()
        modified_columns = helpers.modify_table_columns(calendar_details)
        updated_table = helpers.add_remove_columns(modified_columns)
        helpers.append_csv(updated_table)

    if args_main.modify_table_columns:
        calendar_details = helpers.read_csv()
        modified_columns = helpers.modify_table_columns(calendar_details)
        updated_table = helpers.add_remove_columns(modified_columns)
        helpers.write_csv(updated_table)
    
    if args_main.monthly_activity:
        calendar_details = helpers.read_csv()
        helpers.monthly_activity_bar_chart(calendar_details)
    
    if args_main.average_meeting:
        calendar_details = helpers.read_csv()
        helpers.average_meeting_bar_chart(calendar_details)

    if args_main.time_stats:
        calendar_details = helpers.read_csv()
        helpers.time_stats(calendar_details)


if __name__ == '__main__':
    main()