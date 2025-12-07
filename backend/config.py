# -----------------------------------------------------
#  HEURISTICS CONFIGURATION FOR APP + WINDOW ANALYSIS
# -----------------------------------------------------
#  This file defines:
#     - Generic process name patterns
#     - Generic window title patterns
#     - Behavioral rules
#     - Thresholds for noise filtering
#
#  These patterns are NOT tied to specific apps.
#  They work dynamically across any system.
# -----------------------------------------------------


# -----------------------------------------------------
# 1. PROCESS PATTERNS
# -----------------------------------------------------
# Use substrings that identify categories of apps.
# These are general-purpose and work for any user.
# -----------------------------------------------------

PROCESS_PATTERNS = {
    
    #activities that need window tracking
    "browsers": [
        "chrome",
        "firefox",
        "edge",
        "yahoo",
        "opera",
    ],
    
    "office_apps": [
        "word",
        "excel",
        "powerpoint",
        "onenote",
        "acrobat",
        "pdf",
    ],

    #-----------------------------------------------------------
    
    #activities that don't need window tracking
    "system_apps": [
        "taskmgr",
        "settings",
        "control",
        "system",
        "explorer",
        "finder",
    ],
    
    
    "code_editors": [
        "code", #VScode
        "studio",  
        "pycharm",
        "sublime",
        "vim",
        "notepad++",
        "eclipse",
    ],
    
    "communication_apps": [
        "discord",
        "teams",
        "slack",
        "zoom",
    ],
}

#minimum interval threshold for a session
MIN_DURATION_IN_SECONDS = 3

