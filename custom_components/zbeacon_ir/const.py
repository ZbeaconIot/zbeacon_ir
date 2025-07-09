
from homeassistant.const import Platform

DOMAIN = "zbeacon_ir"

PLATFORMS = [
    Platform.BUTTON,
    Platform.CLIMATE,
    Platform.SENSOR,
]

ZBEACON_DISCOVERY_TOPIC = "Zbeacon/discovery/+/config"

ZBEACON_IR_EVENT_DEVICE_MSG = "zbeacon_ir_device_msg"
ZBEACON_IR_EVENT_DEVICE_NEW = "zbeacon_ir_device_new"
