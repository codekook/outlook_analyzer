import api
from cli import parsing_func

def main():

    args_main = parsing_func()
    print('argparse arguments: ', args_main)

    if args_main.quickview:
        calendar_details = api.read_csv()
        print(api.quickview(calendar_details))

    if args_main.nrows:
        calendar_details = api.read_csv()
        print(api.count_rows(calendar_details))

    if args_main.new_calendar:
        calendar_details = api.read_csv()
        modified_columns = api.modify_table_columns(calendar_details)
        updated_table = api.add_remove_columns(modified_columns)
        api.append_csv(updated_table)

    if args_main.modify_table_columns:
        calendar_details = api.read_csv()
        modified_columns = api.modify_table_columns(calendar_details)
        updated_table = api.add_remove_columns(modified_columns)
        api.write_csv(updated_table)
    
    if args_main.monthly_activity:
        calendar_details = api.read_csv()
        api.monthly_activity_bar_chart(calendar_details)
    
    if args_main.average_meeting:
        calendar_details = api.read_csv()
        api.average_meeting_bar_chart(calendar_details)

    if args_main.time_stats:
        calendar_details = api.read_csv()
        api.time_stats(calendar_details)


if __name__ == '__main__':
    main()