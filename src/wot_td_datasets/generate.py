import os
from enum import IntFlag

from wot_td_datasets.things.custom import (
    allarm_control_panel,
    binary_window_contact,
    button,
    doorbell,
    ev,
    ev_charger,
    fan,
    humidifier,
    hvac,
    illuminance_sensor,
    lawn_mower,
    light_rgb,
    light_simple,
    lock,
    meter_flat,
    meter_nested,
    pv_inverter,
    pv_panel,
    siren,
    switch,
    tracker,
    vacuum,
    window_cover,
)
from wot_td_datasets.things.kinder import (
    AirConditioner,
    Alarm,
    AmbientLightstrip,
    BedsideLamp,
    CoffeeMachine,
    Counter,
    Dehumidifier,
    Dishwasher,
    Display,
    Dryer,
    ExteriorLight,
    FoodDispenser,
    Kettle,
    Microwave,
    Oven,
    PopcornMaker,
    SecurityCamera,
    SmartHeater,
    SmartLock,
    SmartRadioDevice,
    SmartSpeaker,
    SmartTV,
    Sprinkler,
    Stove,
    Streamingdrone,
    VacuumRobot,
    Ventilator,
)
from wot_td_datasets.things.web_things import (
    wt_air_quality_sensor,
    wt_alarm,
    wt_barometric_pressure_sensor,
    wt_binary_sensor,
    wt_camera,
    wt_color_control,
    wt_color_sensor,
    wt_dimmable_color_light,
    wt_dimmable_light,
    wt_door_sensor,
    wt_energy_monitor,
    wt_humidity_sensor,
    wt_leak_sensor,
    wt_lock,
    wt_motion_sensor,
    wt_multi_level_sensor,
    wt_multi_level_switch,
    wt_on_off_color_light,
    wt_on_off_color_temperature_light,
    wt_on_off_light,
    wt_on_off_switch,
    wt_push_button,
    wt_smoke_sensor,
    wt_temperature_sensor,
    wt_thermostat,
    wt_video_camera,
)

things_list_custom = [
    allarm_control_panel,
    binary_window_contact,
    button,
    doorbell,
    ev,
    ev_charger,
    fan,
    humidifier,
    hvac,
    illuminance_sensor,
    lawn_mower,
    light_rgb,
    light_simple,
    lock,
    meter_flat,
    meter_nested,
    pv_inverter,
    pv_panel,
    siren,
    switch,
    tracker,
    vacuum,
    window_cover,
]

things_list_web_things = [
    wt_air_quality_sensor,
    wt_alarm,
    wt_barometric_pressure_sensor,
    wt_binary_sensor,
    wt_camera,
    wt_color_control,
    wt_color_sensor,
    wt_dimmable_color_light,
    wt_dimmable_light,
    wt_door_sensor,
    wt_energy_monitor,
    wt_humidity_sensor,
    wt_leak_sensor,
    wt_lock,
    wt_motion_sensor,
    wt_multi_level_sensor,
    wt_multi_level_switch,
    wt_on_off_color_light,
    wt_on_off_color_temperature_light,
    wt_on_off_light,
    wt_on_off_switch,
    wt_push_button,
    wt_smoke_sensor,
    wt_temperature_sensor,
    wt_thermostat,
    wt_video_camera,
]

things_list_kinder = [
    AirConditioner,
    Alarm,
    AmbientLightstrip,
    BedsideLamp,
    CoffeeMachine,
    Counter,
    Dehumidifier,
    Dishwasher,
    Display,
    Dryer,
    ExteriorLight,
    FoodDispenser,
    Kettle,
    Microwave,
    Oven,
    PopcornMaker,
    SecurityCamera,
    SmartHeater,
    SmartLock,
    SmartRadioDevice,
    SmartSpeaker,
    SmartTV,
    Sprinkler,
    Stove,
    Streamingdrone,
    VacuumRobot,
    Ventilator,
]


class DataSets(IntFlag):
    CUSTOM = 1
    WEB_THINGS = 2
    KINDER = 4


_things_list = things_list_custom + things_list_web_things + things_list_kinder

_things_dict = {
    DataSets.CUSTOM: things_list_custom,
    DataSets.WEB_THINGS: things_list_web_things,
    DataSets.KINDER: things_list_kinder,
}


def td_datasets(selection: DataSets):
    ds = []
    for dataset in selection:
        ds.extend(_things_dict[dataset])
    return ds


def generate_tds():
    count = 0
    for thing in _things_list:
        td = thing.td()

        if not os.path.exists("tds"):
            os.mkdir("tds")
        for i in range(0, 1):
            with open(f"tds/TD_{count}_{td.type}_{i}.json", "w") as td_file:
                td_content = td.model_dump_json(
                    exclude_none=True,
                    by_alias=True,
                    indent=2,
                    exclude={"properties": {"*": "title"}},
                )
                td_file.write(td_content)
        count += 1
    print(f"Generated {len(_things_list)} TDs")


if __name__ == "__main__":
    generate_tds()
