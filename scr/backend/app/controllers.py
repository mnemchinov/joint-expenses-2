from scr.backend.app.models import Partner, Order, OrderPartners

from scr.backend.core.controllers import ControllerBase


class PartnerController(ControllerBase):
    model = Partner


class OrderController(ControllerBase):
    model = Order


class OrderPartnersController(ControllerBase):
    model = OrderPartners
