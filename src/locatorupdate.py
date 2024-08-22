import os
import zipfile
from arcgis.gis import GIS
import logging
import arcpy
from datetime import datetime
LOGGER = logging.getLogger(__name__)


def run(gis: GIS, output_path: str, locators: list[dict]):
    LOGGER.info('Start')
    
    
    arcpy.SignInToPortal("https://www.cfu.maps.arcgis.com")
    for locator in locators:
        try:
            LOGGER.info(f"Creating locator '{locator['name']}'.")
            arcpy.geocoding.CreateFeatureLocator(
            in_features=locator['link'],
            output_locator=os.path.join(output_path, locator['name'] + "_" + datetime.now().strftime("%Y%m%d")),
            search_fields=locator['map'],
            locator_fields=locator.get('etc')
        )
        except Exception as e:
            LOGGER.exception(f"An error occured generating locator '{locator['name']}'")
    LOGGER.info('End')

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    









'''
locators = [
        {
            "name": "AddressLocator",
            "link": 'https://services5.arcgis.com/g3r4E4Xlpygk5wEz/arcgis/rest/services/Addresses/FeatureServer/0',
            "map": """
                "'*Name' Address VISIBLE NONE" 
            """,
            "etc": """
                "'UnitNumber' UnitNum;
                'StreetAddress' Address;
                'CityName' City;
                'PostalCode' Zip;
                'LocationName' PlaceName;
                'PINNumber' PIN;
                'Subdiv' Subdivision;
                'AddressNumber' AddrNum"
            """
        },
        {
            "name": "BuildingNameLocator",
            "link": 'https://services5.arcgis.com/g3r4E4Xlpygk5wEz/arcgis/rest/services/Buildings_Footprints/FeatureServer/8',
            "map": "'*Name' BldgName VISIBLE NONE"
        },
        {
            "name": "GasCurbValveLocator",
            "link": 'https://services5.arcgis.com/g3r4E4Xlpygk5wEz/arcgis/rest/services/CurbValveLive/FeatureServer/0',
            "map": "'*Name' ValveID VISIBLE NONE"
        },
        {
            "name": "GasMainValveLocator",
            "link": 'https://services5.arcgis.com/g3r4E4Xlpygk5wEz/arcgis/rest/services/GasValveLive/FeatureServer/0',
            "map": "'*Name' ValveID VISIBLE NONE"
        },
        {
            "name": "HydrantLocator",
            "link": 'https://services5.arcgis.com/g3r4E4Xlpygk5wEz/arcgis/rest/services/Hydrants/FeatureServer/3',
            "map": "*Name FACILITYID VISIBLE NONE"
        },
        {
            "name": "RoadIntersectionLocator",
            "link": 'https://services5.arcgis.com/g3r4E4Xlpygk5wEz/arcgis/rest/services/Roads/FeatureServer/31',
            "map": "*Name Alphatag VISIBLE NONE"
        },
        {
            "name": "WaterLateralValveLocator",
            "link": 'https://services5.arcgis.com/g3r4E4Xlpygk5wEz/arcgis/rest/services/Water_All_Valves/FeatureServer/2',
            "map": "*Name FACILITYID VISIBLE NONE"
        },
        {
            "name": "WaterMainValveLocator",
            "link": 'https://services5.arcgis.com/g3r4E4Xlpygk5wEz/arcgis/rest/services/Water_All_Valves/FeatureServer/2',
            "map": "*Name FACILITYID VISIBLE NONE"
        },
        {
            "name": "WaterTowerLocator",
            "link": 'https://services5.arcgis.com/g3r4E4Xlpygk5wEz/arcgis/rest/services/Water_Tower/FeatureServer/0',
            "map": "*Name FacilityID VISIBLE NONE"
        } 
    ]
'''