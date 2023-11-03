# import bibliothec
from openpyxl import Workbook
import pandas as pd

# dimension from pl homologation


def norm_dimension_pl(total_length=16500, king_to_rear=12000):
    return ["L_max", total_length, 0], ["L_frame", king_to_rear, 0]

# load from pl homologation


def norm_load_pl(dmc=40, axis_3=24):
    dmc = ["dmc", 0, dmc]
    axis = ["max_load_axis", 0, axis_3]
    return dmc, axis

# file:///C:/Users/Marek/Documents/301_143_L_STARKOWSKI_3.pdf


class TractorUnit:
    def __init__(self, asix_a, load_a, asix_b, load_b, saddle, length):
        # first axis
        self.asix_a = asix_a
        self.load_a = load_a
        self.asix_b = asix_b
        self.load_b = load_b
        self.saddle = saddle
        self.legth = length

    def matrix(self):
        r_a = ["Ra", self.asix_a, self.load_a]
        r_b = ["Rb", self.asix_b, self.load_b]
        return r_a, r_b


class SemiTrailer:
    def __init__(self, king_pin, axies, axies_load, body_load, body_load_x,
                 frame_load, frame_load_x, length):
        self.king_pin = king_pin
        self.axies = axies
        self.axies_load = axies_load
        self.body_load = body_load
        self.body_load_x = body_load_x
        self.frame_load = frame_load
        self.frame_load_x = frame_load_x
        self.length = length

    def matrix_frame(self):
        r_c = ["Rc", self.king_pin, 0]
        r_d = ["Rd", self.axies, self.axies_load]
        r_e = ["Re", self.body_load, self.body_load_x]
        r_f = ["Rf", self.frame_load, self.frame_load_x]
        length = ["L", self.length, 0]
        return r_c, r_d, r_e, r_f, length


class Load:

    i = 64

    def __init__(self, x, load):
        Load.i = Load.i + 1
        self.x = x
        self.load = load

    def force(self):
        f = [chr(Load.i), self.load, self.x]
        return f
    # def __str__ (self):
    #    f = [chr(Load.i), self.x, self.load]
    #    return f

#norm_dimension_pl= input("sdfsdf")
#norm_load_pl= input("sdfsdf")

#for class TractorUnit:
'''
asix_a= int(input("asix_a_tractorunit-->"))
load_a= int(input("load_a_tractorunit-->"))
asix_b= int(input("asix_b_tractorunit-->"))
load_b= int(input("load_b_tractorunit-->"))
saddle= int(input("saddle_tractorunit-->"))
length= int(input("length_tractorunit-->"))
'''
#for class TractorUnit: RANDOM VALUE!
asix_a= -3150
load_a=4885
asix_b= -1220
load_b=1725
saddle= - 500
length=asix_a + asix_b

'''
#for class SemiTrailer:
king_pin= int(input("king_pin_semitrailer-->"))
axies= int(input("axies_semitrailer--->"))
axies_load= int(input("axies_load_semitrailer--->"))
body_load= int(input("body_load_semitrailer--->"))
body_load_x= int(input("body_load_x_semitrailer--->"))
frame_load= int(input("frame_load_semitrailer--->"))
frame_load_x= int(input("frame_load_x_semitrailer--->"))
length= int(input("length_semitrailer--->"))
'''

#for class SemiTrailer for EXAMPLE!!!
king_pin= 0
axies= 7700
axies_load= 2400
body_load= 3100
body_load_x= 5300
frame_load= 1600
frame_load_x= 5000
length= 10000

extra_loads = []
i = 0
while input("extra load = y, dismiss = n-->")== 'y':
  mass_of_load = int(input("mass_of_load_semitrailer--->"))
  mass_of_load_x = int(input("mass_of_load_x_semitrailer--->"))
  name = f'extra_load_+{i}'

  name = Load(mass_of_load, mass_of_load_x)
  name_force = name.force()
  extra_loads.append(name_force)
  i =i+ 1



#without load
#Ro = axies_load=, Rs = body_load=, Rr = frame_load=
#czop = 0 ,    R*Rox= Mo *Mox + Ms * Msx + Mr * Mrx
#R = ( Mo *Mox + Ms * Msx + Mr * Mrx)/R0x
R_axies = (axies * axies_load + body_load * body_load_x + frame_load * frame_load_x)/axies
print(f'osie bez ladunku = {int(R_axies)}')
#0 = R_king + axies_load + body_load + frame_load - R_axies
R_king = axies_load + body_load + frame_load - R_axies
print(f'czop bez ladunku = {int(R_king)}')
# legth homo
norm_dimension_pl_1 = norm_dimension_pl()
# print(norm_dimension_pl_1)

#with_load
#Ro = axies_load=, Rs = body_load=, Rr = frame_load=
#czop = 0 ,    R*Rox= Mo *Mox + Ms * Msx + Mr * Mrx+
#R = ( Mo *Mox + Ms * Msx + Mr * Mrx)/R0x

for added_load in extra_loads:
  R_axies = R_axies + (added_load[1]*added_load[2]//axies)


print(f'osie z ladunkiem = {int(R_axies)}')
#0 = R_king + axies_load + body_load + frame_load - R_axies
R_king = axies_load  + body_load  + frame_load - R_axies
for added_load in extra_loads:
  R_king = R_king + added_load[2]
print(f'czop z ladunkiem = {int(R_king)}')

R_king = ['R_king',0,R_king]
R_axies = ['R_axies',axies, R_axies]

# max load
dmc_0 = norm_load_pl()
axis_0 = norm_load_pl()[1]


# tractorUnit
tractorunit = TractorUnit(asix_a, load_a, asix_b, load_b, saddle, length)
matrix = tractorunit.matrix()

# semitrailer
frame_1 = SemiTrailer(king_pin, axies, axies_load, body_load, body_load_x,
                      frame_load, frame_load_x, length)
matrix_1 = frame_1.matrix_frame()

# extra force
#extra_load_0 = Load(mass_of_load, mass_of_load_x)


data = []
for cell in matrix_1:
    data.append(cell)
for cell in matrix:
    data.append(cell)
for cell in norm_dimension_pl_1:
    data.append(cell)
for cell in dmc_0:
    data.append(cell)
for cell in extra_loads:
    data.append(cell)
data.append(R_king)
data.append(R_axies)


df = pd.DataFrame(data=data, columns=['nazwa', 'polozenie', 'wartosc_sily'])
# df.reset_index(inplace=True)
#
#print(df)

wb = Workbook()
ws = wb.active
df.to_excel("nazwa_pliku.xlsx", index=False)
#wb.save("calculator_of_load.xlsx")
