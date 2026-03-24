# Introduction

This repository holds the 76 test Thing Descriptions (TDs) used by the paper [“Utilizing Large Language Models for Log-Based Automated Thing Description Generation”](https://ebooks.iospress.nl/doi/10.3233/SSW250014) published at the SEMANTICS 2025 conference.
The TDs are example of MQTT IoT devices that may be found in a Local Energy Community.

# Basic Usage

It is recommended to us [poetry](https://python-poetry.org) and the `pyproject.toml` file to install the dependencies of this project.

```bash
poetry install
```

To generate the TDs run:

```bash
poetry run python src/td_generator/generate.py
```

To generate the mock message logs run:

```bash
poetry run python src/td_generator/mock.py
```

# Datasets

The repository consists of three different datasets:

1. Custom (TDs created by use)
2. Kinder et. al
3. W3C WebThings

See the sections below for full sources.

## Custom Dataset

The `things` module holds all our reference TD.

For General inspiration, we consulted the following sources.

| Project                        | Link                                                                           |
| ------------------------------ | ------------------------------------------------------------------------------ |
| HomeAssistant Integration      | https://www.home-assistant.io/integrations/                                    |
| EVCC documentation             | https://evcc.io                                                                |
| SmartDataModels                | https://smartdatamodels.org                                                    |
| WoT TD Specification           | https://www.w3.org/TR/wot-thing-description11/                                 |
| WoT MQTT Binding Specification | https://w3c.github.io/wot-binding-templates/bindings/protocols/mqtt/index.html |
| Eclipse ThingWeb               | https://thingweb.io                                                            |
| Wikipedia SAE J1772 Article    | https://en.wikipedia.org/wiki/SAE_J1772                                        |
| WebThings                      | https://webthings.io                                                           |
| Tasmota                        | https://github.com/arendst/Tasmota                                             |

See the table below to see what was the primary source of inspiration for each TD.

| Thing Description        | Main source of inspiration                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Alarm Control Panel      | https://www.home-assistant.io/integrations/alarm_control_panel.mqtt/                                                                                                                                                                                                                                                                                                                                                                                                               |
| Alarm Siren              | https://www.home-assistant.io/integrations/siren.mqtt/                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Binary Window Contact    | https://www.home-assistant.io/integrations/binary_sensor.mqtt/                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Button                   | https://www.home-assistant.io/integrations/button.mqtt/                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Ceiling Fan              | https://www.home-assistant.io/integrations/fan.mqtt/                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Door Lock                | https://www.home-assistant.io/integrations/lock.mqtt/                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Doorbell                 | N/A                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Electric Vehicle         | https://docs.evcc.io/docs/devices/vehicles                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Electric Vehicle Charger | https://docs.evcc.io/docs/devices/chargers                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Humidifier               | https://www.home-assistant.io/integrations/humidifier.mqtt/                                                                                                                                                                                                                                                                                                                                                                                                                        |
| HVAC Unit                | https://www.home-assistant.io/integrations/climate.mqtt/                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Illuminance Sensor       | https://w3c.github.io/wot-binding-templates/bindings/protocols/mqtt/index.html#conformance, <br/>https://www.w3.org/TR/wot-thing-description11/#example-69                                                                                                                                                                                                                                                                                                                         |
| Lawn Mower               | https://www.home-assistant.io/integrations/lawn_mower.mqtt/                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Lightbulb (RGB)          | https://www.home-assistant.io/integrations/light.mqtt/, <br/>https://www.w3.org/TR/wot-thing-description11/                                                                                                                                                                                                                                                                                                                                                                        |
| Lightbulb (Single Color) | https://www.home-assistant.io/integrations/light.mqtt/, <br/>https://www.w3.org/TR/wot-thing-description11/                                                                                                                                                                                                                                                                                                                                                                        |
| Location Tracker (GPS)   | https://www.home-assistant.io/integrations/device_tracker.mqtt/                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Photovoltaic Inverter    | https://github.com/smart-data-models/dataModel.GreenEnergy/tree/master/PhotovoltaicMeasurement, <br/>https://swagger.lab.fiware.org/?url=https://smart-data-models.github.io/dataModel.GreenEnergy/PhotovoltaicDevice/swagger.yaml, <br/>https://swagger.lab.fiware.org/?url=https://smart-data-models.github.io/dataModel.S4BLDG/SolarDevice/swagger.yaml, <br/>https://swagger.lab.fiware.org/?url=https://smart-data-models.github.io/dataModel.Energy/SolarEnergy/swagger.yaml |
| Photovoltaic Panel       | https://github.com/smart-data-models/dataModel.GreenEnergy/tree/master/PhotovoltaicMeasurement, <br/>https://swagger.lab.fiware.org/?url=https://smart-data-models.github.io/dataModel.GreenEnergy/PhotovoltaicDevice/swagger.yaml, <br/>https://swagger.lab.fiware.org/?url=https://smart-data-models.github.io/dataModel.S4BLDG/SolarDevice/swagger.yaml, <br/>https://swagger.lab.fiware.org/?url=https://smart-data-models.github.io/dataModel.Energy/SolarEnergy/swagger.yaml |
| Smart Meter              | https://docs.evcc.io/docs/devices/meters                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Switch                   | https://www.home-assistant.io/integrations/switch.mqtt/                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Vacuum Cleaner           | https://www.home-assistant.io/integrations/vacuum.mqtt/                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Window Cover             | https://www.home-assistant.io/integrations/cover.mqtt/                                                                                                                                                                                                                                                                                                                                                                                                                             |

See the table down below to see which licenses these projects use.

| Project                        | License                                                       |
| ------------------------------ | ------------------------------------------------------------- |
| HomeAssistant Integration      | Attribution-NonCommercial-ShareAlike 4.0 International        |
| EVCC documentation             | MIT License                                                   |
| SmartDataModels                | Creative Commons Attribution 4.0 International Public License |
| WoT TD Specification           | Software and Document license - 2023 version                  |
| WoT MQTT Binding Specification | Software and Document license - 2015 version                  |

## W3C WebThings Dataset

[Source](https://github.com/w3c/wot-testing/tree/037c8d686ad8c145dd4fe01c2123ad26eca0e185/data/input_2022/TD/WebThings)

Changes:

- Removed non-devices and demo TD
- Changed the `href` to `mqv:topic`
- Added enum values to some string attributes
- Added missing descriptions
- Removed any reference to being a virtual device
- Deleted double entries (smart plug) etc

License: Unspecified, presumably Software and Document license - 2023 version

## Kinder et. al Dataset

[Source](https://gitlab.kit.edu/lukas.kinder/plannning_with_thing_descriptions_akr3/-/tree/main/WoT-TD?ref_type=heads)

Changes:

- Converted to MQTT topics
- Added some missing descriptions
- Removed Automated Warehouse as not in our domain
- Removed Chiller no forms data
- Naturally extended topics and made them unique
  - i.e., boolean properties with `is_` or `_enabled`, `_full`, `has_`
  - Boolean and non-boolean: extended by affordance name
- Added missing titles
- Removed redDotImage from counter-
- Unified affordance titles (e.g., Smart Display)

License: Lukas Kinder
