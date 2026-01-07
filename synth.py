const lpf_cutoff = slider(6300, 300, 8000, 2000)
stack(
  note("<[c3 e3 g3 b3] [c3 g3 e3 c3]>")
    .sound("piano")
    .room(0.8)
    .gain(0.7),

  note("<~ ~ [b4 ~ c5 ~] [d5 ~ e5 ~]>")
    .sound("piano")
    .room(0.8)
    .gain(0.7),

  sound("bd")
    .gain(0.5),

  sound("<[hh:5 ~ hh:8 ~ hh:5 ~ hh:8 ~]>")
    .gain(0.3)
    .lpf(lpf_cutoff)
    .pan(sine.slow(3))
    .room(0.6),

  note("<[e4,g4,b4] ~ [c4,e4,g4] ~>")
    .sound("triangle")
    .gain(0.2),
  
  note("<[c3 ~ ~ g2 ~ b3 ~ ~]>")
    .sound("sawtooth")
    .gain(0.25)
    .lpf(15000)
    .room(0.9),
)
