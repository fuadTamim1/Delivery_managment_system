from datetime import datetime

def get_formatted_date(date):
    # Get the selected date and format it as "YYYY-MM-DD"
    selected_date = date
    formatted_date = selected_date.strftime("%Y-%m-%d")
    return formatted_date

def compare_dates(date1,date2):
    # Compare two dates and return True if date1 is before date2, False otherwise

    # Convert strings to datetime objects
    date1_obj = datetime.strptime(date1, "%Y-%m-%d")
    date2_obj = datetime.strptime(date2, "%Y-%m-%d")
    
    return date1_obj <= date2_obj 
    
    