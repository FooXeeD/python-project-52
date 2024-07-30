
from django.test import TestCase, Client

from task_manager.test_help import load_data, remove_rollbar, test_english
from task_manager.statuses.models import Status
from task_manager.users.models import User


@remove_rollbar
@test_english
class StatusTestCase(TestCase):
    fixtures = ['user.json', 'status.json']
    test_status = load_data('test_status.json')

    def setUp(self) -> None:
        self.client = Client()

        self.status1 = Status.objects.get(pk=1)
        self.status2 = Status.objects.get(pk=2)
        self.status3 = Status.objects.get(pk=3)
        self.statuses = Status.objects.all()
        self.count = Status.objects.count()

        self.user1 = User.objects.get(pk=1)

        self.client.force_login(self.user1)
