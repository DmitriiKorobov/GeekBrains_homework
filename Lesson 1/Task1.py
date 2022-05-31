duration = int(input('Please enter duration'
                     ' in seconds to convert '))

if duration < 0:
    print('You entered a negative value', duration,
          '\nValue converted to a positive value', duration * (-1))

if duration < 60:
    print(duration, 'seconds')
elif 60 <= duration < 3600:
    print(duration // 60, 'minute',
          duration % 60, 'second')
elif 3600 <= duration < 86400:
    print(duration // 3600, 'hour',
          duration // 60 % 60, 'minute',
          duration % 60, 'second')
elif duration >= 86400:
    print(duration // 86400, 'day',
          duration // 3600 % 24, 'hour',
          duration // 60 % 60, 'minute',
          duration % 60, 'second')
