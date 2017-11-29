# -*- coding: utf-8 -*-
"""
Created on Sun Jul 23 00:12:28 2017

@author: Leszek
"""
# Testowanie klasy AnonymousSurvey
import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """Testy dla klasy AnonymousSurvey."""
    
    def test_store_single_response(self):
        """Sprawdzenie, czy pojedyncza odpowiedź jest prawidłowo
        przechowywana."""
        question = "Jaki jest Twoj ojczysty język?"
        my_survey = AnonymousSurvey(question)
        my_survey.store_response('angielski')
        
        self.assertIn('angielski', my_survey.responses)
        
    def test_store_three_responses(self):
        """Sprawdzenie, czy trzy pojedyncze odpowiedzi są prawidłowo
        przechowywane."""
        question = "Jaki jest Twoj ojczysty język?"
        my_survey = AnonymousSurvey(question)
        responses = ['angielski', 'hiszpański', 'polski']
        for response in responses:
            my_survey.store_response(response)
            
        for response in responses:
            self.assertIn(response, my_survey.responses)
        
unittest.main()