import datetime

calendar = True
DAYS = ('Poniedziałek','Wtorek','Środa','Czwartek','Piątek',
        'Sobota','Niedziela')
MONTHS = ('Styczeń','Luty','Marzec','Kwiecień','Maj','Czerwiec',
          'Lipiec','Siepień','Wrzesień','Październik','Listopad','Grudzień')
while calendar == True:
    print("Podaj rok:")
    response = input('>')

    if response.isdecimal() and int(response) > 0:
        year = int(response)
        break
    continue

while calendar == True:
    print("Podaj miesiąc w formacie od 1 do 12:")
    response = input('>')
    if not response.isdecimal():
        print("Błąd formatu. Podaj miesiąc w formacie od 1 do 12:")
        continue
    month = int(response)
    if 1 <= month <= 12:
        break

def getCalendarFor(year,month):
    calText = " "
    calText += ' ' * 34 + MONTHS[month - 1] + ' ' + str(year) + '\n'
    calText +='  Niediela  Poniedziałek  Wtorek   Środa      Czwartek    Piątek    Sobota \n'
    
    weekSeparator = ('+----------' * 7) + '+\n'
    blankRow =('|          ' * 7) + '|\n'
    currentDate = datetime.date(year,month,1)

    while currentDate.weekday() !=6:
        currentDate -= datetime.timedelta(days=1)
    while True:
        calText += weekSeparator
        dayNumberRow = ' '
        for i in range(7):
            dayNumberLabel = str(currentDate.day).rjust(2)
            dayNumberRow +='|' + dayNumberLabel + (' ' * 8)
            currentDate += datetime.timedelta(days=1)
        dayNumberRow += '|\n'
        calText += dayNumberRow
        for i in range(3):
            calText += blankRow
        if currentDate.month != month:
            break
    calText += weekSeparator
    return calText

calText = getCalendarFor(year,month)
print(calText)

calendarFilename = 'kalendarz{}_{}.txt'.format(year,month)
with open(calendarFilename, 'w') as fileObj:
    fileObj.write(calText)
print("Zapisano" + calendarFilename)

