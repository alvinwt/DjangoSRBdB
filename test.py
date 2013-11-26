from srb.models import Interval
from django.test import TestCase
from django.core.urlresolvers import reverse

def create_interval(NeatName,start,stop):
    return Interval.objects.create(NeatName=NeatName, chr=chr,start=start,stop=stop)
class IntDetailTests(TestCase):
    def home_page_no_intervals(self):
        response = self.client.get(reverse('interval'))
        self.assertEquals(response.status_code,200)
        self.assertContains(response,"No intervals available")
        self.assertQueryEqual(response.context['IntervalDetailView'],[])
        
    # def test_get_table_data(self):
    #     no_table_data=create_interval()
