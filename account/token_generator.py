from datetime import date
from django.conf import settings
from django.utils.crypto import constant_time_compare, salted_hmac
from django.utils.http import base36_to_int, int_to_base36

class PasswordResetTokenGenerator:
    secret = settings.SECRET_KEY
    def make_token(self):

        return self._make_token_with_timestamp(self._num_days(self._today()))

    def check_token(self,token):

        if not token :

            return False

        try:

            ts_b36, hash = token.split("-")

        except ValueError:

            return False

        try:

            ts = base36_to_int(ts_b36)

        except ValueError:

            return False

        # Check that the timestamp/uid has not been tampered with

        if not constant_time_compare(self._make_token_with_timestamp(ts), token):

            return False



        # Check the timestamp is within limit. Timestamps are rounded to

        # midnight (server time) providing a resolution of only 1 day. If a

        # link is generated 5 minutes before midnight and used 6 minutes later,

        # that counts as 1 day. Therefore, PASSWORD_RESET_TIMEOUT_DAYS = 1 means

        # "at least 1 day, could be up to 2."

        if (self._num_days(self._today()) - ts) > 3:

            return False
        return True



    def _make_token_with_timestamp(self, timestamp):

        # timestamp is number of days since 2001-1-1.  Converted to

        # base 36, this gives us a 3 digit string until about 2121

        ts_b36 = int_to_base36(timestamp)


        hash = salted_hmac(
            2,
            self._make_hash_value(timestamp),

            secret=self.secret,

        ).hexdigest()[::2]

        return "%s-%s" % (ts_b36, hash)



    def _make_hash_value(self, timestamp):

        # Ensure results are consistent across DB backends



        return str(timestamp)



    def _num_days(self, dt):

        return (dt - date(2001, 1, 1)).days



    def _today(self):

        # Used for mocking in tests

        return date.today()


modified_token_generator = PasswordResetTokenGenerator()