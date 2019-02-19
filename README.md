# RESTful Raspberry Pi Switch Server for Home Assistant
An example RESTful GPIO server that is compatible with Home Assistant. This repository aims to provide you with a template to create your own programs to connect to the [REST switch component](https://www.home-assistant.io/components/switch.rest/) of the Home Assistant

# Quick Runthrough
This server supports operations outlined in the [REST switch component](https://www.home-assistant.io/components/switch.rest/):

- Querying state 
- Turning on
- Turning off

The functions that you should be concerned with are:

- fetchState()
- turnOn()
- turnOff()

Something you might do is to make it interact with a GPIO pin to control a physical device such as a relay. 

# Requirements
To develop this template on your computer, you need:

- Python 3
- Flask (`pip3 install flask`)

# Setting up on your Pi
Setting it up on a fresh install of Raspbian is supported in the provided install script. Simply `cd` to the root of this repository on your Raspberry Pi and run the `install.sh`.

# Connect to Home Assistant
Add this to the configuration file of your Home Assistant:
```yaml
switch:
  - platform: rest
    resource: http://IP_ADDRESS/led_endpoint
    body_on: '{"active": "true"}'
    body_off: '{"active": "false"}'
    is_on_template: '{{ value_json.is_active }}'
    headers:
      Content-Type: application/json
    verify_ssl: true