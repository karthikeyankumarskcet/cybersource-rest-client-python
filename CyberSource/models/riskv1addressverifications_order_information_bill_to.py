# coding: utf-8

"""
    CyberSource Merged Spec

    All CyberSource API specs merged together. These are available at https://developer.cybersource.com/api/reference/api-reference.html

    OpenAPI spec version: 0.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class Riskv1addressverificationsOrderInformationBillTo(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
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
        'address1': 'str',
        'address2': 'str',
        'address3': 'str',
        'address4': 'str',
        'administrative_area': 'str',
        'country': 'str',
        'locality': 'str',
        'postal_code': 'str'
    }

    attribute_map = {
        'address1': 'address1',
        'address2': 'address2',
        'address3': 'address3',
        'address4': 'address4',
        'administrative_area': 'administrativeArea',
        'country': 'country',
        'locality': 'locality',
        'postal_code': 'postalCode'
    }

    def __init__(self, address1=None, address2=None, address3=None, address4=None, administrative_area=None, country=None, locality=None, postal_code=None):
        """
        Riskv1addressverificationsOrderInformationBillTo - a model defined in Swagger
        """

        self._address1 = None
        self._address2 = None
        self._address3 = None
        self._address4 = None
        self._administrative_area = None
        self._country = None
        self._locality = None
        self._postal_code = None

        self.address1 = address1
        if address2 is not None:
          self.address2 = address2
        if address3 is not None:
          self.address3 = address3
        if address4 is not None:
          self.address4 = address4
        if administrative_area is not None:
          self.administrative_area = administrative_area
        self.country = country
        self.locality = locality
        self.postal_code = postal_code

    @property
    def address1(self):
        """
        Gets the address1 of this Riskv1addressverificationsOrderInformationBillTo.
        Payment card billing street address as it appears on the credit card issuer’s records.  #### Atos This field must not contain colons (:).  #### CyberSource through VisaNet **Important** When you populate orderInformation.billTo.address1 and orderInformation.billTo.address2, CyberSource through VisaNet concatenates the two values. If the concatenated value exceeds 40 characters, CyberSource through VisaNet truncates the value at 40 characters before sending it to Visa and the issuing bank. Truncating this value affects AVS results and therefore might also affect risk decisions and chargebacks. Credit card networks cannot process transactions that contain non-ASCII characters. CyberSource through VisaNet accepts and stores non-ASCII characters correctly and displays them correctly in reports. However, the limitations of the credit card networks prevent CyberSource through VisaNet from transmitting non-ASCII characters to the credit card networks. Therefore, CyberSource through VisaNet replaces non-ASCII characters with meaningless ASCII characters for transmission to the credit card networks.  #### FDMS Nashville When the street name is numeric, it must be sent in numeric format. For example, if the address is _One First Street_, it must be sent as _1 1st Street_.  Required if keyed; not used if swiped.  String (20)  #### TSYS Acquiring Solutions Required when `processingInformation.billPaymentOptions.billPayment=true` and `pointOfSaleInformation.entryMode=keyed`.  #### All other processors: Optional. String (60)  #### For Payouts This field may be sent only for FDC Compass.  **Important** It is your responsibility to determine whether a field is required for the transaction you are requesting. 

        :return: The address1 of this Riskv1addressverificationsOrderInformationBillTo.
        :rtype: str
        """
        return self._address1

    @address1.setter
    def address1(self, address1):
        """
        Sets the address1 of this Riskv1addressverificationsOrderInformationBillTo.
        Payment card billing street address as it appears on the credit card issuer’s records.  #### Atos This field must not contain colons (:).  #### CyberSource through VisaNet **Important** When you populate orderInformation.billTo.address1 and orderInformation.billTo.address2, CyberSource through VisaNet concatenates the two values. If the concatenated value exceeds 40 characters, CyberSource through VisaNet truncates the value at 40 characters before sending it to Visa and the issuing bank. Truncating this value affects AVS results and therefore might also affect risk decisions and chargebacks. Credit card networks cannot process transactions that contain non-ASCII characters. CyberSource through VisaNet accepts and stores non-ASCII characters correctly and displays them correctly in reports. However, the limitations of the credit card networks prevent CyberSource through VisaNet from transmitting non-ASCII characters to the credit card networks. Therefore, CyberSource through VisaNet replaces non-ASCII characters with meaningless ASCII characters for transmission to the credit card networks.  #### FDMS Nashville When the street name is numeric, it must be sent in numeric format. For example, if the address is _One First Street_, it must be sent as _1 1st Street_.  Required if keyed; not used if swiped.  String (20)  #### TSYS Acquiring Solutions Required when `processingInformation.billPaymentOptions.billPayment=true` and `pointOfSaleInformation.entryMode=keyed`.  #### All other processors: Optional. String (60)  #### For Payouts This field may be sent only for FDC Compass.  **Important** It is your responsibility to determine whether a field is required for the transaction you are requesting. 

        :param address1: The address1 of this Riskv1addressverificationsOrderInformationBillTo.
        :type: str
        """
        if address1 is None:
            raise ValueError("Invalid value for `address1`, must not be `None`")
        if address1 is not None and len(address1) > 60:
            raise ValueError("Invalid value for `address1`, length must be less than or equal to `60`")

        self._address1 = address1

    @property
    def address2(self):
        """
        Gets the address2 of this Riskv1addressverificationsOrderInformationBillTo.
        Used for additional address information. For example: _Attention: Accounts Payable_ Optional field.  For Payouts: This field may be sent only for FDC Compass.  #### Atos This field must not contain colons (:).  #### CyberSource through VisaNet **Important** When you populate `orderInformation.billTo.address1` and `orderInformation.billTo.address2`, CyberSource through VisaNet concatenates the two values. If the concatenated value exceeds 40 characters, CyberSource through VisaNet truncates the value at 40 characters before sending it to Visa and the issuing bank. Truncating this value affects AVS results and therefore might also affect risk decisions and chargebacks. Credit card networks cannot process transactions that contain non-ASCII characters. CyberSource through VisaNet accepts and stores non-ASCII characters correctly and displays them correctly in reports. However, the limitations of the credit card networks prevent CyberSource through VisaNet from transmitting non-ASCII characters to the credit card networks. Therefore, CyberSource through VisaNet replaces non-ASCII characters with meaningless ASCII characters for transmission to the credit card networks.  #### Chase Paymentech Solutions, FDC Compass, and TSYS Acquiring Solutions This value is used for AVS.  #### FDMS Nashville `orderInformation.billTo.address1` and `orderInformation.billTo.address2` together cannot exceed 20 characters. String (20)  #### All Other Processors String (60) 

        :return: The address2 of this Riskv1addressverificationsOrderInformationBillTo.
        :rtype: str
        """
        return self._address2

    @address2.setter
    def address2(self, address2):
        """
        Sets the address2 of this Riskv1addressverificationsOrderInformationBillTo.
        Used for additional address information. For example: _Attention: Accounts Payable_ Optional field.  For Payouts: This field may be sent only for FDC Compass.  #### Atos This field must not contain colons (:).  #### CyberSource through VisaNet **Important** When you populate `orderInformation.billTo.address1` and `orderInformation.billTo.address2`, CyberSource through VisaNet concatenates the two values. If the concatenated value exceeds 40 characters, CyberSource through VisaNet truncates the value at 40 characters before sending it to Visa and the issuing bank. Truncating this value affects AVS results and therefore might also affect risk decisions and chargebacks. Credit card networks cannot process transactions that contain non-ASCII characters. CyberSource through VisaNet accepts and stores non-ASCII characters correctly and displays them correctly in reports. However, the limitations of the credit card networks prevent CyberSource through VisaNet from transmitting non-ASCII characters to the credit card networks. Therefore, CyberSource through VisaNet replaces non-ASCII characters with meaningless ASCII characters for transmission to the credit card networks.  #### Chase Paymentech Solutions, FDC Compass, and TSYS Acquiring Solutions This value is used for AVS.  #### FDMS Nashville `orderInformation.billTo.address1` and `orderInformation.billTo.address2` together cannot exceed 20 characters. String (20)  #### All Other Processors String (60) 

        :param address2: The address2 of this Riskv1addressverificationsOrderInformationBillTo.
        :type: str
        """
        if address2 is not None and len(address2) > 60:
            raise ValueError("Invalid value for `address2`, length must be less than or equal to `60`")

        self._address2 = address2

    @property
    def address3(self):
        """
        Gets the address3 of this Riskv1addressverificationsOrderInformationBillTo.
        Additional address information (third line of the billing address) 

        :return: The address3 of this Riskv1addressverificationsOrderInformationBillTo.
        :rtype: str
        """
        return self._address3

    @address3.setter
    def address3(self, address3):
        """
        Sets the address3 of this Riskv1addressverificationsOrderInformationBillTo.
        Additional address information (third line of the billing address) 

        :param address3: The address3 of this Riskv1addressverificationsOrderInformationBillTo.
        :type: str
        """
        if address3 is not None and len(address3) > 60:
            raise ValueError("Invalid value for `address3`, length must be less than or equal to `60`")

        self._address3 = address3

    @property
    def address4(self):
        """
        Gets the address4 of this Riskv1addressverificationsOrderInformationBillTo.
        Additional address information (fourth line of the billing address) 

        :return: The address4 of this Riskv1addressverificationsOrderInformationBillTo.
        :rtype: str
        """
        return self._address4

    @address4.setter
    def address4(self, address4):
        """
        Sets the address4 of this Riskv1addressverificationsOrderInformationBillTo.
        Additional address information (fourth line of the billing address) 

        :param address4: The address4 of this Riskv1addressverificationsOrderInformationBillTo.
        :type: str
        """
        if address4 is not None and len(address4) > 60:
            raise ValueError("Invalid value for `address4`, length must be less than or equal to `60`")

        self._address4 = address4

    @property
    def administrative_area(self):
        """
        Gets the administrative_area of this Riskv1addressverificationsOrderInformationBillTo.
        State or province of the billing address. Use the [State, Province, and Territory Codes for the United States and Canada](https://developer.cybersource.com/library/documentation/sbc/quickref/states_and_provinces.pdf).  For Payouts: This field may be sent only for FDC Compass.  ##### CyberSource through VisaNet Credit card networks cannot process transactions that contain non-ASCII characters. CyberSource through VisaNet accepts and stores non-ASCII characters correctly and displays them correctly in reports. However, the limitations of the credit card networks prevent CyberSource through VisaNet from transmitting non-ASCII characters to the credit card networks. Therefore, CyberSource through VisaNet replaces non-ASCII characters with meaningless ASCII characters for transmission to the credit card networks.  **Important** It is your responsibility to determine whether a field is required for the transaction you are requesting.  #### Chase Paymentech Solutions Optional field.  ####  Credit Mutuel-CIC Optional field.  #### OmniPay Direct Optional field.  #### SIX Optional field.  #### TSYS Acquiring Solutions Required when `processingInformation.billPaymentOptions.billPayment=true` and `pointOfSaleInformation.entryMode=keyed`.  #### Worldpay VAP Optional field.  #### All other processors Not used. 

        :return: The administrative_area of this Riskv1addressverificationsOrderInformationBillTo.
        :rtype: str
        """
        return self._administrative_area

    @administrative_area.setter
    def administrative_area(self, administrative_area):
        """
        Sets the administrative_area of this Riskv1addressverificationsOrderInformationBillTo.
        State or province of the billing address. Use the [State, Province, and Territory Codes for the United States and Canada](https://developer.cybersource.com/library/documentation/sbc/quickref/states_and_provinces.pdf).  For Payouts: This field may be sent only for FDC Compass.  ##### CyberSource through VisaNet Credit card networks cannot process transactions that contain non-ASCII characters. CyberSource through VisaNet accepts and stores non-ASCII characters correctly and displays them correctly in reports. However, the limitations of the credit card networks prevent CyberSource through VisaNet from transmitting non-ASCII characters to the credit card networks. Therefore, CyberSource through VisaNet replaces non-ASCII characters with meaningless ASCII characters for transmission to the credit card networks.  **Important** It is your responsibility to determine whether a field is required for the transaction you are requesting.  #### Chase Paymentech Solutions Optional field.  ####  Credit Mutuel-CIC Optional field.  #### OmniPay Direct Optional field.  #### SIX Optional field.  #### TSYS Acquiring Solutions Required when `processingInformation.billPaymentOptions.billPayment=true` and `pointOfSaleInformation.entryMode=keyed`.  #### Worldpay VAP Optional field.  #### All other processors Not used. 

        :param administrative_area: The administrative_area of this Riskv1addressverificationsOrderInformationBillTo.
        :type: str
        """
        if administrative_area is not None and len(administrative_area) > 20:
            raise ValueError("Invalid value for `administrative_area`, length must be less than or equal to `20`")

        self._administrative_area = administrative_area

    @property
    def country(self):
        """
        Gets the country of this Riskv1addressverificationsOrderInformationBillTo.
        Payment card billing country. Use the two-character [ISO Standard Country Codes](http://apps.cybersource.com/library/documentation/sbc/quickref/countries_alpha_list.pdf).  #### CyberSource through VisaNet Credit card networks cannot process transactions that contain non-ASCII characters. CyberSource through VisaNet accepts and stores non-ASCII characters correctly and displays them correctly in reports. However, the limitations of the credit card networks prevent CyberSource through VisaNet from transmitting non-ASCII characters to the credit card networks. Therefore, CyberSource through VisaNet replaces non-ASCII characters with meaningless ASCII characters for transmission to the credit card networks.  **Important** It is your responsibility to determine whether a field is required for the transaction you are requesting.  #### Chase Paymentech Solutions Optional field.  ####  Credit Mutuel-CIC Optional field.  #### OmniPay Direct Optional field.  #### SIX Optional field.  #### TSYS Acquiring Solutions Required when `processingInformation.billPaymentOptions.billPayment=true` and `pointOfSaleInformation.entryMode=keyed`.  #### Worldpay VAP Optional field.  #### All other processors Not used. 

        :return: The country of this Riskv1addressverificationsOrderInformationBillTo.
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """
        Sets the country of this Riskv1addressverificationsOrderInformationBillTo.
        Payment card billing country. Use the two-character [ISO Standard Country Codes](http://apps.cybersource.com/library/documentation/sbc/quickref/countries_alpha_list.pdf).  #### CyberSource through VisaNet Credit card networks cannot process transactions that contain non-ASCII characters. CyberSource through VisaNet accepts and stores non-ASCII characters correctly and displays them correctly in reports. However, the limitations of the credit card networks prevent CyberSource through VisaNet from transmitting non-ASCII characters to the credit card networks. Therefore, CyberSource through VisaNet replaces non-ASCII characters with meaningless ASCII characters for transmission to the credit card networks.  **Important** It is your responsibility to determine whether a field is required for the transaction you are requesting.  #### Chase Paymentech Solutions Optional field.  ####  Credit Mutuel-CIC Optional field.  #### OmniPay Direct Optional field.  #### SIX Optional field.  #### TSYS Acquiring Solutions Required when `processingInformation.billPaymentOptions.billPayment=true` and `pointOfSaleInformation.entryMode=keyed`.  #### Worldpay VAP Optional field.  #### All other processors Not used. 

        :param country: The country of this Riskv1addressverificationsOrderInformationBillTo.
        :type: str
        """
        if country is None:
            raise ValueError("Invalid value for `country`, must not be `None`")
        if country is not None and len(country) > 2:
            raise ValueError("Invalid value for `country`, length must be less than or equal to `2`")

        self._country = country

    @property
    def locality(self):
        """
        Gets the locality of this Riskv1addressverificationsOrderInformationBillTo.
        Payment card billing city.  #### Atos This field must not contain colons (:).  #### CyberSource through VisaNet Credit card networks cannot process transactions that contain non-ASCII characters. CyberSource through VisaNet accepts and stores non-ASCII characters correctly and displays them correctly in reports. However, the limitations of the credit card networks prevent CyberSource through VisaNet from transmitting non-ASCII characters to the credit card networks. Therefore, CyberSource through VisaNet replaces non-ASCII characters with meaningless ASCII characters for transmission to the credit card networks.  #### For Payouts: This field may be sent only for FDC Compass.  #### Chase Paymentech Solutions Optional field.  ####  Credit Mutuel-CIC Optional field.  #### OmniPay Direct Optional field.  #### SIX Optional field.  #### TSYS Acquiring Solutions Required when `processingInformation.billPaymentOptions.billPayment=true` and `pointOfSaleInformation.entryMode=keyed`.  #### Worldpay VAP Optional field.  #### All other processors Not used. 

        :return: The locality of this Riskv1addressverificationsOrderInformationBillTo.
        :rtype: str
        """
        return self._locality

    @locality.setter
    def locality(self, locality):
        """
        Sets the locality of this Riskv1addressverificationsOrderInformationBillTo.
        Payment card billing city.  #### Atos This field must not contain colons (:).  #### CyberSource through VisaNet Credit card networks cannot process transactions that contain non-ASCII characters. CyberSource through VisaNet accepts and stores non-ASCII characters correctly and displays them correctly in reports. However, the limitations of the credit card networks prevent CyberSource through VisaNet from transmitting non-ASCII characters to the credit card networks. Therefore, CyberSource through VisaNet replaces non-ASCII characters with meaningless ASCII characters for transmission to the credit card networks.  #### For Payouts: This field may be sent only for FDC Compass.  #### Chase Paymentech Solutions Optional field.  ####  Credit Mutuel-CIC Optional field.  #### OmniPay Direct Optional field.  #### SIX Optional field.  #### TSYS Acquiring Solutions Required when `processingInformation.billPaymentOptions.billPayment=true` and `pointOfSaleInformation.entryMode=keyed`.  #### Worldpay VAP Optional field.  #### All other processors Not used. 

        :param locality: The locality of this Riskv1addressverificationsOrderInformationBillTo.
        :type: str
        """
        if locality is None:
            raise ValueError("Invalid value for `locality`, must not be `None`")
        if locality is not None and len(locality) > 50:
            raise ValueError("Invalid value for `locality`, length must be less than or equal to `50`")

        self._locality = locality

    @property
    def postal_code(self):
        """
        Gets the postal_code of this Riskv1addressverificationsOrderInformationBillTo.
        Postal code for the billing address. The postal code must consist of 5 to 9 digits.  When the billing country is the U.S., the 9-digit postal code must follow this format: [5 digits][dash][4 digits]  **Example** `12345-6789`  When the billing country is Canada, the 6-digit postal code must follow this format: [alpha][numeric][alpha][space][numeric][alpha][numeric]  **Example** `A1B 2C3`  **Important** It is your responsibility to determine whether a field is required for the transaction you are requesting.  #### For Payouts:  This field may be sent only for FDC Compass.  #### American Express Direct Before sending the postal code to the processor, CyberSource removes all nonalphanumeric characters and, if the remaining value is longer than nine characters, truncates the value starting from the right side.  #### Atos This field must not contain colons (:).  #### CyberSource through VisaNet Credit card networks cannot process transactions that contain non-ASCII characters. CyberSource through VisaNet accepts and stores non-ASCII characters correctly and displays them correctly in reports. However, the limitations of the credit card networks prevent CyberSource through VisaNet from transmitting non-ASCII characters to the credit card networks. Therefore, CyberSource through VisaNet replaces non-ASCII characters with meaningless ASCII characters for transmission to the credit card networks.  #### FDMS Nashville Required if `pointOfSaleInformation.entryMode=keyed` and the address is in the U.S. or Canada. Optional if `pointOfSaleInformation.entryMode=keyed` and the address is **not** in the U.S. or Canada. Not used if swiped.  #### RBS WorldPay Atlanta: For best card-present keyed rates, send the postal code if `pointOfSaleInformation.entryMode=keyed`.  #### TSYS Acquiring Solutions Required when `processingInformation.billPaymentOptions.billPayment=true` and `pointOfSaleInformation.entryMode=keyed`.  #### All other processors: Optional field. 

        :return: The postal_code of this Riskv1addressverificationsOrderInformationBillTo.
        :rtype: str
        """
        return self._postal_code

    @postal_code.setter
    def postal_code(self, postal_code):
        """
        Sets the postal_code of this Riskv1addressverificationsOrderInformationBillTo.
        Postal code for the billing address. The postal code must consist of 5 to 9 digits.  When the billing country is the U.S., the 9-digit postal code must follow this format: [5 digits][dash][4 digits]  **Example** `12345-6789`  When the billing country is Canada, the 6-digit postal code must follow this format: [alpha][numeric][alpha][space][numeric][alpha][numeric]  **Example** `A1B 2C3`  **Important** It is your responsibility to determine whether a field is required for the transaction you are requesting.  #### For Payouts:  This field may be sent only for FDC Compass.  #### American Express Direct Before sending the postal code to the processor, CyberSource removes all nonalphanumeric characters and, if the remaining value is longer than nine characters, truncates the value starting from the right side.  #### Atos This field must not contain colons (:).  #### CyberSource through VisaNet Credit card networks cannot process transactions that contain non-ASCII characters. CyberSource through VisaNet accepts and stores non-ASCII characters correctly and displays them correctly in reports. However, the limitations of the credit card networks prevent CyberSource through VisaNet from transmitting non-ASCII characters to the credit card networks. Therefore, CyberSource through VisaNet replaces non-ASCII characters with meaningless ASCII characters for transmission to the credit card networks.  #### FDMS Nashville Required if `pointOfSaleInformation.entryMode=keyed` and the address is in the U.S. or Canada. Optional if `pointOfSaleInformation.entryMode=keyed` and the address is **not** in the U.S. or Canada. Not used if swiped.  #### RBS WorldPay Atlanta: For best card-present keyed rates, send the postal code if `pointOfSaleInformation.entryMode=keyed`.  #### TSYS Acquiring Solutions Required when `processingInformation.billPaymentOptions.billPayment=true` and `pointOfSaleInformation.entryMode=keyed`.  #### All other processors: Optional field. 

        :param postal_code: The postal_code of this Riskv1addressverificationsOrderInformationBillTo.
        :type: str
        """
        if postal_code is None:
            raise ValueError("Invalid value for `postal_code`, must not be `None`")
        if postal_code is not None and len(postal_code) > 10:
            raise ValueError("Invalid value for `postal_code`, length must be less than or equal to `10`")

        self._postal_code = postal_code

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, Riskv1addressverificationsOrderInformationBillTo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
