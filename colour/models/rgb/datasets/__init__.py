# -*- coding: utf-8 -*-

from __future__ import absolute_import

from colour.utilities import CaseInsensitiveMapping
from .aces import (ACES_2065_1_COLOURSPACE, ACES_CC_COLOURSPACE,
                   ACES_CCT_COLOURSPACE, ACES_CG_COLOURSPACE,
                   ACES_PROXY_COLOURSPACE)
from .adobe_rgb_1998 import ADOBE_RGB_1998_COLOURSPACE
from .adobe_wide_gamut_rgb import ADOBE_WIDE_GAMUT_RGB_COLOURSPACE
from .apple_rgb import APPLE_RGB_COLOURSPACE
from .arri_alexa_wide_gamut import ALEXA_WIDE_GAMUT_COLOURSPACE
from .best_rgb import BEST_RGB_COLOURSPACE
from .beta_rgb import BETA_RGB_COLOURSPACE
from .cie_rgb import CIE_RGB_COLOURSPACE
from .canon_cinema_gamut import CINEMA_GAMUT_COLOURSPACE
from .color_match_rgb import COLOR_MATCH_RGB_COLOURSPACE
from .dcdm_xyz import DCDM_XYZ_COLOURSPACE
from .dci_p3 import DCI_P3_COLOURSPACE, DCI_P3_P_COLOURSPACE
from .display_p3 import DISPLAY_P3_COLOURSPACE
from .p3_d65 import P3_D65_COLOURSPACE
from .don_rgb_4 import DON_RGB_4_COLOURSPACE
from .dji_dgamut import DJI_D_GAMUT_COLOURSPACE
from .eci_rgb_v2 import ECI_RGB_V2_COLOURSPACE
from .ekta_space_ps5 import EKTA_SPACE_PS_5_COLOURSPACE
from .fujifilm_f_gamut import F_GAMUT_COLOURSPACE
from .filmlight_egamut import FILMLIGHT_E_GAMUT_COLOURSPACE
from .gopro import PROTUNE_NATIVE_COLOURSPACE
from .itur_bt_470 import BT470_525_COLOURSPACE, BT470_625_COLOURSPACE
from .itur_bt_709 import BT709_COLOURSPACE
from .itur_bt_2020 import BT2020_COLOURSPACE
from .max_rgb import MAX_RGB_COLOURSPACE
from .pal_secam import PAL_SECAM_COLOURSPACE
from .red import (RED_COLOR_COLOURSPACE, RED_COLOR_2_COLOURSPACE,
                  RED_COLOR_3_COLOURSPACE, RED_COLOR_4_COLOURSPACE,
                  DRAGON_COLOR_COLOURSPACE, DRAGON_COLOR_2_COLOURSPACE,
                  RED_WIDE_GAMUT_RGB_COLOURSPACE)
from .rimm_romm_rgb import (ROMM_RGB_COLOURSPACE, RIMM_RGB_COLOURSPACE,
                            ERIMM_RGB_COLOURSPACE, PROPHOTO_RGB_COLOURSPACE)
from .russell_rgb import RUSSELL_RGB_COLOURSPACE
from .sharp import SHARP_RGB_COLOURSPACE
from .smpte_240m import SMPTE_240M_COLOURSPACE
from .smpte_c import SMPTE_C_COLOURSPACE
from .ntsc import NTSC_1953_COLOURSPACE, NTSC_1987_COLOURSPACE
from .sony import (S_GAMUT_COLOURSPACE, S_GAMUT3_COLOURSPACE,
                   S_GAMUT3_CINE_COLOURSPACE, VENICE_S_GAMUT3_COLOURSPACE,
                   VENICE_S_GAMUT3_CINE_COLOURSPACE)
from .srgb import sRGB_COLOURSPACE
from .panasonic_v_gamut import V_GAMUT_COLOURSPACE
from .xtreme_rgb import XTREME_RGB_COLOURSPACE

