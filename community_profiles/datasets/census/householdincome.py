from .core import CensusDataset
import collections

__all__ = ["HouseholdIncome"]


class HouseholdIncome(CensusDataset):
    """
    Household income in the past 12 months (in inflation-adjusted dollars).
    """

    UNIVERSE = "households"
    TABLE_NAME = "B19001"
    RAW_FIELDS = collections.OrderedDict(
        {
            "001": "universe",
            "002": "0_to_9999",
            "003": "10000_to_14999",
            "004": "15000_to_19999",
            "005": "20000_to_24999",
            "006": "25000_to_29999",
            "007": "30000_to_34999",
            "008": "35000_to_39999",
            "009": "40000_to_44999",
            "010": "45000_to_49999",
            "011": "50000_to_59999",
            "012": "60000_to_74999",
            "013": "75000_to_99999",
            "014": "100000_to_124999",
            "015": "125000_to_149999",
            "016": "150000_to_199999",
            "017": "200000_or_more",
        }
    )

