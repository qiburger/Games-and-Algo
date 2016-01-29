__author__ = 'Qi_He'


class nim_game(object):
    def canWin(self, n):
        """
        :rtype : bool
        """
        if n == 1:
            return False
        if n == 2:
            return True
        if n == 3:
            return True
        return self.canWin(n-1) or self.canWin(n-2) or self.canWin(n-3)


tester = nim_game()
print tester.canWin(5)
