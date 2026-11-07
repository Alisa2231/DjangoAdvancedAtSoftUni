from django.contrib.auth.mixins import UserPassesTestMixin


class UserIsOwnerMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.id == self.get_object().id

class UserIsACoachMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.role == 'Coach'