from srb.models import Interval
from django.test import TestCase
from django.core.urlresolvers import reverse

class IntDetailTests(TestCase):
    def create_interval(NeatName,start,stop):
        return Interval.objects.create(NeatName=NeatName, chr=chr,start=start,stop=stop)
    def test_home_page_no_intervals(self):
        response = self.client.get(reverse('interval'))
        self.assertEquals(response.status_code,200)
        self.assertContains(response,"404")
        self.assertQueryEqual(response.context['IntervalDetailView'],[])
        
    # def test_get_table_data(self):
    #     no_table_data=create_interval()
