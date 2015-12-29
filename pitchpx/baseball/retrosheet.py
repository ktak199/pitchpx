#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Shinichi Nakagawa'


class RetroSheet(object):

    EVENT_02_GENERIC_OUT_FLYBALL = ('flyout', 'fly out', 'sac fly', 'sac fly dp')
    EVENT_02_GENERIC_OUT_LINEDRIVE = ('lineout', 'line out', 'bunt lineout')
    EVENT_02_GENERIC_OUT_POPUP = ('pop out', 'bunt pop out')
    EVENT_02_GENERIC_OUT_GROUNDBALL = ('groundout', 'ground out', 'sac bunt', 'bunt groundout', 'grounded into dp')
    EVENT_02_GENERIC_OUT_OTHER = ('forceout', 'double play', 'triple play', 'sacrifice bunt d')
    EVENT_03_STRIKE_OUT = ('strikeout', 'strikeout - dp')
    EVENT_14_WALK = ('walk', )
    EVENT_15_INTENT_WALK = ('intent walk', )
    EVENT_16_HIT_BY_PITCH = ('hit by pitch', )
    EVENT_19_FIELDERS_CHOICE = ('fielders choice out', 'fielders choice')
    EVENT_20_SINGLE = ('single', )
    EVENT_21_DOUBLE = ('double', )
    EVENT_22_TRIPLE = ('triple', )
    EVENT_23_HOMERUN = ('home run')

    @classmethod
    def event_cd(cls, event_tx: str, ab_des: str) -> int:
        """
        Event Code for Retrosheet
        :param event_tx:
        :return: event_cd(int)
        """
        _event_tx = event_tx.lower()
        # Generic out(event_cd:2)
        if _event_tx in cls.EVENT_02_GENERIC_OUT_FLYBALL:
            return 2
        elif _event_tx in cls.EVENT_02_GENERIC_OUT_LINEDRIVE:
            return 2
        elif _event_tx in cls.EVENT_02_GENERIC_OUT_POPUP:
            return 2
        elif _event_tx in cls.EVENT_02_GENERIC_OUT_GROUNDBALL:
            return 2
        elif _event_tx in cls.EVENT_02_GENERIC_OUT_OTHER:
            return 2
        # Strike out(event_cd:3)
        elif _event_tx in cls.EVENT_03_STRIKE_OUT:
            return 3
        # Walk(event_cd:14)
        elif _event_tx in cls.EVENT_14_WALK:
            return 14
        # Intent Walk(event_cd:15)
        elif _event_tx in cls.EVENT_15_INTENT_WALK:
            return 15
        # Hit By Pitch(event_cd:16)
        elif _event_tx in cls.EVENT_16_HIT_BY_PITCH:
            return 16
        # Interference(event_cd:17)
        elif _event_tx.lower().count('interference') > 0:
            return 17
        # Error(event_cd:18)
        elif _event_tx[-5:] == 'error':
            return 18
        # Fielder's choice(event_cd:19)
        elif _event_tx in cls.EVENT_19_FIELDERS_CHOICE:
            return 19
        # Single(event_cd:20)
        elif _event_tx in cls.EVENT_20_SINGLE:
            return 20
        # 2B(event_cd:21)
        elif _event_tx in cls.EVENT_21_DOUBLE:
            return 21
        # 3B(event_cd:22)
        elif _event_tx in cls.EVENT_22_TRIPLE:
            return 22
        # HR(event_cd:22)
        elif _event_tx in cls.EVENT_23_HOMERUN:
            return 23
        # Runner Out
        elif _event_tx == 'runner out':
            # Caught stealing(event_cd:6)
            if ab_des.lower().count("caught stealing") > 0:
                return 6
            # Picks off(event_cd:6)
            elif ab_des.lower().count("picks off") > 0:
                return 8
            # Unknown event(event_cd:0)
            else:
                return 0
        # Unknown event(event_cd:0)
        else:
            return 0
