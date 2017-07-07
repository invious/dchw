from django.conf import settings
import boto.ec2
import re
from updates.models import Instance, InstanceHistory
from dateutil import parser


class EC2:
    def __init__(self):
        self._regions = [u'us-east-1',
                         u'us-east-2',
                         u'us-west-1', u'us-west-2']
        self._ec2_connection = None
        self._access_key = settings.AWS_ACCESS_KEY
        self._secret_key = settings.AWS_SECRET_KEY

    def _get_region_instances(self, region):
        self._ec2_connection = boto.ec2.connect_to_region(region,
                                                          aws_access_key_id=self._access_key,
                                                          aws_secret_access_key=self._secret_key)
        return sum((list(reservation.instances) for reservation in self._ec2_connection.get_all_reservations()),
                   [])  # flatten list

    def update_db(self):
        updated_instances = []
        for region in self._regions:
            instances = self._get_region_instances(region)
            for i in instances:
                instance, created = Instance.objects.update_or_create(
                    id=int(''.join(re.findall('\d+', i.id))),
                    # Have to extract only digits for id due to bad design in crudbuilder. Would probably create fork of their project if had more time
                    defaults={
                        'name': i.key_name,
                        'type': i.instance_type,
                        'ip_address': i.ip_address,
                        'state_code': str(i.state_code),
                        'architecture': i.architecture,
                        'monitored': i.monitored,
                        'launched': parser.parse(i.launch_time),
                        'placement': i.placement,
                        'private_dns': i.private_dns_name,
                        'public_dns': i.public_dns_name,
                    }
                )
                if not created:
                    updated_instances.append(instance.private_dns)
        return updated_instances
