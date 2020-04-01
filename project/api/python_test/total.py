class Total:
    def __init__(self, total_dict):
        """
        verify value
        """
        try:
            self.numbers_to_add = list(total_dict['list'])
        except TypeError:
            raise TypeError('It is not a list')

    def sum(self):
        """
        sum of numbers
        """
        result = dict()
        result['total'] = 0
        for i in self.numbers_to_add:
            result['total'] += i
        
        return result