RGB_COLOURSPACES = CaseInsensitiveMapping({
    ACES_2065_1_COLOURSPACE.name: ACES_2065_1_COLOURSPACE,
    ACES_CC_COLOURSPACE.name: ACES_CC_COLOURSPACE,
    ACES_CCT_COLOURSPACE.name: ACES_CCT_COLOURSPACE,
    ACES_PROXY_COLOURSPACE.name: ACES_PROXY_COLOURSPACE,
    ACES_CG_COLOURSPACE.name: ACES_CG_COLOURSPACE,
    ADOBE_RGB_1998_COLOURSPACE.name: ADOBE_RGB_1998_COLOURSPACE,
    ADOBE_WIDE_GAMUT_RGB_COLOURSPACE.name: ADOBE_WIDE_GAMUT_RGB_COLOURSPACE,
    APPLE_RGB_COLOURSPACE.name: APPLE_RGB_COLOURSPACE,
    ALEXA_WIDE_GAMUT_COLOURSPACE.name: ALEXA_WIDE_GAMUT_COLOURSPACE,
    BEST_RGB_COLOURSPACE.name: BEST_RGB_COLOURSPACE,
    BETA_RGB_COLOURSPACE.name: BETA_RGB_COLOURSPACE,
    BT470_525_COLOURSPACE.name: BT470_525_COLOURSPACE,
    BT470_625_COLOURSPACE.name: BT470_625_COLOURSPACE,
    BT709_COLOURSPACE.name: BT709_COLOURSPACE,
    BT2020_COLOURSPACE.name: BT2020_COLOURSPACE,
    CIE_RGB_COLOURSPACE.name: CIE_RGB_COLOURSPACE,
    CINEMA_GAMUT_COLOURSPACE.name: CINEMA_GAMUT_COLOURSPACE,
    COLOR_MATCH_RGB_COLOURSPACE.name: COLOR_MATCH_RGB_COLOURSPACE,
    DCDM_XYZ_COLOURSPACE.name: DCDM_XYZ_COLOURSPACE,
    DCI_P3_COLOURSPACE.name: DCI_P3_COLOURSPACE,
    DCI_P3_P_COLOURSPACE.name: DCI_P3_P_COLOURSPACE,
    DISPLAY_P3_COLOURSPACE.name: DISPLAY_P3_COLOURSPACE,
    DJI_D_GAMUT_COLOURSPACE.name: DJI_D_GAMUT_COLOURSPACE,
    DON_RGB_4_COLOURSPACE.name: DON_RGB_4_COLOURSPACE,
    ECI_RGB_V2_COLOURSPACE.name: ECI_RGB_V2_COLOURSPACE,
    EKTA_SPACE_PS_5_COLOURSPACE.name: EKTA_SPACE_PS_5_COLOURSPACE,
    FILMLIGHT_E_GAMUT_COLOURSPACE.name: FILMLIGHT_E_GAMUT_COLOURSPACE,
    PROTUNE_NATIVE_COLOURSPACE.name: PROTUNE_NATIVE_COLOURSPACE,
    MAX_RGB_COLOURSPACE.name: MAX_RGB_COLOURSPACE,
    P3_D65_COLOURSPACE.name: P3_D65_COLOURSPACE,
    PAL_SECAM_COLOURSPACE.name: PAL_SECAM_COLOURSPACE,
    RED_COLOR_COLOURSPACE.name: RED_COLOR_COLOURSPACE,
    RED_COLOR_2_COLOURSPACE.name: RED_COLOR_2_COLOURSPACE,
    RED_COLOR_3_COLOURSPACE.name: RED_COLOR_3_COLOURSPACE,
    RED_COLOR_4_COLOURSPACE.name: RED_COLOR_4_COLOURSPACE,
    RED_WIDE_GAMUT_RGB_COLOURSPACE.name: RED_WIDE_GAMUT_RGB_COLOURSPACE,
    DRAGON_COLOR_COLOURSPACE.name: DRAGON_COLOR_COLOURSPACE,
    DRAGON_COLOR_2_COLOURSPACE.name: DRAGON_COLOR_2_COLOURSPACE,
    ROMM_RGB_COLOURSPACE.name: ROMM_RGB_COLOURSPACE,
    RIMM_RGB_COLOURSPACE.name: RIMM_RGB_COLOURSPACE,
    ERIMM_RGB_COLOURSPACE.name: ERIMM_RGB_COLOURSPACE,
    F_GAMUT_COLOURSPACE.name: F_GAMUT_COLOURSPACE,
    PROPHOTO_RGB_COLOURSPACE.name: PROPHOTO_RGB_COLOURSPACE,
    RUSSELL_RGB_COLOURSPACE.name: RUSSELL_RGB_COLOURSPACE,
    SHARP_RGB_COLOURSPACE.name: SHARP_RGB_COLOURSPACE,
    SMPTE_240M_COLOURSPACE.name: SMPTE_240M_COLOURSPACE,
    SMPTE_C_COLOURSPACE.name: SMPTE_C_COLOURSPACE,
    NTSC_1953_COLOURSPACE.name: NTSC_1953_COLOURSPACE,
    NTSC_1987_COLOURSPACE.name: NTSC_1987_COLOURSPACE,
    S_GAMUT_COLOURSPACE.name: S_GAMUT_COLOURSPACE,
    S_GAMUT3_COLOURSPACE.name: S_GAMUT3_COLOURSPACE,
    S_GAMUT3_CINE_COLOURSPACE.name: S_GAMUT3_CINE_COLOURSPACE,
    VENICE_S_GAMUT3_COLOURSPACE.name: VENICE_S_GAMUT3_COLOURSPACE,
    VENICE_S_GAMUT3_CINE_COLOURSPACE.name: VENICE_S_GAMUT3_CINE_COLOURSPACE,
    sRGB_COLOURSPACE.name: sRGB_COLOURSPACE,
    V_GAMUT_COLOURSPACE.name: V_GAMUT_COLOURSPACE,
    XTREME_RGB_COLOURSPACE.name: XTREME_RGB_COLOURSPACE
})
RGB_COLOURSPACES.__doc__ = """
Aggregated *RGB* colourspaces.

RGB_COLOURSPACES : CaseInsensitiveMapping

Aliases:

-   'aces': ACES_2065_1_COLOURSPACE.name
-   'adobe1998': ADOBE_RGB_1998_COLOURSPACE.name
-   'prophoto': PROPHOTO_RGB_COLOURSPACE.name
"""
# yapf: disable
RGB_COLOURSPACES['aces'] = (
    RGB_COLOURSPACES[ACES_2065_1_COLOURSPACE.name])
