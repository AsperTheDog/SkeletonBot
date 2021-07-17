from datetime import datetime, timedelta

from src.Modules.trigger import TriggerManager


@TriggerManager.triggerClass
class AtHour:
    def __init__(self, args):
        self.time = args['times']

    def check(self, data, variables):
        today = datetime.utcnow().replace(hour=0, minute=0, second=0, microsecond=0)
        now = datetime.utcnow()
        for time in self.times:
            if ((today + timedelta(seconds=time['time'])) - datetime.utcnow()).total_seconds() < 60 and datetime.utcnow().weekday() in time['wday']:
                return True
        return False

    def serialize(self):
        return {
            'id': AtHour.__name__,
            'args': {
                'times': [{'time': time['time'], 'wday': time['wday']} for time in self.times]
            }
        }
