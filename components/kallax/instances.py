"""Physical instances in the reviewed nominal assembly, in millimetres."""
def define_instances(**kwargs):
    records = []
    for row, tall, cy in [("front", False, 0), ("rear", True, 187)]:
        z = 112 if tall else 37
        a = -167.505
        def add(name, part, pos, reverse=False):
            records.append(dict(name=row+'_'+name, part=part, pos=pos, reverse=reverse))
        for i, x in enumerate([0, 108.67, 185.34, 335.01], 1):
            add('frame_'+str(i), 'P2' if tall else 'P1', [a+x, cy, 59.5 if tall else 22], i==4)
        for j, y in enumerate([cy-67.5, cy+67.5]):
            add('rod_'+str(j), 'H1', [a+150,y,z])
            add('fixed_'+str(j), 'H2', [a+2.5,y,z])
            add('long_first_'+str(j), 'P3', [a+9,y,z])
            add('centre_'+str(j), 'P4', [a+117.67,y,z])
            add('long_last_'+str(j), 'P3', [a+294.01,y,z], True)
            add('housing_'+str(j), 'P5', [a+294.01,y,z])
            add('coupling_'+str(j), 'H3', [a+303.01,y,z])
            add('clip_'+str(j), 'P7', [a+312.01,y,z])
            add('nut_cover_'+str(j), 'P6', [a+319.01,y,z])
            add('retaining_'+str(j), 'H2', [a+323.51,y,z])
            add('bolt_'+str(j), 'H4', [a+330.01,y,z])
    return records
