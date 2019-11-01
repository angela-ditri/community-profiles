from .core import CensusDataset


class TotalPopulation(CensusDataset):
    """
    Total population

    Source
    ------
    American Community Survey
    """

    UNIVERSE = "Total Population"
    TABLE_NAME = "B01003"
    RAW_FIELDS = {"001": "total_population"}

    @classmethod
    def process(cls, df):

        # Area in sq. mile
        FT_PER_MILE = 5280.0
        df["area"] = df.geometry.area / (FT_PER_MILE) ** 2
        df["area_moe"] = 0

        # Density in people / sq mile
        df["density"] = df["total_population"] / df["area"]
        df["density_moe"] = df["total_population_moe"] / df["area"]

        return df

