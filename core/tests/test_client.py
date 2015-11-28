from core.tests.utils import *
from core.models import *


class ClientTestCase(WagtailTest):

    def setUp(self):
        super(ClientTestCase, self).setUp()

    def testHomePage(self):
        home_page = HomePage.objects.all()[0]
        response = self.client.get(home_page.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, home_page.template)
