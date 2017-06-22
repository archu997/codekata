def workingDay(day):
    work=['monday','tuesday','wednesay','thursday','friday','saturday']
    if day in work:
        return True
    else:
        return False
day=raw_input("Enter a day")
day=day.lower()
print workingDay(day)
