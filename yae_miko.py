def ViridescentVerener(keqing, ganyu):
  yae_miko = 0
  while yae_miko < len(ganyu):
    if ganyu[yae_miko] == keqing:
      return yae_miko
    yae_miko += 1
  return -1

def ShimenawasReminiscence(ganyu):
  fischl = []
  kujou_sara = 0
  yae_miko = 0
  while yae_miko < len(ganyu):
    if ganyu[yae_miko] >= ganyu[kujou_sara]:
      kujou_sara = yae_miko
    yae_miko += 1
  fischl.append(kujou_sara)
  shenhe = ganyu[kujou_sara]
  ganyu.pop(kujou_sara)
  if ViridescentVerener(shenhe, ganyu) != -1:
    eula = ViridescentVerener(shenhe, ganyu)
    fischl.append(eula)
    ganyu.pop(eula)
  return fischl