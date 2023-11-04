# import bibliothec
from openpyxl import Workbook
import pandas as pd

# dimension from pl homologation


def norm_dimension_pl(total_length=16500, king_to_rear=12000):
    return ["L_max", total_length, 0], ["L_frame", king_to_rear, 0]

# load from pl homologation


def norm_load_pl(dmc=40000, axis_3=24000):
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
        r_d = ["Rd", self.axies_load, self.axies]
        r_e = ["Re", self.body_load_x, self.body_load]
        r_f = ["Rf", self.frame_load_x, self.frame_load]
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

# norm_dimension_pl= input("sdfsdf")
# norm_load_pl= input("sdfsdf")

# for class TractorUnit:


'''
asix_a= int(input("asix_a_tractorunit-->"))
load_a= int(input("load_a_tractorunit-->"))
asix_b= int(input("asix_b_tractorunit-->"))
load_b= int(input("load_b_tractorunit-->"))
saddle= int(input("saddle_tractorunit-->"))
length= int(input("length_tractorunit-->"))
'''


# for class TractorUnit: RANDOM VALUE!
asix_a_0 = -3150
load_a_0 = 4885
asix_b_0 = -1220
load_b_0 = 1725
saddle_0 = - 100
length_0 = asix_a_0 + asix_b_0

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

# for class SemiTrailer for EXAMPLE!!!
king_pin_0 = 0
axies_0 = 7700
axies_load_0 = 1950
body_load_0 = 3100
body_load_x_0 = 5300
frame_load_0 = 2050
frame_load_x_0 = 5000
length_frame_0 = 10000

extra_loads = []
i = 0
while input("extra load = y, dismiss = n-->") == 'y':
    mass_of_load = int(input("mass_of_load_semitrailer--->"))
    mass_of_load_x = int(input("mass_of_load_x_semitrailer--->"))

    name = Load(mass_of_load, mass_of_load_x)
    name_force = name.force()
    extra_loads.append(name_force)
    i = i + 1

# without load
# Ro = axies_load=, Rs = body_load=, Rr = frame_load=
# czop = 0 ,    R*Rox= Mo *Mox + Ms * Msx + Mr * Mrx
# R = ( Mo *Mox + Ms * Msx + Mr * Mrx)/R0x
R_axies_0 = (axies_0 * axies_load_0 + body_load_0 * body_load_x_0 + frame_load_0 * frame_load_x_0)/axies_0
print(f'osie bez ladunku = {int(R_axies_0)}')
# 0 = R_king + axies_load + body_load + frame_load - R_axies
R_king_0 = axies_load_0 + body_load_0 + frame_load_0 - R_axies_0
print(f'czop bez ladunku = {int(R_king_0)}')
# legth homo
norm_dimension_pl_1 = norm_dimension_pl()
# print(norm_dimension_pl_1)

# with_load
# Ro = axies_load=, Rs = body_load=, Rr = frame_load=
# czop = 0 ,    R*Rox= Mo *Mox + Ms * Msx + Mr * Mrx+
# R = ( Mo *Mox + Ms * Msx + Mr * Mrx)/R0x

for added_load in extra_loads:
    R_axies_0 = R_axies_0 + (added_load[1]*added_load[2]//axies_0)


print(f'osie z ladunkiem = {int(R_axies_0)}')
# 0 = R_king + axies_load + body_load + frame_load - R_axies
R_king_0 = axies_load_0 + body_load_0 + frame_load_0 - R_axies_0
for added_load in extra_loads:
    R_king_0 = R_king_0 + added_load[2]
print(f'czop z ladunkiem = {int(R_king_0)}')


# Ma = 0   0 = (a-b)*loab_b -(a-b)Rx + (a-b-saddle)R_king

tractor_axis_b_load = ((asix_a_0-asix_b_0) * load_b_0 + (asix_a_0-asix_b_0-saddle_0)*R_king_0)/(asix_a_0-asix_b_0)
print(f'os tylna tracotra z ladunkiem= {int(tractor_axis_b_load)}')

# 0 = Fa + Fb - Czop - Fb0 - Fa0 --> Fa = -Fb + czop + Fbo +Fao
tractor_axis_a_load = - tractor_axis_b_load + R_king_0 + load_b_0 + load_a_0
print(f'os przednia tracotra z ladunkiem= {int(tractor_axis_a_load)}')


R_king = ['R_king', 0, R_king_0]
R_axies = ['R_axies', axies_0, R_axies_0]
tractor_axis_b_load = ['tractor_axis_b_load', tractor_axis_b_load, asix_b_0]
tractor_axis_a_load = ['tractor_axis_a_load', tractor_axis_a_load, asix_a_0]
# max load
dmc_0 = norm_load_pl()
axis_0 = norm_load_pl()[1]


# tractorUnit
tractorunit = TractorUnit(asix_a_0, load_a_0, asix_b_0, load_b_0, saddle_0, length_0)
matrix = tractorunit.matrix()

# semitrailer
frame_1 = SemiTrailer(king_pin_0, axies_0, axies_load_0, body_load_0, body_load_x_0,
                      frame_load_0, frame_load_x_0, length_0)
matrix_1 = frame_1.matrix_frame()

# extra force
# e xtra_load_0 = Load(mass_of_load, mass_of_load_x)

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
data.append(tractor_axis_b_load)
data.append(tractor_axis_a_load)


df = pd.DataFrame(data=data, columns=['nazwa', 'polozenie', 'wartosc_sily'])
# df.reset_index(inplace=True)
#
# print(df)

wb = Workbook()
ws = wb.active
df.to_excel("nazwa_pliku.xlsx", index=False)
# wb.save("calculator_of_load.xlsx")
