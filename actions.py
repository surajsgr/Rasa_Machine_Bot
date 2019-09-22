from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_core.actions.action import Action
from rasa_core.events import SlotSet


class ActionMachine(Action):
    def name(self):
        return 'action_machine'

    def run(self, dispatcher, tracker, domain):
        import psycopg2
        # from apixu.client import ApixuClient
        # api_key = '3ffa98232f754912a5f105936181406'  # your apixu key
        # client = ApixuClient(api_key)
        from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


        conn = psycopg2.connect(host="0.0.0.0", user="postgres", password="12345", port="5434", dbname='test_db21')
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cursor = conn.cursor()

        psql = "SET datestyle = dmy;"
        cursor.execute(psql)
        loc = tracker.get_slot('machine')
        print("loc---->",loc)
        sql='''
        select count(*) from machine where lower(MACHINE_TYPE)
        ='{}'
        '''.format(loc)
        cursor.execute(sql)
        N=cursor.fetchall()

        # current = client.getCurrentWeather(q=loc)

        # country = current['location']['country']
        # city =2
        #  current['location']['name']
        # condition = current['current']['condition']['text']
        # temperature_c = current['current']['temp_c']
        # humidity = current['current']['humidity']
        # wind_mph = current['current']['wind_mph']


        response = """The total number of {} are {} """.format(
            loc,N)

        #
        dispatcher.utter_message(response)
        return [SlotSet('machine', loc)]

