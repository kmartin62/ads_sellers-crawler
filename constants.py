import csv

PAGE_URL = "https://www.autoscout24.com"

TYPE_LABEL = "Type"
PREVIOUS_OWNERS_LABEL = "Previous Owners"
GEARING_TYPE_LABEL = "Gearing Type"
GEARS_LABEL = "Gears"
DISPLACEMENT_LABEL = "Displacement"
CYLINDERS_LABEL = "Cylinders"
WEIGHT_LABEL = "Weight"
DRIVE_CHAIN_LABEL = "Drive chain"
MAKE_LABEL = "Make"
MODEL_LABEL = "Model"
OFFER_NUMBER_LABEL = "Offer Number"
BODY_COLOR_LABEL = "Body Color"
PAINT_TYPE_LABEL = "Paint Type"
BODY_COLOR_ORIGINAL_LABEL = "Body Color Original"
UPHOLSTERY_LABEL = "Upholstery"
BODY_LABEL = "Body"
NR_OF_DOORS_LABEL = "Nr. of Doors"
NR_OF_SEATS_LABEL = "Nr. of Seats"
MODEL_CODE_LABEL = "Model Code"

CAR_METRICS = ["ID", "Make", "Model", "Body", "First Registration", "Fuel", "Mileage", "Power(hp)",
               "Gearing Type", "Displacement", "Warranty", "Full Service", "Non-smoking Vehicle",
               "Model Code", "Price"]

AD_METRICS = ["CarID", "SellerID", "Title", "Description", "Price", "Type", "URL"]

EQ_METRICS = ["AdID", "ABS", "Driver-side airbag", "Passenger-side airbag",
              "Sunroof", "Radio", "4WD", "Power windows", "Alloy wheels", "Central door lock", "Alarm system",
              "Navigation system", "Immobilizer", "Side airbag", "Seat heating", "Disabled accessible",
              "Cruise control",
              "Xenon headlights", "On-board computer", "Electronic stability control", "Fog lights", "Trailer hitch",
              "Air conditioning",
              "Roof rack", "Power steering", "Automatic climate control", "Traction control",
              "Electrically adjustable seats",
              "MP3", "Panorama roof", "Auxiliary heating", "Sport package", "Start-stop system",
              "Multi-function steering wheel",
              "Daytime running lights", "Sport suspension", "Sport seats",
              "Adaptive headlights", "Ski bag", "Adaptive Cruise Control",
              "Armrest", "Electrically heated windshield", "Heated steering wheel",
              "Hill Holder", "Digital radio", "LED Headlights", "Electric tailgate",
              "LED Daytime Running Lights", "Leather steering wheel",
              "Air suspension", "Massage seats", "Night view assist", "Tire pressure monitoring system",
              "Keyless central door lock", "Lane departure warning system",
              "Blind spot monitor", "Touch screen", "USB", "Traffic sign recognition",
              "Electrical side mirrors", "Bluetooth", "Isofix", "Rain sensor",
              "Parking assist system sensors front", "Parking assist system sensors rear",
              "Parking assist system camera", "Parking assist system self-steering",
              "CD player"]

SELLER_METRICS = ["SellerID", "Vendor", "City", "ZipCode", "Country"]

CAR_DICT = dict.fromkeys(CAR_METRICS, "NULL")
AD_DICT = dict.fromkeys(AD_METRICS, "NULL")
EQ_DICT = dict.fromkeys(EQ_METRICS, "NULL")
SELLER_DICT = dict.fromkeys(SELLER_METRICS, "NULL")


BMW_MODELS = list()
with open('bmw_models.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        BMW_MODELS.append(row[0])
