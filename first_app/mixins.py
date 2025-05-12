from django.contrib.auth.mixins import UserPassesTestMixin
from first_app.my_utils import is_user_superuser



class UserIsAdminMixin (UserPassesTestMixin):

    def test_func(self):
        return self.request.user.is_superuser