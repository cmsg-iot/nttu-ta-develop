state = {
    'data': {
        'pressure_in': 0.0,
        'pressure_out': 0.0,
        'temp': 0.0,
        'hum': 0.0,
        'hx711': 0.0,
        'mq2_smoke': 0,
        'mq2_LPG': 0,
        'mq2_methane': 0,
        'mq2_hydrogen': 0,
        'mq2_2_smoke': 0,
        'mq2_2_LPG': 0,
        'mq2_2_methane': 0,
        'mq2_2_hydrogen': 0,
        'mq7': 0,
        'hall': 0,
        'buzzer': 0,
        'heater': 0,
        'valveOpen': 0,
        'valveClose': 0,
        'valveState': 0
    },
    'config': {
        'pressure_in': {
            'shift': 0,
            'radial': 1.0
        },
        'pressure_out': {
            'shift': 0,
            'radial': 1.0
        },
        'hx711': {
            'ch': 0,
            'shift': 0,
            'radial': 1.0
        }
    },
    'rules': {},
    'uart': None,
    'message': "",
    'log': False,
    'isConfigUpdate': False
}
