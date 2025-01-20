from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
import secrets

# Create your models here.

class ElectionOfficer(models.Model):
    register_no = models.IntegerField()
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=255, unique=True)
    phone_number = models.CharField(max_length=15, unique=True)
    address = models.TextField()
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    
# class Election(models.Model):
#     regno=models.IntegerField()
#     election_name = models.CharField(max_length=200)
#     description = models.TextField(blank=True, null=True)
#     start_date = models.DateTimeField()
#     end_date = models.DateTimeField()
#     is_active = models.CharField(max_length=20,choices=choice)
    
# class Candidate(models.Model):
#     election = models.ForeignKey(Election, on_delete=models.CASCADE)
#     full_name = models.CharField(max_length=200)
#     party_name = models.CharField(max_length=200, blank=True, null=True)
#     bio = models.TextField(blank=True, null=True)

class Poll(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    pub_date = models.DateTimeField(default=timezone.now)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def user_can_vote(self, user):
        """ 
        Return False if user already voted
        """
        user_votes = user.vote_set.all()
        qs = user_votes.filter(poll=self)
        if qs.exists():
            return False
        return True

    @property
    def get_vote_count(self):
        return self.vote_set.count()

    def get_result_dict(self):
        res = []
        for choice in self.choice_set.all():
            d = {}
            alert_class = ['primary', 'secondary', 'success',
                           'danger', 'dark', 'warning', 'info']

            d['alert_class'] = secrets.choice(alert_class)
            d['text'] = choice.choice_text
            d['num_votes'] = choice.get_vote_count
            if not self.get_vote_count:
                d['percentage'] = 0
            else:
                d['percentage'] = (choice.get_vote_count /
                                   self.get_vote_count)*100

            res.append(d)
        return res

    def __str__(self):
        return self.text


class Choice(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def get_vote_count(self):
        return self.vote_set.count()

    def __str__(self):
        return f"{self.poll.text[:25]} - {self.choice_text[:25]}"


class Vote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.poll.text[:15]} - {self.choice.choice_text[:15]} - {self.user.username}'

    

