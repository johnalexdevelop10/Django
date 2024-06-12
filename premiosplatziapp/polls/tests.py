import datetime

from django.test import TestCase
from django.utils import timezone
from .models import Question
from django.urls.base import reverse
class QuestionModelTest(TestCase):
    
    def test_was_published_recently_with_future_questions(self):
        """was_published_recently returns False for questions whose pub_date is in the future """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(question_text="¿Quine es el mejor Course Director de platzi?",pub_date=time)
        self.assertIs(future_question.was_published_recently(),False)
        
    class QuestionIndexViewTests(TestCase):
     def test_no_cuestions(self):
         """if no question exist, an appropiate message is displayed"""
         response = self.client.get(reverse("polls:index"))
         self.assertEqual(response.status_code,200)
         self.assertContains(response,"no polls are available.")
         self.assertQuerySetEqual(response.content["latest_question_list"],[])
   

    