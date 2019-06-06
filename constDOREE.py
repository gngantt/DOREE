'''
DOREE - Gabby Gantt, Jacob Lebreux, Janine Thomas

This file is used to receive the programmed warning and ready levels for DOREE

CRIT - the critical level where, when reached, DOREE will abort mission to go
charge her battery
WARN - the warning level where, when reached, DOREE will warn navigation to
get ready to go charge her battery
READY - the ready level where, when reached, DOREE will need to stop charging
and continue with her mission
'''

okay = False

while not okay:
    CRIT = float(input('Please enter the desired critical level: '))
    WARN = float(input('Please enter the desired warning level: '))
    READY = float(input('Please enter the desired ready level: '))

    print('The critical level for DOREE is ', CRIT)
    print('The warning level for DOREE is ', WARN)
    print('The ready level for DOREE is ', READY)

    question = input('\nIs this okay? (Y/N): ')

    okay = True if ((question == 'Y') or (question == 'y')) else False

print('Critical, Warning, and Ready levels have been set!\n')
