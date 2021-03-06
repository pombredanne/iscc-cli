# -*- coding: utf-8 -*-
import os
from tests import ROOT_DIR
from iscc_cli import audio_id
from iscc_cli import fpcalc

os.chdir(ROOT_DIR)


def test_content_id_audio():
    assert audio_id.content_id_audio([1, 2, 3]) == "CACCCCCidbPMJ"


def test_get_chroma_vector_file_path():
    if not fpcalc.is_installed():
        fpcalc.install()
    r = audio_id.get_chroma_vector("tests/audio/demo.mp3")
    assert isinstance(r, list)
    assert r == [
        684003877,
        683946551,
        1749295639,
        2017796679,
        2026256086,
        2022066918,
        2022001639,
        2021968035,
        2038741139,
        2059709571,
        503750851,
        369541315,
        320225426,
        289292450,
        830368930,
        838789539,
        1940835201,
        1928186752,
        1651297920,
        1651283600,
        1650959072,
        1655022116,
        1722069540,
        1726259749,
        1713694254,
        1847914286,
        1847912494,
        1780832302,
        -362410962,
        -352973810,
        1809196111,
        1770397775,
        1753686797,
        683942429,
        943989277,
        943989255,
        944121430,
        952503910,
        948374246,
        948717799,
        1485621411,
        462203011,
        508470403,
        370053251,
        303988867,
        322879651,
        322892963,
        862907811,
        1928256417,
        1928317841,
        1651297152,
        1647091344,
        1650827936,
        1659216416,
        1722069540,
        1726263844,
        1717887533,
        1713696302,
        1847912494,
        1847883822,
        -366540754,
        -345633778,
        -336184242,
        1771447375,
        1753620815,
        1757684255,
        675553815,
        943989255,
        944120390,
        952508006,
        948308582,
        948718050,
        411879650,
        428648578,
        516861059,
        370057347,
        303988865,
        306086033,
        306086049,
        841919649,
        846133665,
        1919929264,
        1647168400,
        1647101584,
        1650827936,
        1659216484,
        1671733796,
        1738838588,
        1717887517,
        1713696302,
        1847913774,
        1847879726,
        1780960302,
        -362410978,
        -336196594,
        1775641678,
        1770397775,
        1753555743,
        683942429,
        943989271,
        944185926,
        2026255094,
        2022051494,
        2021919654,
    ]


def test_get_chroma_vector_file_stream():
    if not fpcalc.is_installed():
        fpcalc.install()
    with open("tests/audio/demo.mp3", "rb") as file_obj:
        r = audio_id.get_chroma_vector(file_obj)
    assert isinstance(r, list)
    assert r == [
        684003877,
        683946551,
        1749295639,
        2017796679,
        2026256086,
        2022066918,
        2022001639,
        2021968035,
        2038741139,
        2059709571,
        503750851,
        369541315,
        320225426,
        289292450,
        830368930,
        838789539,
        1940835201,
        1928186752,
        1651297920,
        1651283600,
        1650959072,
        1655022116,
        1722069540,
        1726259749,
        1713694254,
        1847914286,
        1847912494,
        1780832302,
        -362410962,
        -352973810,
        1809196111,
        1770397775,
        1753686797,
        683942429,
        943989277,
        943989255,
        944121430,
        952503910,
        948374246,
        948717799,
        1485621411,
        462203011,
        508470403,
        370053251,
        303988867,
        322879651,
        322892963,
        862907811,
        1928256417,
        1928317841,
        1651297152,
        1647091344,
        1650827936,
        1659216416,
        1722069540,
        1726263844,
        1717887533,
        1713696302,
        1847912494,
        1847883822,
        -366540754,
        -345633778,
        -336184242,
        1771447375,
        1753620815,
        1757684255,
        675553815,
        943989255,
        944120390,
        952508006,
        948308582,
        948718050,
        411879650,
        428648578,
        516861059,
        370057347,
        303988865,
        306086033,
        306086049,
        841919649,
        846133665,
        1919929264,
        1647168400,
        1647101584,
        1650827936,
        1659216484,
        1671733796,
        1738838588,
        1717887517,
        1713696302,
        1847913774,
        1847879726,
        1780960302,
        -362410978,
        -336196594,
        1775641678,
        1770397775,
        1753555743,
        683942429,
        943989271,
        944185926,
        2026255094,
        2022051494,
        2021919654,
    ]
