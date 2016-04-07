from __future__ import (unicode_literals, division, absolute_import,
                        print_function)

__license__   = 'GPL v3'
__copyright__ = '2015, dloraine'
__docformat__ = 'restructuredtext en'


# Define some column types
PERSON_TYPE = {"is_multiple": True, "is_names": True, "datatype": "text"}
TAG_TYPE    = {"is_multiple": True, "is_names": False, "datatype": "text"}
SINGLE_TYPE = {"is_multiple": False, "is_names": False, "datatype": "text"}
FLOAT_TYPE  = {"is_multiple": False, "is_names": False, "datatype": "float"}
SERIES_TYPE = {"is_multiple": False, "is_names": False, "datatype": "series"}

# Some constants for ease of reading
CONFIG_NAME = 0
CONFIG_TITLE = 1
CONFIG_DEFAULT = 2
CONFIG_COLUMN_TYPE = 3
CONFIG_DESCRIPTION = 1
CONFIG_TRIGGER_FUNC = 2
CONFIG_TRIGGER_ARG = 3
CONFIG_ARTISTS_COLUMNS = 0
CONFIG_OTHER_COLUMNS = 1
CONFIG_OPTIONS = 2
CONFIG_MAIN_BUTTON = 3
CONFIG_MENU = 4


def get_configuration():
    '''
    All configuration for preferences and the UI-Menu is made with the
    informations given here. No need to change anything in config.py or ui.py,
    if new preferences or menu items need to be made.

    Name: The internal name for the preference group
    Title: The Label in the config menu
    Type: Either "columnboxes" or "checkboxes"
    Columns: How many columns the group should have in the config menu
    Items: The preferences in the menu group. Has the form:
           [preference_name, displayed name, default_state, if column: columntype]
    UI_Action_Items: The buttons in the toolbar menu. Has the form:
           [name, displayed_text, triggerfunc, triggerfunc_arg]
    '''
    from calibre_plugins.EmbedComicMetadata.languages.lang import _L
    from calibre_plugins.EmbedComicMetadata.main import embed_into_comic, import_to_calibre, embed_cover, convert

    # configuration
    config = [
        {
            "Name": "artists_custom_columns",
            "Title": _L["Artists Custom Columns:"],
            "Type": "columnboxes",
            "Columns": 2,
            "Items": [
                ["penciller_column", _L['Penciller Column:'], None, PERSON_TYPE],
                ["inker_column", _L['Inker Column:'], None, PERSON_TYPE],
                ["colorist_column", _L['Colorist Column:'], None, PERSON_TYPE],
                ["letterer_column", _L['Letterer Column:'], None, PERSON_TYPE],
                ["cover_artist_column", _L['Cover Artist Column:'], None, PERSON_TYPE],
                ["editor_column", _L['Editor Column:'], None, PERSON_TYPE]
            ]
        },
        {
            "Name": "other_custom_columns",
            "Title": _L["Other Custom Columns:"],
            "Type": "columnboxes",
            "Columns": 2,
            "Items": [
                ["storyarc_column", _L['Story Arc Column:'], None, SINGLE_TYPE],
                ["characters_column", _L['Characters Column:'], None, TAG_TYPE],
                ["teams_column", _L['Teams Column:'], None, TAG_TYPE],
                ["locations_column", _L['Locations Column:'], None, TAG_TYPE],
                ["volume_column", _L['Volume Column:'], None, SINGLE_TYPE],
                ["genre_column", _L['Genre Column:'], None, TAG_TYPE]
            ]
        },
        {
            "Name": "options",
            "Title": _L["Options:"],
            "Type": "checkboxes",
            "Columns": 2,
            "Items": [
                ["cbi_embed", _L['Write metadata in zip comment'], True],
                ["cix_embed", _L['Write metadata in ComicInfo.xml'], True],
                ["read_cbi", _L['Import metadata from zip comment'], True],
                ["read_cix", _L['Import metadata from ComicInfo.xml'], True],
                ["convert_cbr", _L['Auto convert cbr to cbz'], True],
                ["convert_reading", _L['Auto convert while importing to calibre'], False],
                ["delete_cbr", _L['Delete cbr after conversion'], False],
                ["swap_names", _L['Swap names to "LN, FN" when importing metadata'], False],
                ["import_tags", _L['Import tags from comic metadata'], False],
                ["overwrite_calibre_tags", _L['If checked, overwrites the tags in calibre.'], False]
            ]
        },
        {
            "Name": "main_button",
            "Title": _L["Main Button Action (needs a calibre restart):"],
            "Type": "checkboxes",
            "Columns": 2,
            "Items": [
                ["main_embed", _L['Embed metadata'], True],
                ["main_import", _L['Import metadata'], False],
            ]
        },
        {
            "Name": "menu",
            "Title": _L["Menu Buttons:"],
            "Type": "checkboxes",
            "Columns": 2,
            "Items": [
                ["embed", _L['Show embed both button'], True],
                ["embedcbi", _L['Show embed cbi button'], False],
                ["embedcix", _L['Show embed cix button'], False],
                ["read_both", _L['Show import both button'], True],
                ["import_cix", _L['Show import cix button'], False],
                ["import_cbi", _L['Show import cbi button'], False],
                ["convert", _L['Show convert button'], True],
                ["cover", _L['Show embed cover button (experimental)'], False]
            ],
            "UI_Action_Items": [
                ["read_both", _L['Import Metadata from the comic archive into calibre'], import_to_calibre, "both"],
                ["import_cix", _L["Import Comic Rack Metadata from the comic archive into calibre"], import_to_calibre, "cix"],
                ["import_cbi", _L["Import Comment Metadata from the comic archive into calibre"], import_to_calibre, "cbi"],
                ["seperator"],
                ["embed", _L["Embed both Comic Metadata types"], embed_into_comic, "both"],
                ["embedcbi", _L["Only embed Metadata in zip comment"], embed_into_comic, "cbi"],
                ["embedcix", _L["Only embed Metadata in ComicInfo.xml"], embed_into_comic, "cix"],
                ["seperator"],
                ["convert", _L["Only convert cbr to cbz"], convert, None],
                ["cover", _L["Embed the calibre cover"], embed_cover, None],
                ["seperator"]
            ]
        }
    ]

    return config