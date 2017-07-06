from crudbuilder.abstract import BaseCrudBuilder
from updates.models import Instance


class InstanceCrud(BaseCrudBuilder):
    model = Instance
    search_fields = ['state_code', 'architecture', 'type', 'ip_address', 'name', 'monitored', 'launched', 'placement', 'private_dns', 'public_dns']
    tables2_fields = ('name', 'type', 'launched', 'placement','ip_address', 'state_code', 'architecture', 'monitored', 'private_dns', 'public_dns')
    tables2_css_class = "table table-bordered table-condensed"
    tables2_pagination = 20  # default is 10
    modelform_excludes = []
    login_required = False
    permission_required = False

    custom_templates = {
        'list': 'instance_list.html'
    }

