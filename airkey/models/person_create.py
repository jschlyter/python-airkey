# coding: utf-8

"""
    EVVA AirKey Cloud API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: v16.20.7
    Contact: office-wien@evva.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class PersonCreate(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'first_name': 'str',
        'last_name': 'str',
        'secondary_identification': 'str',
        'gender': 'str',
        'birthday': 'str',
        'phone': 'str',
        'email_address': 'str',
        'street': 'str',
        'postal_code': 'str',
        'country_code': 'str',
        'city': 'str',
        'comment': 'str',
        'correspondence_language_code': 'str'
    }

    attribute_map = {
        'first_name': 'firstName',
        'last_name': 'lastName',
        'secondary_identification': 'secondaryIdentification',
        'gender': 'gender',
        'birthday': 'birthday',
        'phone': 'phone',
        'email_address': 'emailAddress',
        'street': 'street',
        'postal_code': 'postalCode',
        'country_code': 'countryCode',
        'city': 'city',
        'comment': 'comment',
        'correspondence_language_code': 'correspondenceLanguageCode'
    }

    def __init__(self, first_name=None, last_name=None, secondary_identification=None, gender=None, birthday=None, phone=None, email_address=None, street=None, postal_code=None, country_code=None, city=None, comment=None, correspondence_language_code=None):  # noqa: E501
        """PersonCreate - a model defined in Swagger"""  # noqa: E501
        self._first_name = None
        self._last_name = None
        self._secondary_identification = None
        self._gender = None
        self._birthday = None
        self._phone = None
        self._email_address = None
        self._street = None
        self._postal_code = None
        self._country_code = None
        self._city = None
        self._comment = None
        self._correspondence_language_code = None
        self.discriminator = None
        self.first_name = first_name
        self.last_name = last_name
        if secondary_identification is not None:
            self.secondary_identification = secondary_identification
        if gender is not None:
            self.gender = gender
        if birthday is not None:
            self.birthday = birthday
        if phone is not None:
            self.phone = phone
        if email_address is not None:
            self.email_address = email_address
        if street is not None:
            self.street = street
        if postal_code is not None:
            self.postal_code = postal_code
        if country_code is not None:
            self.country_code = country_code
        if city is not None:
            self.city = city
        if comment is not None:
            self.comment = comment
        self.correspondence_language_code = correspondence_language_code

    @property
    def first_name(self):
        """Gets the first_name of this PersonCreate.  # noqa: E501

        First name of the person (max. 50 characters)  # noqa: E501

        :return: The first_name of this PersonCreate.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this PersonCreate.

        First name of the person (max. 50 characters)  # noqa: E501

        :param first_name: The first_name of this PersonCreate.  # noqa: E501
        :type: str
        """
        if first_name is None:
            raise ValueError("Invalid value for `first_name`, must not be `None`")  # noqa: E501

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this PersonCreate.  # noqa: E501

        Last name of the person (max. 50 characters)  # noqa: E501

        :return: The last_name of this PersonCreate.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this PersonCreate.

        Last name of the person (max. 50 characters)  # noqa: E501

        :param last_name: The last_name of this PersonCreate.  # noqa: E501
        :type: str
        """
        if last_name is None:
            raise ValueError("Invalid value for `last_name`, must not be `None`")  # noqa: E501

        self._last_name = last_name

    @property
    def secondary_identification(self):
        """Gets the secondary_identification of this PersonCreate.  # noqa: E501

        Secondary identification of the person (max. 50 characters)  # noqa: E501

        :return: The secondary_identification of this PersonCreate.  # noqa: E501
        :rtype: str
        """
        return self._secondary_identification

    @secondary_identification.setter
    def secondary_identification(self, secondary_identification):
        """Sets the secondary_identification of this PersonCreate.

        Secondary identification of the person (max. 50 characters)  # noqa: E501

        :param secondary_identification: The secondary_identification of this PersonCreate.  # noqa: E501
        :type: str
        """

        self._secondary_identification = secondary_identification

    @property
    def gender(self):
        """Gets the gender of this PersonCreate.  # noqa: E501

        Gender of the person  # noqa: E501

        :return: The gender of this PersonCreate.  # noqa: E501
        :rtype: str
        """
        return self._gender

    @gender.setter
    def gender(self, gender):
        """Sets the gender of this PersonCreate.

        Gender of the person  # noqa: E501

        :param gender: The gender of this PersonCreate.  # noqa: E501
        :type: str
        """
        allowed_values = ["MALE", "FEMALE"]  # noqa: E501
        if gender not in allowed_values:
            raise ValueError(
                "Invalid value for `gender` ({0}), must be one of {1}"  # noqa: E501
                .format(gender, allowed_values)
            )

        self._gender = gender

    @property
    def birthday(self):
        """Gets the birthday of this PersonCreate.  # noqa: E501

        Birthday (ISO 8601-format compliant date without time zone: yyyy-mm-dd)  # noqa: E501

        :return: The birthday of this PersonCreate.  # noqa: E501
        :rtype: str
        """
        return self._birthday

    @birthday.setter
    def birthday(self, birthday):
        """Sets the birthday of this PersonCreate.

        Birthday (ISO 8601-format compliant date without time zone: yyyy-mm-dd)  # noqa: E501

        :param birthday: The birthday of this PersonCreate.  # noqa: E501
        :type: str
        """

        self._birthday = birthday

    @property
    def phone(self):
        """Gets the phone of this PersonCreate.  # noqa: E501

        Phone number (max. 50 characters)  # noqa: E501

        :return: The phone of this PersonCreate.  # noqa: E501
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this PersonCreate.

        Phone number (max. 50 characters)  # noqa: E501

        :param phone: The phone of this PersonCreate.  # noqa: E501
        :type: str
        """

        self._phone = phone

    @property
    def email_address(self):
        """Gets the email_address of this PersonCreate.  # noqa: E501

        Email address (max. 50 characters)  # noqa: E501

        :return: The email_address of this PersonCreate.  # noqa: E501
        :rtype: str
        """
        return self._email_address

    @email_address.setter
    def email_address(self, email_address):
        """Sets the email_address of this PersonCreate.

        Email address (max. 50 characters)  # noqa: E501

        :param email_address: The email_address of this PersonCreate.  # noqa: E501
        :type: str
        """

        self._email_address = email_address

    @property
    def street(self):
        """Gets the street of this PersonCreate.  # noqa: E501

        Street (max. 50 characters)  # noqa: E501

        :return: The street of this PersonCreate.  # noqa: E501
        :rtype: str
        """
        return self._street

    @street.setter
    def street(self, street):
        """Sets the street of this PersonCreate.

        Street (max. 50 characters)  # noqa: E501

        :param street: The street of this PersonCreate.  # noqa: E501
        :type: str
        """

        self._street = street

    @property
    def postal_code(self):
        """Gets the postal_code of this PersonCreate.  # noqa: E501

        Postal code (max. 50 characters)  # noqa: E501

        :return: The postal_code of this PersonCreate.  # noqa: E501
        :rtype: str
        """
        return self._postal_code

    @postal_code.setter
    def postal_code(self, postal_code):
        """Sets the postal_code of this PersonCreate.

        Postal code (max. 50 characters)  # noqa: E501

        :param postal_code: The postal_code of this PersonCreate.  # noqa: E501
        :type: str
        """

        self._postal_code = postal_code

    @property
    def country_code(self):
        """Gets the country_code of this PersonCreate.  # noqa: E501

        Country code, ISO 3166-1 alpha-3 compliant and case sensitive (ONLY the defined ISO codes are accepted)  # noqa: E501

        :return: The country_code of this PersonCreate.  # noqa: E501
        :rtype: str
        """
        return self._country_code

    @country_code.setter
    def country_code(self, country_code):
        """Sets the country_code of this PersonCreate.

        Country code, ISO 3166-1 alpha-3 compliant and case sensitive (ONLY the defined ISO codes are accepted)  # noqa: E501

        :param country_code: The country_code of this PersonCreate.  # noqa: E501
        :type: str
        """
        allowed_values = ["ABW", "AFG", "AGO", "AIA", "ALA", "ALB", "AND", "ANT", "ARE", "ARG", "ARM", "ASM", "ATA", "ATF", "ATG", "AUS", "AUT", "AZE", "BDI", "BEL", "BEN", "BES", "BFA", "BGD", "BGR", "BHR", "BHS", "BIH", "BLM", "BLR", "BLZ", "BMU", "BOL", "BRA", "BRB", "BRN", "BTN", "BVT", "BWA", "CAF", "CAN", "CCK", "CHE", "CHL", "CHN", "CIV", "CMR", "COD", "COG", "COK", "COL", "COM", "CPV", "CRI", "CUB", "CUW", "CXR", "CYM", "CYP", "CZE", "DEU", "DJI", "DMA", "DNK", "DOM", "DZA", "ECU", "EGY", "ERI", "ESH", "ESP", "EST", "ETH", "FIN", "FJI", "FLK", "FRA", "FRO", "FSM", "GAB", "GBR", "GEO", "GGY", "GHA", "GIB", "GIN", "GLP", "GMB", "GNB", "GNQ", "GRC", "GRD", "GRL", "GTM", "GUF", "GUM", "GUY", "HKG", "HMD", "HND", "HRV", "HTI", "HUN", "IDN", "IMN", "IND", "IOT", "IRL", "IRN", "IRQ", "ISL", "ISR", "ITA", "JAM", "JEY", "JOR", "JPN", "KAZ", "KEN", "KGZ", "KHM", "KIR", "KNA", "KOR", "KWT", "LAO", "LBN", "LBR", "LBY", "LCA", "LIE", "LKA", "LSO", "LTU", "LUX", "LVA", "MAC", "MAF", "MAR", "MCO", "MDA", "MDG", "MDV", "MEX", "MHL", "MKD", "MLI", "MLT", "MMR", "MNE", "MNG", "MNP", "MOZ", "MRT", "MSR", "MTQ", "MUS", "MWI", "MYS", "MYT", "NAM", "NCL", "NER", "NFK", "NGA", "NIC", "NIU", "NLD", "NOR", "NPL", "NRU", "NZL", "OMN", "PAK", "PAN", "PCN", "PER", "PHL", "PLW", "PNG", "POL", "PRI", "PRK", "PRT", "PRY", "PSE", "PYF", "QAT", "REU", "ROU", "RUS", "RWA", "SAU", "SCG", "SDN", "SEN", "SGP", "SGS", "SHN", "SJM", "SLB", "SLE", "SLV", "SMR", "SOM", "SPM", "SRB", "STP", "SUR", "SVK", "SVN", "SWE", "SWZ", "SXM", "SYC", "SYR", "TCA", "TCD", "TGO", "THA", "TJK", "TKL", "TKM", "TLS", "TON", "TTO", "TUN", "TUR", "TUV", "TWN", "TZA", "UGA", "UKR", "UMI", "URY", "USA", "UZB", "VAT", "VCT", "VEN", "VGB", "VIR", "VNM", "VUT", "WLF", "WSM", "YEM", "ZAF", "ZMB", "ZWE"]  # noqa: E501
        if country_code not in allowed_values:
            raise ValueError(
                "Invalid value for `country_code` ({0}), must be one of {1}"  # noqa: E501
                .format(country_code, allowed_values)
            )

        self._country_code = country_code

    @property
    def city(self):
        """Gets the city of this PersonCreate.  # noqa: E501

        City (max. 50 characters)  # noqa: E501

        :return: The city of this PersonCreate.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this PersonCreate.

        City (max. 50 characters)  # noqa: E501

        :param city: The city of this PersonCreate.  # noqa: E501
        :type: str
        """

        self._city = city

    @property
    def comment(self):
        """Gets the comment of this PersonCreate.  # noqa: E501

        Comment (max. 500 characters)  # noqa: E501

        :return: The comment of this PersonCreate.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this PersonCreate.

        Comment (max. 500 characters)  # noqa: E501

        :param comment: The comment of this PersonCreate.  # noqa: E501
        :type: str
        """

        self._comment = comment

    @property
    def correspondence_language_code(self):
        """Gets the correspondence_language_code of this PersonCreate.  # noqa: E501

        Language code for correspondences, IETF bcp47 compliant and case sensitive (ONLY the 11 defined language tags are accepted)  # noqa: E501

        :return: The correspondence_language_code of this PersonCreate.  # noqa: E501
        :rtype: str
        """
        return self._correspondence_language_code

    @correspondence_language_code.setter
    def correspondence_language_code(self, correspondence_language_code):
        """Sets the correspondence_language_code of this PersonCreate.

        Language code for correspondences, IETF bcp47 compliant and case sensitive (ONLY the 11 defined language tags are accepted)  # noqa: E501

        :param correspondence_language_code: The correspondence_language_code of this PersonCreate.  # noqa: E501
        :type: str
        """
        if correspondence_language_code is None:
            raise ValueError("Invalid value for `correspondence_language_code`, must not be `None`")  # noqa: E501
        allowed_values = ["de-DE", "en-UK", "nl-NL", "sv-SE", "fr-FR", "it-IT", "es-ES", "pt-PT", "cs-CZ", "sk-SK", "pl-PL"]  # noqa: E501
        if correspondence_language_code not in allowed_values:
            raise ValueError(
                "Invalid value for `correspondence_language_code` ({0}), must be one of {1}"  # noqa: E501
                .format(correspondence_language_code, allowed_values)
            )

        self._correspondence_language_code = correspondence_language_code

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(PersonCreate, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PersonCreate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
