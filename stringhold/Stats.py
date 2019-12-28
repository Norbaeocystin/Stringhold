'''
date: December 2019
purpose: classes to help with scraping tasks
version: 1.0.0
doctest: python3 Stats.py -v
'''
import re

class Stats():
    
    def get_alpha_ratio(self, string):
        """Example function with types documented in the docstring.

        Returns ratio in percents of latin letters in string

        Parameters
        ----------
        string : str
            string to be checked.

        Returns
        -------
        float
            percent of ascii characters in string.
        
        Examples
        --------
        >>> stats.get_alpha_ratio('string')
        100.0
        >>> stats.get_alpha_ratio('Acta Non Verba.')
        80.0
        >>> stats.get_alpha_ratio('12345')
        0.0
        """
        length = len(string)
        residue = re.sub('[a-zA-Z]','',string)
        residue_length = len(residue)
        return ((length - residue_length)/length)*100
    
    def get_digit_ratio(self, string):
        """

        Returns ratio in percents of digit letters in string

        Parameters
        ----------
        string : str
            string to be checked.

        Returns
        -------
        float
            percent of digit characters in string.
        
        Examples
        --------
        >>> stats.get_digit_ratio('string')
        0.0
        >>> stats.get_digit_ratio('1. Acta Non Verba.')
        5.555555555555555
        >>> stats.get_digit_ratio('12345')
        100.0
        """
        length = len(string)
        residue = re.sub('[0-9]','',string)
        residue_length = len(residue)
        return ((length - residue_length)/length)*100
    
    def get_ascii_ratio(self, string):
        """

        Returns ratio in percents of ascii ( 7 bits) characters in string

        Parameters
        ----------
        string : str
            string to be checked.

        Returns
        -------
        float
            percent of ascii characters in string.
        
        Examples
        --------
        >>> stats.get_ascii_ratio('string')
        100.0
        >>> stats.get_ascii_ratio('Câ\x82\x81â\x82\x85Hâ\x82\x82â\x82\x84O')
        20.0
        >>> stats.get_ascii_ratio('https://www.oglaf.com/brimstone-vinegar/')
        100.0
        """
        length = len(string)
        ascii_length = len([True for item in string if ord(item) < 128])
        return (ascii_length/length)*100
    
if __name__ == "__main__":
    import doctest
    doctest.testmod(extraglobs={'stats': Stats()})