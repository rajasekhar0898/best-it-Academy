class Config:
    
    """SECRET_KEY = 'secret'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://avnadmin:AVNS_dro4YtU_Jx8pbFN0OOc@mysql-class-rajasekharvadlamudi57-d7cd.a.aivencloud.com:12873/defaultdb'"""
    
    
    UPLOAD_FOLDERS = {
        'python': {
            'notes': 'upload_python_notes',
            'recordings': 'upload_python_recordings',
            'assignments': 'upload_python_assignments',
            'assessments': 'upload_python_assessments'
        },
        'java': {
            'notes': 'upload_java_notes',
            'recordings': 'upload_java_recordings',
            'assignments': 'upload_java_assignments',
            'assessments': 'upload_java_assessments'
        },
        'digitalmarketing': {
            'notes': 'upload_DigitalMarketing_notes',
            'recordings': 'upload_digitalmarketing_recordings',
            'assignments': 'upload_DigitalMarketing_assignments',
            'assessments': 'upload_DigitalMarketing_assessments'
        },
        'testingtools': {
            'notes': 'upload_testingtools_notes',
            'recordings': 'upload_testingtools_recordings',
            'assignments': 'upload_testingtools_assignments',
            'assessments': 'upload_testingtools_assessments'
        }
    }

