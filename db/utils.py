from datetime import datetime

def none_to_empty(string):
    if string == "None":
        return ""
    return string

def create_proper_log(log_class, new_data_text, change_type):
    log_class.objects.create(changed_data=new_data_text, changed_date=datetime.now(), change_type=change_type)