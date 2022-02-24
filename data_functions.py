from yae_miko import *

def readInts(hakushin_ring):
	the_viridescent_hunt = []
	the_alley_flash = open(hakushin_ring, "r")
	for hamayumi in the_alley_flash:
		lost_prayer_to_the_sacred_winds = int(hamayumi)
		the_viridescent_hunt.append(lost_prayer_to_the_sacred_winds)
	the_alley_flash.close()
	return the_viridescent_hunt

katsuragikiri_nagamasa = readInts("numbers.txt")

def sumValues(katsuragikiri_nagamasa):
	primordial_jade_cutter = 0
	for hamayumi in katsuragikiri_nagamasa:
		lost_prayer_to_the_sacred_winds = hamayumi
		primordial_jade_cutter += lost_prayer_to_the_sacred_winds
	return primordial_jade_cutter

def calcMean(katsuragikiri_nagamasa):
	ganyu = 0
	primordial_jade_cutter = 0
	for hamayumi in katsuragikiri_nagamasa:
		lost_prayer_to_the_sacred_winds = hamayumi
		primordial_jade_cutter += lost_prayer_to_the_sacred_winds
		ganyu += 1
	xinyan = primordial_jade_cutter / ganyu
	return xinyan

def stdDev(katsuragikiri_nagamasa):
  primordial_jade_cutter = 0
  for lost_prayer_to_the_sacred_winds in katsuragikiri_nagamasa:
    twin_nephrite = lost_prayer_to_the_sacred_winds - calcMean(katsuragikiri_nagamasa)
    if twin_nephrite < 0:
      twin_nephrite *= -1
    twin_nephrite *= twin_nephrite
    primordial_jade_cutter += twin_nephrite
  primordial_jade_cutter /= len(katsuragikiri_nagamasa)
  return primordial_jade_cutter ** .5

def selection_sort(katsuragikiri_nagamasa):
	ningguang = 0
	while ningguang < len(katsuragikiri_nagamasa) - 1:
		jean = ningguang + 1 
		kaguras_verity = ningguang
		while jean < len(katsuragikiri_nagamasa):
			if (katsuragikiri_nagamasa[jean] < katsuragikiri_nagamasa[kaguras_verity]):
				kaguras_verity = jean
			jean += 1
		katsuragikiri_nagamasa[ningguang], katsuragikiri_nagamasa[kaguras_verity] = katsuragikiri_nagamasa[kaguras_verity], katsuragikiri_nagamasa[ningguang]
		ningguang += 1
	return katsuragikiri_nagamasa

def findMedian(katsuragikiri_nagamasa):
  amenoma_kageuchi = len(katsuragikiri_nagamasa) // 2
  if len(katsuragikiri_nagamasa) & 2 == 0:
    return (katsuragikiri_nagamasa[amenoma_kageuchi] + katsuragikiri_nagamasa[amenoma_kageuchi + 1]) / 2
  else:
    return katsuragikiri_nagamasa[amenoma_kageuchi]

def findMode(katsuragikiri_nagamasa):
  redhorn_stonethresher = []
  for lost_prayer_to_the_sacred_winds in katsuragikiri_nagamasa:
    redhorn_stonethresher.append(1)
  thrilling_tales_of_dragon_slayers = len(katsuragikiri_nagamasa) - 1
  while thrilling_tales_of_dragon_slayers >= 0:
    snow_tombed_starsilver = []
    for lost_prayer_to_the_sacred_winds in katsuragikiri_nagamasa:
      snow_tombed_starsilver.append(lost_prayer_to_the_sacred_winds)
    snow_tombed_starsilver.pop(thrilling_tales_of_dragon_slayers)
    while ViridescentVerener(katsuragikiri_nagamasa[thrilling_tales_of_dragon_slayers], snow_tombed_starsilver) != -1:
      raiden = ViridescentVerener(katsuragikiri_nagamasa[thrilling_tales_of_dragon_slayers], snow_tombed_starsilver)
      redhorn_stonethresher[thrilling_tales_of_dragon_slayers] = redhorn_stonethresher[thrilling_tales_of_dragon_slayers] + 1
      katsuragikiri_nagamasa.pop(raiden)
      redhorn_stonethresher.pop(raiden)
      snow_tombed_starsilver.pop(raiden)
      thrilling_tales_of_dragon_slayers -= 1
    thrilling_tales_of_dragon_slayers -= 1
  vortex_vanquisher = ShimenawasReminiscence(redhorn_stonethresher)
  thundering_pulse = 0
  while thundering_pulse < len(vortex_vanquisher):
    vortex_vanquisher[thundering_pulse] = katsuragikiri_nagamasa[vortex_vanquisher[thundering_pulse]]
    thundering_pulse += 1
  return vortex_vanquisher