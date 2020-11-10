# !/usr/bin/env python3
# -*- coding: utf-8 -*-

# ----------------------------------------------------- IMPORTS ----------------------------------------------------- #

from __future__ import annotations
import logging
from abc import ABC
from Crypto.PublicKey import RSA
from typing import List

from src.utils.crypto import sign, verify


__author__ = 'Denis Verstraeten'
__date__ = '2020.3.5'


class Participant(ABC):
    """
    This super class handles everything related to participants of the auction.
    It should be extended in Auctioneer and in Bidder.
    """

    # ------------------------------------------------- CONSTRUCTOR ------------------------------------------------- #

    def __init__(self,
                 address: str,
                 generate_new_keys: bool
                 ) -> None:
        """
        :param address: Address of the Participant.
        :param generate_new_keys: Flag indicating whether new RSA keys need to be generated.
        """

        logging.info('Creating Participant.')
        self.address = address
        if generate_new_keys:

            self._RSA_key = RSA.generate(2048)
            self.public_key = self._RSA_key.publickey()

        else:

            self._RSA_key = None
            self.public_key = None

        self._ring = None  # List of public keys used for the ring signature scheme.
        self._s = None  # Index of the Participant in the ring. self._ring[s] = self.public_key.
