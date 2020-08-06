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


class Tmsv2customersEmbedded(object):
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
        'default_payment_instrument': 'Tmsv2customersEmbeddedDefaultPaymentInstrument',
        'default_shipping_address': 'Tmsv2customersEmbeddedDefaultShippingAddress'
    }

    attribute_map = {
        'default_payment_instrument': 'defaultPaymentInstrument',
        'default_shipping_address': 'defaultShippingAddress'
    }

    def __init__(self, default_payment_instrument=None, default_shipping_address=None):
        """
        Tmsv2customersEmbedded - a model defined in Swagger
        """

        self._default_payment_instrument = None
        self._default_shipping_address = None

        if default_payment_instrument is not None:
          self.default_payment_instrument = default_payment_instrument
        if default_shipping_address is not None:
          self.default_shipping_address = default_shipping_address

    @property
    def default_payment_instrument(self):
        """
        Gets the default_payment_instrument of this Tmsv2customersEmbedded.

        :return: The default_payment_instrument of this Tmsv2customersEmbedded.
        :rtype: Tmsv2customersEmbeddedDefaultPaymentInstrument
        """
        return self._default_payment_instrument

    @default_payment_instrument.setter
    def default_payment_instrument(self, default_payment_instrument):
        """
        Sets the default_payment_instrument of this Tmsv2customersEmbedded.

        :param default_payment_instrument: The default_payment_instrument of this Tmsv2customersEmbedded.
        :type: Tmsv2customersEmbeddedDefaultPaymentInstrument
        """

        self._default_payment_instrument = default_payment_instrument

    @property
    def default_shipping_address(self):
        """
        Gets the default_shipping_address of this Tmsv2customersEmbedded.

        :return: The default_shipping_address of this Tmsv2customersEmbedded.
        :rtype: Tmsv2customersEmbeddedDefaultShippingAddress
        """
        return self._default_shipping_address

    @default_shipping_address.setter
    def default_shipping_address(self, default_shipping_address):
        """
        Sets the default_shipping_address of this Tmsv2customersEmbedded.

        :param default_shipping_address: The default_shipping_address of this Tmsv2customersEmbedded.
        :type: Tmsv2customersEmbeddedDefaultShippingAddress
        """

        self._default_shipping_address = default_shipping_address

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
        if not isinstance(other, Tmsv2customersEmbedded):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
