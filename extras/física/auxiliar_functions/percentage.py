def remove_percentage(percentage, total):
    value_removed = total - (total/100) * percentage
    
    return value_removed