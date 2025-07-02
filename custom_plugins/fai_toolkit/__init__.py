''' RotorHazard FAI Toolkit '''

from eventmanager import Evt
from RHUI import UIField, UIFieldType, UIFieldSelectOption
    
def initialize(rhapi):
    fields = rhapi.fields
    ui = rhapi.ui
    fields.register_pilot_attribute( UIField('fainumber', "FAI Number", UIFieldType.TEXT) )
    fields.register_pilot_attribute( UIField('safetycheck', "Safety Checked", UIFieldType.CHECKBOX) )
