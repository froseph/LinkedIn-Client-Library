'''
All fields supported by the LinkedIn API. These are combined in selector lists
to retrieve specific information from the account represented by the current
access token.  Field selectors are described in detail at:

http://developer.linkedin.com/docs/DOC-1014

The following note of caution from the docs:

"Remember, each field you select adds computation time to your API request. 
It's best to be very specific as to what fields you want returned in each API call you make."

'''


LINKEDIN_PROFILE_FIELDS = [
    'id', 
    'first-name', 
    'last-name', 
    'headline', 
    'location:(name)', 
    'location:(country:(code))',
    'industry',
    'distance',
    'relation-to-viewer:(distance)',
    'relation-to-viewer:(num-related-connections)',
    'relation-to-viewer:(related-connections)',
    'connections', 
    'num-connections', 
    'num-connections-capped', 
    'summary', 
    'specialties', 
    'proposal-comments',
    'associations',
    'honors',
    'interests', 
    'positions',
    'publications',
    'patents',
    'languages',
    'skills',
    'certifications',
    'educations',
    'three-current-positions',
    'three-past-positions'     
    'num-recommenders', 
    'recommendations-received', 
    'phone-numbers', 
    'im-accounts',
    'twitter-accounts',
    'date-of-birth', 
    'main-address', 
    'member-url-resources',
    'member-url:(url)',
    'member-url:(name)',
    'picture-url',
    'site-standard-profile-request:(url)',
    'api-public-profile-request:(url)',
    'site-public-profile-request:(url)',
    'api-standard-profile-request:(url)',
    'api-standard-profile-request:(headers)',
    'public-profile-url'
]


LINKEDIN_POSITION_FIELDS = [
    'id',
    'title',
    'summary',
    'start-date',
    'end-date',
    'is-current',
    'company'
]

LINKEDIN_COMPANY_FIELDS = [
    'name',
    'type',
    'size',
    'industry',
    'ticker'
]

LINKEDIN_PUBLICATION_FIELDS = [
    'id',
    'title',
    'publisher:(name)',
    'authors:(id)',
    'authors:(name)',
    'authors:(person)',
    'date',
    'url',
    'summary'
]

LINKEDIN_PATENT_FIELDS = [
    'id',
    'title',
    'summary',
    'number',
    'status:(id)',
    'status:(name)',
    'office:(name)',
    'inventors:(id)',
    'inventors:(name)',
    'inventors:(person)',
    'date',
    'url'
]

LINKEDIN_LANGUAGE_FIELDS = [
    'id',
    'language:(name)',
    'proficiency:(level)',
    'proficiency:(name)'
]

LINKEDIN_SKILL_FIELDS = [
    'id',
    'skill:(name)',
    'proficiency:(level)',
    'proficiency:(name)',
    'years:(id)',
    'years:(name)'
]

LINKEDIN_CERTIFICATION_FIELDS = [
    'id',
    'name',
    'authority:(name)',
    'number',
    'start-date',
    'end-date'
]

LINKEDIN_EDUCATION_FIELDS = [
    'id',
    'school-name',
    'field-of-study',
    'start-date',
    'end-date',
    'degree',
    'activities',
    'notes'
]

LINKEDIN_RECOMMENDATION_FIELDS = [
    'id',
    'recommendation-type',
    'recommender'
]