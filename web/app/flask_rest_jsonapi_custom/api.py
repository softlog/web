from flask_rest_jsonapi.api import Api


class Api(Api):


    def permission_manager(self, permission_manager):
        """Use permission manager to enable permission for API

        :param callable permission_manager: the permission manager
        """
        self.check_permissions = permission_manager
        #print("Entrei aqui", len(self.resource_registry))
        for resource in self.resource_registry:
            #print(getattr(resource, 'disable_permission', None))
            if getattr(resource, 'disable_permission', None) is not True:
                  			
                for method in getattr(resource, 'methods', ('GET', 'POST', 'PATCH', 'DELETE')):
                    try:
                        setattr(resource,
								method.lower(),
								self.has_permission()(getattr(resource, method.lower())))
                    except:
                        pass
