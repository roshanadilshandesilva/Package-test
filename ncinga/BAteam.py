class BAteam:
    def __init__(self):
        ''' Constructor for this class. '''
        # Create some members
        self.members = ['Anuradha', 'Lahiru', 'Chan','Namal']

    def printMembers(self):
        print('Printing members of the BA team')
        for member in self.members:
            print('\t%s ' % member)