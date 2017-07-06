from django.conf import settings
import boto.ec2

class EC2:
    def __init__(self):
        self._regions = [u'ap-south-1', u'eu-west-2', u'eu-west-1', u'ap-northeast-2', u'ap-northeast-1', u'sa-east-1',
                    u'ca-central-1', u'ap-southeast-1', u'ap-southeast-2', u'eu-central-1', u'us-east-1', u'us-east-2',
                    u'us-west-1', u'us-west-2']
        self._ec2_connection = None
        self._access_key = settings.AWS_ACCESS_KEY
        self._secret_key = settings.AWS_SECRET_KEY

    def _get_region_instances(self, region):
        self._ec2_connection = boto.ec2.connect_to_region(region,
                aws_access_key_id=self._access_key,
                aws_secret_access_key=self._secret_key)
        return (reservation.instance for reservation in self._ec2_connection.get_all_reservations())