RGB_COLOURSPACES['adobe1998'] = (
    RGB_COLOURSPACES[ADOBE_RGB_1998_COLOURSPACE.name])
RGB_COLOURSPACES['prophoto'] = (
    RGB_COLOURSPACES[PROPHOTO_RGB_COLOURSPACE.name])
# yapf: enable

__all__ = ['RGB_COLOURSPACES']
__all__ += [
    'ACES_2065_1_COLOURSPACE', 'ACES_CC_COLOURSPACE', 'ACES_CCT_COLOURSPACE',
    'ACES_PROXY_COLOURSPACE', 'ACES_CG_COLOURSPACE',
    'ADOBE_RGB_1998_COLOURSPACE', 'ADOBE_WIDE_GAMUT_RGB_COLOURSPACE',
    'ALEXA_WIDE_GAMUT_COLOURSPACE', 'APPLE_RGB_COLOURSPACE',
    'BEST_RGB_COLOURSPACE', 'BETA_RGB_COLOURSPACE', 'BT470_525_COLOURSPACE',
    'BT470_625_COLOURSPACE', 'BT709_COLOURSPACE', 'BT2020_COLOURSPACE',
    'CIE_RGB_COLOURSPACE', 'CINEMA_GAMUT_COLOURSPACE',
    'COLOR_MATCH_RGB_COLOURSPACE', 'DCDM_XYZ_COLOURSPACE',
    'DCI_P3_COLOURSPACE', 'DCI_P3_P_COLOURSPACE', 'DISPLAY_P3_COLOURSPACE',
    'DJI_D_GAMUT_COLOURSPACE', 'DON_RGB_4_COLOURSPACE',
    'ECI_RGB_V2_COLOURSPACE', 'EKTA_SPACE_PS_5_COLOURSPACE',
    'FILMLIGHT_E_GAMUT_COLOURSPACE', 'PROTUNE_NATIVE_COLOURSPACE',
    'MAX_RGB_COLOURSPACE', 'P3_D65_COLOURSPACE', 'PAL_SECAM_COLOURSPACE',
    'RED_COLOR_COLOURSPACE', 'RED_COLOR_2_COLOURSPACE',
    'RED_COLOR_3_COLOURSPACE', 'RED_COLOR_4_COLOURSPACE',
    'DRAGON_COLOR_COLOURSPACE', 'DRAGON_COLOR_2_COLOURSPACE',
    'RED_WIDE_GAMUT_RGB_COLOURSPACE', 'ROMM_RGB_COLOURSPACE',
    'RIMM_RGB_COLOURSPACE', 'ERIMM_RGB_COLOURSPACE',
    'PROPHOTO_RGB_COLOURSPACE', 'RUSSELL_RGB_COLOURSPACE',
    'SHARP_RGB_COLOURSPACE', 'SMPTE_240M_COLOURSPACE', 'SMPTE_C_COLOURSPACE',
    'NTSC_1953_COLOURSPACE', 'NTSC_1987_COLOURSPACE', 'S_GAMUT_COLOURSPACE',
    'S_GAMUT3_COLOURSPACE', 'S_GAMUT3_CINE_COLOURSPACE',
    'VENICE_S_GAMUT3_COLOURSPACE', 'VENICE_S_GAMUT3_CINE_COLOURSPACE',
    'sRGB_COLOURSPACE', 'V_GAMUT_COLOURSPACE', 'XTREME_RGB_COLOURSPACE',
    'F_GAMUT_COLOURSPACE'
]
