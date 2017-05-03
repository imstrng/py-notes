def getCfg():
    if os.path.isfile('settings.json'):
        f = open("settings.json", "r")
        cfg = json.load(f)
        f.close()
    else:
        print('Using default configuration')
        cfg['VAR1'] = 'data1'
        cfg['VAR2'] = 'data2'
        cfg['VAR3'] = 'data3'
        putCfg(cfg)
    return cfg


def putCfg(cfg):
    f = open("settings.json", "w")
    f.write(json.dumps(cfg, indent=4, sort_keys=True))
    f.close()
