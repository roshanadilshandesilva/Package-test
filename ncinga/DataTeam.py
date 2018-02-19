class DataTeam:
    def __init__(self):
        ''' Constructor for this class. '''
        # Create some members
        self.members = ['Isura', 'Deshika', 'Rashini','Roshana']

    def printMembers(self):
        print('Printing members of the Data Team')
        for member in self.members:
            print('\t%s ' % member)