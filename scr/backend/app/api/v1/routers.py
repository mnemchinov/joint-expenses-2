from scr.backend.app.controllers import PartnerController, OrderController, \
    OrderPartnersController

from scr.backend.core.routers import RouterBase


class PartnerRouter(RouterBase):
    controller = PartnerController
    tags = ['Partners']
    path: str = 'partner'
    path_plural: str = 'partners'


class OrderRouter(RouterBase):
    controller = OrderController
    tags = ['Orders']
    path: str = 'order'
    path_plural: str = 'orders'


class OrderPartnersRouter(RouterBase):
    controller = OrderPartnersController
    tags = ['Order partners']
    path: str = 'order_partner'
    path_plural: str = 'order_partners'
