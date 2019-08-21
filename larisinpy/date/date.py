
import datetime
import pytz

from dateutil import tz

class DateUtils(object):

    def __init__(self):
        pass

    def utcnow(self):
        """
            Generate current time in UTC ISO8601

            Return:
                - UTC with format YYYY-mm-dd'T'HH:MM:SS.DDDZ
        """
        return datetime.datetime.utcnow().strftime(
            "%Y-%m-%dT%H:%M:%S.%f")[:-3]+"Z"

    def to_utc(self, date, timezone="Asia/Jakarta"):

        local = pytz.timezone(timezone)

        try:
            # 2019-07-31T11:08:22Z
            if date[19] == "Z" and date[16] == ":":
                
                return date[:19] + ".000Z"
        except:
            pass

        try:
            # 2019-07-31T11:08:22.566Z
            if date[23] == "Z" and date[19] == "." and date[10] == "T":
                
                return date
        except:
            pass
        
        try:
            # 2019-07-31T11:08:22.566
            if len(date) == 23 and date[19] == "." and date[10] == "T":
                
                return date
        except:
            pass
        
        try:
            # 2019-07-31 11:08:22.566724 # 2019-07-18 22:33:06.45200890
            if len(date) == 26 and date[10] == " ":

                date = datetime.datetime.strptime(date, '%Y-%m-%d %H:%M:%S.%f')
                local_dt = local.localize(date, is_dst=None)
                utc_dt = local_dt.astimezone(pytz.utc)

                return utc_dt.strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3]+"Z"
        except:
            pass

        try:
            if len(date) == 26 and date[10] == "T":

                date = datetime.datetime.strptime(date, '%Y-%m-%dT%H:%M:%S.%f')
                local_dt = local.localize(date, is_dst=None)
                utc_dt = local_dt.astimezone(pytz.utc)

                return utc_dt.strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3]+"Z"
        except:
            pass

        try:
            # 2019-07-31T11:08:22.566724Z
            if date[26] == "Z" and date[10] == "T":

                return date[:23] + "Z"
        except:
            pass

        print("Format undetectable: {}".format(date))
        return date

    def to_local(self, date, timezone='Asia/Jakarta'):
        """
            Convert UTC date to Asia/Jakarta Time for Reporting
        """
        
        # Check UTC or not
        if date[-1] == "Z":

            from_zone = tz.gettz('UTC')
            to_zone = tz.gettz('Asia/Jakarta')

            # Format 2019-08-12T07:54:37.507221Z and 2019-08-12T07:54:37.507Z
            utc = datetime.datetime.strptime(date, '%Y-%m-%dT%H:%M:%S.%fZ')
            utc = utc.replace(tzinfo=from_zone)
            
            return utc.astimezone(to_zone).strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3]
        
        else:
            if len(date) == 26:
                # 2019-08-12T07:38:59.705119
                return date[:-3]
            
            else:
                return date
