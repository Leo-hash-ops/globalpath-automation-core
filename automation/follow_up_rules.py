FOLLOW_UP_RULES = {
    'Study Abroad':   24,
    'Work Visa':      24,
    'Travel/Tourism': 12,
    'PR/Relocation':  48,
    'Consultation':    6,
    'default':        24,
}

def get_follow_up_hours(service):
    """
    Returns hours before follow-up needed for a service.
    Returns 24 if service not found.
    """
    return FOLLOW_UP_RULES.get(service, FOLLOW_UP_RULES['default'])
