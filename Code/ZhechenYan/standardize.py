def standardize(path):
	'''
	File name: extract_raw_output.py
	Author: Zhechen Yan
	Date created: 10/15/2016
	Date last modified: 10/15/2016
	Python Version: 3.5.2
	Desc: given the path and fields of the raw tsv file, extract the corresponding filds from it and output as a txt file.
	input type:
	path : str
	fields : list of str
	output : .txt file
	'''
	__author__ = "Zhechen Yan"
	__copyright__ = "Copyright 2016, Fung institute of Engineering, UC Berkeley"
	__credits__ = ["Zhechen Yan", "Jiahuan Chen", "Liangjing Zhu",
						"Guancheng Li", "Lee Fleming"]
	__version__ = "0.0.1"
	__maintainer__ = "Zhechen Yan"
	__email__ = "harry.yan@berkeley.edu"
	__status__ = "Research"
	
	# clear datas
	with open('./data/result.std.txt', 'w')as fw:
		pass

	abbreviations = {
    'ACADEMY': 'ACAD',
    'COMPANY': 'CO',
    'COMMITTEE': 'CMTE',
    'COLLEGE': 'COLL',
    'ASSOCIATIONS': 'ASSNS',
    'UNITED STATES': 'US',
    'COALITION': 'CLTN',
    'UNIVERSITY': 'UNIV',
    'INCORPORATED': 'INC',
    'FEDERAL': 'FED',
    'COLLEGES': 'COLLS',
    'NATIONAL': 'NAT',
    'FEDERATION': 'FEDN',
    'INTERNATIONAL': 'INT',
    'INSTITUTE': 'INST',
    'ASSOCIATION': 'ASSN',
    'EDUCATIONAL': 'ED',
    'DEPARTMENT': 'DEPT',
    'LIMITED': 'LTD',
    'CORPORATION': 'CORP',
    'ASSOCIATES': 'ASSOC',
    'DEVELOPMENT': 'DEV',
    'RESEARCH': 'RES',
    'CHEMICAL': 'CHEM',
    'SCIENTIFIC': 'SCI',
    'SCIENCES': 'SCI',
    'SCIENCE': 'SCI',
    'TECHNOLOGIES': 'TECH',
    'TECHNICAL':'TECH',
    'TECHNOLOGICAL': 'TECH',
    'PHARMACEUTICAL': 'PHARM',
    'ENGINEERING': 'ENG',
    'LABORATORY': 'LAB',
    'INDUSTRY': 'IND',
    'INDUSTRIES': 'IND',
    'AKTIENGESESELLSCHAFT': 'AG',
    'AND': '&',
    'THE': '',
    'BY': ''
    }
	univ = {
 'BOARD OF GOVERNORS': '',
 'BOARD OF GOVERNORS OF': '',
 'BOARD OF GOVERNORS OF THE': '',
 'BOARD OF REGENTS': '',
 'BOARD OF REGENTS OF': '',
 'BOARD OF REGENTS OF THE': '',
 'BOARD OF SUPERVISORS': '',
 'BOARD OF SUPERVISORS OF': '',
 'BOARD OF SUPERVISORS OF THE': '',
 'BOARD OF TRUSTEES': '',
 'BOARD OF TRUSTEES OF': '',
 'BOARD OF TRUSTEES OF THE': '',
 'BOARD OF TRUSTEES OPERATING': '',
 'CURATORS': '',
 'CURATORS OF THE': '',
 'GOVERNORS': '',
 'GOVERNORS OF': '',
 'GOVERNORS OF THE': '',
 'REGENTS': '',
 'REGENTS OF': '',
 'REGENTS OF THE': '',
 'SUPERVISORS': '',
 'SUPERVISORS OF': '',
 'SUPERVISORS OF THE': '',
 'THE': '',
 'TRUSTEES': '',
 'TRUSTEES OF': '',
 'TRUSTEES OF THE': ''}

	derwent = {
	'A B': 'AB',
	'A CALIFORNIA CORP': 'CORP',
	'A DELAWARE CORP': 'CORP',
	'A/S': 'AS',
	'ACADEMY': 'ACAD',
	'ACTIEN GESELLSCHAFT': 'AG',
	'ACTIENGESELLSCHAFT': 'AG',
	'AGRICOLA': 'AGRIC',
	'AGRICOLAS': 'AGRIC',
	'AGRICOLE': 'AGRIC',
	'AGRICOLES': 'AGRIC',
	'AGRICOLI': 'AGRIC',
	'AGRICOLTURE': 'AGRIC',
	'AGRICULTURA': 'AGRIC',
	'AGRICULTURAL': 'AGRIC',
	'AGRICULTURE': 'AGRIC',
	'AKADEMI': 'AKAD',
	'AKADEMIA': 'AKAD',
	'AKADEMIE': 'AKAD',
	'AKADEMIEI': 'AKAD',
	'AKADEMII': 'AKAD',
	'AKADEMIJA': 'AKAD',
	'AKADEMIYA': 'AKAD',
	'AKADEMIYAKH': 'AKAD',
	'AKADEMIYAM': 'AKAD',
	'AKADEMIYAMI': 'AKAD',
	'AKADEMIYU': 'AKAD',
	'AKTIEBOLAG': 'AB',
	'AKTIEBOLAGET': 'AB',
	'AKTIEN GESELLSCHAFT': 'AG',
	'AKTIENGESELLSCHAFT': 'AG',
	'AKTIESELSKAB': 'AS',
	'AKTIESELSKABET': 'AS',
	'ALLGEMEINE': 'ALLG',
	'ALLGEMEINER': 'ALLG',
	'ANPARTSSELSKAB': 'APS',
	'ANPARTSSELSKABET': 'APS',
	'ANTREPRIZA': 'ANTR',
	'APARARII': 'APAR',
	'APARATE': 'APAR',
	'APARATELOR': 'APAR',
	'APPARATE': 'APP',
	'APPARATEBAU': 'APP',
	'APPARATUS': 'APP',
	'APPARECHHI': 'APP',
	'APPAREIL': 'APP',
	'APPAREILLAGE': 'APP',
	'APPAREILLAGES': 'APP',
	'APPAREILS': 'APP',
	'APPLICATION': 'APPL',
	'APPLICATIONS': 'APPL',
	'APPLICAZIONE': 'APPL',
	'APPLICAZIONI': 'APPL',
	'ASSOCIACAO': 'ASSOC',
	'ASSOCIATE': 'ASSOCIATES',
	'ASSOCIATED': 'ASSOC',
	'ASSOCIATES': 'ASSOCIATES',
	'ASSOCIATION': 'ASSOC',
	'BEPERKTE AANSPRAKELIJKHEID': 'PVBA',
	'BESCHRANKTER HAFTUNG': 'BET GMBH',
	'BESLOTEN VENNOOTSCHAP': 'BV',
	'BESLOTEN VENNOOTSCHAP MET': 'BV',
	'BETEILIGUNGS GESELLSCHAFT MIT': 'BET GMBH',
	'BETEILIGUNGSGESELLSCHAFT': 'BET GES',
	'BETEILIGUNGSGESELLSCHAFT MBH': 'BET GMBH',
	'BRODERNA': 'BRDR',
	'BRODRENE': 'BRDR',
	'BROEDERNA': 'BRDR',
	'BROEDRENE': 'BRDR',
	'BROTHERS': 'BROS',
	'CENTER': 'CENT',
	'CENTRAAL': 'CENT',
	'CENTRAL': 'CENT',
	'CENTRALA': 'CENT',
	'CENTRALE': 'CENT',
	'CENTRALES': 'CENT',
	'CENTRAUX': 'CENT',
	'CENTRE': 'CENT',
	'CENTRO': 'CENT',
	'CENTRUL': 'CENT',
	'CENTRUM': 'CENT',
	'CERCETARE': 'CERC',
	'CERCETARI': 'CERC',
	'CHEMICAL': 'CHEM',
	'CHEMICALS': 'CHEM',
	'CHEMICKE': 'CHEM',
	'CHEMICKEJ': 'CHEM',
	'CHEMICKY': 'CHEM',
	'CHEMICKYCH': 'CHEM',
	'CHEMICZNE': 'CHEM',
	'CHEMICZNY': 'CHEM',
	'CHEMIE': 'CHEM',
	'CHEMII': 'CHEM',
	'CHEMISCH': 'CHEM',
	'CHEMISCHE': 'CHEM',
	'CHEMISKEJ': 'CHEM',
	'CHEMISTRY': 'CHEM',
	'CHIMIC': 'CHIM',
	'CHIMICA': 'CHIM',
	'CHIMICE': 'CHIM',
	'CHIMICI': 'CHIM',
	'CHIMICO': 'CHIM',
	'CHIMIE': 'CHIM',
	'CHIMIEI': 'CHIM',
	'CHIMIESKOJ': 'CHIM',
	'CHIMII': 'CHIM',
	'CHIMIKO': 'CHIM',
	'CHIMIQUE': 'CHIM',
	'CHIMIQUES': 'CHIM',
	'CHIMIYA': 'CHIM',
	'CHIMIYAKH': 'CHIM',
	'CHIMIYAM': 'CHIM',
	'CHIMIYAMI': 'CHIM',
	'CHIMIYU': 'CHIM',
	'CLOSE CORPORATION': 'CC',
	'CO OPERATIVE': 'COOP',
	'CO OPERATIVES': 'COOP',
	'COMBINATUL': 'COMB',
	'COMMERCIAL': 'COMML',
	'COMMERCIALE': 'COMML',
	'COMPAGNIA': 'CIA',
	'COMPAGNIE': 'CIE',
	'COMPAGNIE FRANCAISE': 'CIE FR',
	'COMPAGNIE GENERALE': 'CIE GEN',
	'COMPAGNIE INDUSTRIALE': 'CIE IND',
	'COMPAGNIE INDUSTRIELLE': 'CIE IND',
	'COMPAGNIE INDUSTRIELLES': 'CIE IND',
	'COMPAGNIE INTERNATIONALE': 'CIE INT',
	'COMPAGNIE NATIONALE': 'CIE NAT',
	'COMPAGNIE PARISIEN': 'CIE PARIS',
	'COMPAGNIE PARISIENN': 'CIE PARIS',
	'COMPAGNIE PARISIENNE': 'CIE PARIS',
	'COMPANHIA': 'CIA',
	'COMPANIES': 'CO',
	'COMPANY': 'CO',
	'CONSOLIDATED': 'CONSOL',
	'CONSTRUCCION': 'CONSTR',
	'CONSTRUCCIONE': 'CONSTR',
	'CONSTRUCCIONES': 'CONSTR',
	'CONSTRUCTIE': 'CONSTR',
	'CONSTRUCTII': 'CONSTR',
	'CONSTRUCTIILOR': 'CONSTR',
	'CONSTRUCTION': 'CONSTR',
	'CONSTRUCTIONS': 'CONSTR',
	'CONSTRUCTOR': 'CONSTR',
	'CONSTRUCTORTUL': 'CONSTR',
	'CONSTRUCTORUL': 'CONSTR',
	'COOPERATIEVE': 'COOP',
	'COOPERATION': 'COOP',
	'COOPERATIVA': 'COOP',
	'COOPERATIVE': 'COOP',
	'COOPERATIVES': 'COOP',
	'CORPORASTION': 'CORP',
	'CORPORATE': 'CORP',
	'CORPORATION': 'CORP',
	'CORPORATION OF AMERICA': 'CORP',
	'CORPORATIOON': 'CORP',
	'COSTRUZIONI': 'COSTR',
	'DEMOKRATISCHE REPUBLIK': 'DDR',
	'DEMOKRATISCHEN REPUBLIK': 'DDR',
	'DEPARTEMENT': 'DEPT',
	'DEPARTMENT': 'DEPT',
	'DEUTSCH': 'DEUT',
	'DEUTSCHE': 'DEUT',
	'DEUTSCHEN': 'DEUT',
	'DEUTSCHER': 'DEUT',
	'DEUTSCHES': 'DEUT',
	'DEUTSCHLAND': 'DEUT',
	'DEVELOP': 'DEV',
	'DEVELOPMENT': 'DEV',
	'DEVELOPMENTS': 'DEV',
	'DEVELOPPEMENT': 'DEV',
	'DEVELOPPEMENTS': 'DEV',
	'DIVISION': 'DIV',
	'DIVISIONE': 'DIV',
	'EINGETRAGENER VEREIN': 'EV',
	'ENGINEERING': 'ENG',
	'EQUIPEMENT': 'EQUIP',
	'EQUIPEMENTS': 'EQUIP',
	'EQUIPMENT': 'EQUIP',
	'EQUIPMENTS': 'EQUIP',
	'ESTABLISHMENT': 'ESTAB',
	'ESTABLISHMENTS': 'ESTAB',
	'ESTABLISSEMENT': 'ESTAB',
	'ESTABLISSEMENTS': 'ESTAB',
	'ETABLISSEMENT': 'ETAB',
	'ETABLISSEMENTS': 'ETAB',
	'ETABS': 'ETAB',
	'ETS': 'ETAB',
	'ETUDE': 'ETUD',
	'ETUDES': 'ETUD',
	'EUROPAEISCHE': 'EURO',
	'EUROPAEISCHEN': 'EURO',
	'EUROPAEISCHES': 'EURO',
	'EUROPAISCHE': 'EURO',
	'EUROPAISCHEN': 'EURO',
	'EUROPAISCHES': 'EURO',
	'EUROPE': 'EURO',
	'EUROPEA': 'EURO',
	'EUROPEAN': 'EURO',
	'EUROPEEN': 'EURO',
	'EUROPEENNE': 'EURO',
	'EXPLOATERING': 'EXPL',
	'EXPLOATERINGS': 'EXPL',
	'EXPLOITATIE': 'EXPL',
	'EXPLOITATION': 'EXPL',
	'EXPLOITATIONS': 'EXPL',
	'F LLI': 'FRAT',
	'FABBRICA': 'FAB',
	'FABBRICAZIONI': 'FAB',
	'FABBRICHE': 'FAB',
	'FABRICA': 'FAB',
	'FABRICATION': 'FAB',
	'FABRICATIONS': 'FAB',
	'FABRIEK': 'FAB',
	'FABRIEKEN': 'FAB',
	'FABRIK': 'FAB',
	'FABRIKER': 'FAB',
	'FABRIQUE': 'FAB',
	'FABRIQUES': 'FAB',
	'FABRIZIO': 'FAB',
	'FABRYKA': 'FAB',
	'FARMACEUTICA': 'FARM',
	'FARMACEUTICE': 'FARM',
	'FARMACEUTICHE': 'FARM',
	'FARMACEUTICI': 'FARM',
	'FARMACEUTICO': 'FARM',
	'FARMACEUTICOS': 'FARM',
	'FARMACEUTISK': 'FARM',
	'FARMACEVTSKIH': 'FARM',
	'FARMACIE': 'FARM',
	'FIRMA': 'FA',
	'FLLI': 'FRAT',
	'FONDATION': 'FOND',
	'FONDAZIONE': 'FOND',
	'FOUNDATION': 'FOUND',
	'FOUNDATIONS': 'FOUND',
	'FRANCAIS': 'FR',
	'FRANCAISE': 'FR',
	'FRATELLI': 'FRAT',
	'GAKKO HOJIN': 'GH',
	'GAKKO HOUJIN': 'GH',
	'GEB': 'GEBR',
	'GEBRODER': 'GEBR',
	'GEBRODERS': 'GEBR',
	'GEBROEDER': 'GEBR',
	'GEBROEDERS': 'GEBR',
	'GEBRUDER': 'GEBR',
	'GEBRUDERS': 'GEBR',
	'GEBRUEDER': 'GEBR',
	'GEBRUEDERS': 'GEBR',
	'GENERAL': 'GEN',
	'GENERALA': 'GEN',
	'GENERALE': 'GEN',
	'GENERALES': 'GEN',
	'GENERAUX': 'GEN',
	'GESELLSCHAFT': 'GES',
	'GESELLSCHAFT MBH': 'GMBH',
	'GESELLSCHAFT MIT BESCHRANKTER HAFTUNG': 'GMBH',
	'GEWERKSCHAFT': 'GEW',
	'GOMEI GAISHA': 'GK',
	'GOMEI KAISHA': 'GK',
	'GOSHI KAISHA': 'GK',
	'GOUSHI GAISHA': 'GK',
	'GROUPEMENT': 'GRP',
	'GROUPMENT': 'GRP',
	'GUTEHOFFNUNGSCHUETTE': 'GHH',
	'GUTEHOFFNUNGSCHUTTE': 'GHH',
	'HANDELS BOLAGET': 'HB',
	'HANDELSBOLAGET': 'HB',
	'HANDELSMAATSCHAPPIJ': 'HANDL',
	'HANDELSMIJ': 'HANDL',
	'HER MAJESTY THE QUEEN': 'UK',
	'HER MAJESTY THE QUEEN IN RIGHT OF CANADA AS REPRESENTED BY THE MINISTER OF': 'CANADA MIN OF',
	'INCORPORATED': 'INC',
	'INCORPORATION': 'INC',
	'INDUSTRI': 'IND',
	'INDUSTRIA': 'IND',
	'INDUSTRIAL': 'IND',
	'INDUSTRIALA': 'IND',
	'INDUSTRIALE': 'IND',
	'INDUSTRIALI': 'IND',
	'INDUSTRIALIZARE': 'IND',
	'INDUSTRIALIZAREA': 'IND',
	'INDUSTRIALS': 'IND',
	'INDUSTRIAS': 'IND',
	'INDUSTRIE': 'IND',
	'INDUSTRIEELE': 'IND',
	'INDUSTRIEI': 'IND',
	'INDUSTRIEL': 'IND',
	'INDUSTRIELL': 'IND',
	'INDUSTRIELLE': 'IND',
	'INDUSTRIELLES': 'IND',
	'INDUSTRIELS': 'IND',
	'INDUSTRIER': 'IND',
	'INDUSTRIES': 'IND',
	'INDUSTRII': 'IND',
	'INDUSTRIJ': 'IND',
	'INDUSTRIYA': 'IND',
	'INDUSTRIYAKH': 'IND',
	'INDUSTRIYAM': 'IND',
	'INDUSTRIYAMI': 'IND',
	'INDUSTRIYU': 'IND',
	'INDUSTRY': 'IND',
	'INGENIER': 'ING',
	'INGENIERIA': 'ING',
	'INGENIEUR': 'ING',
	'INGENIEURBUERO': 'ING',
	'INGENIEURBUREAU': 'ING',
	'INGENIEURBURO': 'ING',
	'INGENIEURGESELLSCHAFT': 'ING',
	'INGENIEURS': 'ING',
	'INGENIEURSBUREAU': 'ING',
	'INGENIEURTECHNISCHE': 'ING',
	'INGENIEURTECHNISCHES': 'ING',
	'INGENIOERFIRMAET': 'ING',
	'INGENIORSFIRMA': 'ING',
	'INGENIORSFIRMAN': 'ING',
	'INGENJORSFIRMA': 'ING',
	'INGINERIE': 'ING',
	'INSINOORITOMISTO': 'INSTMSTO',
	'INSTITUT': 'INST',
	'INSTITUT FRANCAIS': 'INST FR',
	'INSTITUT NATIONAL': 'INST NAT',
	'INSTITUTA': 'INST',
	'INSTITUTAM': 'INST',
	'INSTITUTAMI': 'INST',
	'INSTITUTAMKH': 'INST',
	'INSTITUTE': 'INST',
	'INSTITUTE FRANCAISE': 'INST FR',
	'INSTITUTE NATIONALE': 'INST NAT',
	'INSTITUTES': 'INST',
	'INSTITUTET': 'INST',
	'INSTITUTO': 'INST',
	'INSTITUTOM': 'INST',
	'INSTITUTOV': 'INST',
	'INSTITUTT': 'INST',
	'INSTITUTU': 'INST',
	'INSTITUTUL': 'INST',
	'INSTITUTY': 'INST',
	'INSTITUUT': 'INST',
	'INSTITZHT': 'INST',
	'INSTRUMENT': 'INSTR',
	'INSTRUMENTATION': 'INSTR',
	'INSTRUMENTE': 'INSTR',
	'INSTRUMENTS': 'INSTR',
	'INSTYTUT': 'INST',
	'INTERNACIONAL': 'INT',
	'INTERNATIONAL': 'INT',
	'INTERNATIONALE': 'INT',
	'INTERNATIONALEN': 'INT',
	'INTERNATIONAUX': 'INT',
	'INTERNATIONELLA': 'INT',
	'INTERNATL': 'INT',
	'INTERNAZIONALE': 'INT',
	'INTL': 'INT',
	'INTREPRINDEREA': 'INTR',
	'ISTITUTO': 'IST',
	'ITALI': 'ITAL',
	'ITALIA': 'ITAL',
	'ITALIAN': 'ITAL',
	'ITALIANA': 'ITAL',
	'ITALIANE': 'ITAL',
	'ITALIANI': 'ITAL',
	'ITALIANO': 'ITAL',
	'ITALIEN': 'ITAL',
	'ITALIENNE': 'ITAL',
	'ITALO': 'ITAL',
	'ITALY': 'ITAL',
	'JUNIOR': 'JR',
	'KABUSHIKI GAISHA': 'KK',
	'KABUSHIKI GAISYA': 'KK',
	'KABUSHIKI KAISHA': 'KK',
	'KABUSHIKI KAISYA': 'KK',
	'KABUSHIKIGAISHA': 'KK',
	'KABUSHIKIGAISYA': 'KK',
	'KABUSHIKIKAISHA': 'KK',
	'KABUSHIKIKAISYA': 'KK',
	'KOMBINAT': 'KOMB',
	'KOMBINATU': 'KOMB',
	'KOMBINATY': 'KOMB',
	'KOMMANDIT BOLAG': 'KB',
	'KOMMANDIT BOLAGET': 'KB',
	'KOMMANDIT GESELLSCHAFT': 'KG',
	'KOMMANDIT GESELLSCHAFT AUF AKTIEN': 'KGAA',
	'KOMMANDITBOLAG': 'KB',
	'KOMMANDITBOLAGET': 'KB',
	'KOMMANDITGESELLSCHAFT': 'KG',
	'KOMMANDITGESELLSCHAFT AUF AKTIEN': 'KGAA',
	'KONCERNOVY PODNIK': 'KP',
	'KONINKLIJKE': 'KONINK',
	'KUNSTSTOFF': 'KUNST',
	'KUNSTSTOFFTECHNIK': 'KUNST',
	'KUTATO INTEZET': 'KI',
	'KUTATO INTEZETE': 'KI',
	'KUTATOINTEZET': 'KI',
	'KUTATOINTEZETE': 'KI',
	'LABORATOIR': 'LAB',
	'LABORATOIRE': 'LAB',
	'LABORATOIRES': 'LAB',
	'LABORATORI': 'LAB',
	'LABORATORIEI': 'LAB',
	'LABORATORIES': 'LAB',
	'LABORATORII': 'LAB',
	'LABORATORIJ': 'LAB',
	'LABORATORIO': 'LAB',
	'LABORATORIOS': 'LAB',
	'LABORATORIUM': 'LAB',
	'LABORATORY': 'LAB',
	'LABORTORI': 'LAB',
	'LAVORAZA': 'LAVORAZ',
	'LAVORAZI': 'LAVORAZ',
	'LAVORAZIO': 'LAVORAZ',
	'LAVORAZIONE': 'LAVORAZ',
	'LAVORAZIONI': 'LAVORAZ',
	'LIMITADA': 'LTDA',
	'LIMITED': 'LTD',
	'LIMITED PARTNERSHIP': 'LP',
	'LTD LTEE': 'LTD',
	'MAATSCHAPPIJ': 'MIJ',
	'MAGYAR TUDOMANYOS AKADEMIA': 'MTA',
	'MANIFATTURA': 'MFR',
	'MANIFATTURAS': 'MFR',
	'MANIFATTURE': 'MFR',
	'MANUFACTURAS': 'MFR',
	'MANUFACTURE': 'MFR',
	'MANUFACTURER': 'MFR',
	'MANUFACTURERS': 'MFR',
	'MANUFACTURES': 'MFR',
	'MANUFACTURING': 'MFG',
	'MANUFACTURINGS': 'MFG',
	'MANUFATURA': 'MFR',
	'MASCHIN': 'MASCH',
	'MASCHINEN': 'MASCH',
	'MASCHINENBAU': 'MASCHBAU',
	'MASCHINENBAUANSTALT': 'MASCHBAU',
	'MASCHINENFAB': 'MASCHFAB',
	'MASCHINENFABRIEK': 'MASCHFAB',
	'MASCHINENFABRIK': 'MASCHFAB',
	'MASCHINENFABRIKEN': 'MASCHFAB',
	'MASCHINENVERTRIEB': 'MASCH',
	'MEDICAL': 'MED',
	'MINISTER': 'MIN',
	'MINISTERE': 'MIN',
	'MINISTERIUM': 'MIN',
	'MINISTERO': 'MIN',
	'MINISTERSTV': 'MIN',
	'MINISTERSTVA': 'MIN',
	'MINISTERSTVAKH': 'MIN',
	'MINISTERSTVAM': 'MIN',
	'MINISTERSTVAMI': 'MIN',
	'MINISTERSTVE': 'MIN',
	'MINISTERSTVO': 'MIN',
	'MINISTERSTVOM': 'MIN',
	'MINISTERSTVU': 'MIN',
	'MINISTERSTWO': 'MIN',
	'MINISTERUL': 'MIN',
	'MINISTRE': 'MIN',
	'MINISTRY': 'MIN',
	'MIT BESCHRANKTER HAFTUNG': 'MBH',
	'N V': 'NV',
	'NAAMLOOSE VENOOTSCHAP': 'NV',
	'NAAMLOZE VENNOOTSCHAP': 'NV',
	'NARODNI PODNIK': 'NP',
	'NARODNIJ PODNIK': 'NP',
	'NARODNY PODNIK': 'NP',
	'NATIONAAL': 'NAT',
	'NATIONAL': 'NAT',
	'NATIONALE': 'NAT',
	'NATIONAUX': 'NAT',
	'NATL': 'NAT',
	'NAZIONALE': 'NAZ',
	'NAZIONALI': 'NAZ',
	'NORDDEUTSCH': 'NORDDEUT',
	'NORDDEUTSCHE': 'NORDDEUT',
	'NORDDEUTSCHER': 'NORDDEUT',
	'NORDDEUTSCHES': 'NORDDEUT',
	'OBOROVY PODNIK': 'OP',
	'OESTERREICH': 'OESTERR',
	'OESTERREICHISCH': 'OESTERR',
	'OESTERREICHISCHE': 'OESTERR',
	'OESTERREICHISCHES': 'OESTERR',
	'OFFENE HANDELSGESELLSCHAFT': 'OHG',
	'OFFICINE MECCANICA': 'OFF MEC',
	'OFFICINE MECCANICHE': 'OFF MEC',
	'OFFICINE NATIONALE': 'OFF NAT',
	'ONTWIKKELINGS': 'ONTWIK',
	'ONTWIKKELINGSBUREAU': 'ONTWIK',
	'ORGANISATIE': 'ORG',
	'ORGANISATION': 'ORG',
	'ORGANISATIONS': 'ORG',
	'ORGANIZATION': 'ORG',
	'ORGANIZATIONS': 'ORG',
	'ORGANIZZAZIONE': 'ORG',
	'OSAKEYHTIO': 'OY',
	'OSTERREICH': 'OESTERR',
	'OSTERREICHISCH': 'OESTERR',
	'OSTERREICHISCHE': 'OESTERR',
	'OSTERREICHISCHES': 'OESTERR',
	'PERSONENVENNOOTSCHAP MET': 'PVBA',
	'PHARMACEUTICA': 'PHARM',
	'PHARMACEUTICAL': 'PHARM',
	'PHARMACEUTICALS': 'PHARM',
	'PHARMACEUTIQUE': 'PHARM',
	'PHARMACEUTIQUES': 'PHARM',
	'PHARMAZEUTIKA': 'PHARM',
	'PHARMAZEUTISCH': 'PHARM',
	'PHARMAZEUTISCHE': 'PHARM',
	'PHARMAZEUTISCHEN': 'PHARM',
	'PHARMAZIE': 'PHARM',
	'PRELUCRARE': 'PRELUC',
	'PRELUCRAREA': 'PRELUC',
	'PRODOTTI': 'PROD',
	'PRODUCE': 'PROD',
	'PRODUCT': 'PROD',
	'PRODUCTA': 'PROD',
	'PRODUCTAS': 'PROD',
	'PRODUCTIE': 'PROD',
	'PRODUCTION': 'PRODN',
	'PRODUCTIONS': 'PRODN',
	'PRODUCTO': 'PROD',
	'PRODUCTORES': 'PROD',
	'PRODUCTOS': 'PROD',
	'PRODUCTS': 'PROD',
	'PRODUIT': 'PROD',
	'PRODUIT CHIMIQUE': 'PROD CHIM',
	'PRODUIT CHIMIQUES': 'PROD CHIM',
	'PRODUITS': 'PROD',
	'PRODUKCJI': 'PROD',
	'PRODUKT': 'PROD',
	'PRODUKTE': 'PROD',
	'PRODUKTER': 'PROD',
	'PRODUKTION': 'PRODN',
	'PRODUKTIONS': 'PRODN',
	'PRODUSE': 'PROD',
	'PRODUTOS': 'PROD',
	'PRODUZIONI': 'PRODN',
	'PROIECTARE': 'PROI',
	'PROIECTARI': 'PROI',
	'PROPRIETARY': 'PTY',
	'PRZEDSIEBIOSTWO': 'PRZEDSIEB',
	'PRZEMYSLU': 'PRZEYM',
	'PUBLIC LIMITED COMPANY': 'PLC',
	'REALISATION': 'REAL',
	'REALISATIONS': 'REAL',
	'RECHERCHE': 'RECH',
	'RECHERCHE ET DEVELOPMENT': 'RECH & DEV',
	'RECHERCHE ET DEVELOPPEMENT': 'RECH & DEV',
	'RECHERCHES': 'RECH',
	'RECHERCHES ET DEVELOPMENTS': 'RECH & DEV',
	'RECHERCHES ET DEVELOPPEMENTS': 'RECH & DEV',
	'RESEARCH': 'RES',
	'RESEARCH & DEVELOPMENT': 'RES & DEV',
	'RESEARCH AND DEVELOPMENT': 'RES & DEV',
	'RIJKSUNIVERSITEIT': 'RIJKSUNIV',
	'SA DITE': 'SA',
	'SCHWEIZER': 'SCHWEIZ',
	'SCHWEIZERISCH': 'SCHWEIZ',
	'SCHWEIZERISCHE': 'SCHWEIZ',
	'SCHWEIZERISCHER': 'SCHWEIZ',
	'SCHWEIZERISCHES': 'SCHWEIZ',
	'SCIENCE': 'SCI',
	'SCIENCES': 'SCI',
	'SCIENTIFIC': 'SCI',
	'SCIENTIFICA': 'SCI',
	'SCIENTIFIQUE': 'SCI',
	'SCIENTIFIQUES': 'SCI',
	'SDRUZENI PODNIK': 'SP',
	'SDRUZENI PODNIKU': 'SP',
	'SECREATRY': 'SECRETARY',
	'SECRETARY': 'SEC',
	'SECRETARY OF STATE FOR': 'UK SEC FOR',
	'SECRETATY': 'SECRETARY',
	'SECRETRY': 'SECRETARY',
	'SHADAN HOJIN': 'SH',
	'SIDERURGIC': 'SIDER',
	'SIDERURGICA': 'SIDER',
	'SIDERURGICAS': 'SIDER',
	'SIDERURGIE': 'SIDER',
	'SIDERURGIQUE': 'SIDER',
	'SOCIEDAD': 'SOC',
	'SOCIEDAD ANONIMA': 'SA',
	'SOCIEDAD CIVIL': 'SOC CIV',
	'SOCIEDAD DE RESPONSABILIDAD LIMITADA': 'SRL',
	'SOCIEDAD ESPANOLA': 'SOC ESPAN',
	'SOCIEDADE': 'SOC',
	'SOCIETA': 'SOC',
	'SOCIETA APPLICAZIONE': 'SOC APPL',
	'SOCIETA IN ACCOMANDITA SEMPLICE': 'SAS',
	'SOCIETA IN NOME COLLECTIVO': 'SNC',
	'SOCIETA PER AZIONI': 'SPA',
	'SOCIETE': 'SOC',
	'SOCIETE A RESPONSABILITE LIMITEE': 'SARL',
	'SOCIETE A RESPONSIBILITE LIMITEE': 'SARL',
	'SOCIETE ALSACIENNE': 'SOC ALSAC',
	'SOCIETE ANONYME': 'SA',
	'SOCIETE ANONYME DITE': 'SA',
	'SOCIETE APPLICATION': 'SOC APPL',
	'SOCIETE AUXILIAIRE': 'SOC AUX',
	'SOCIETE CHIMIQUE': 'SOC CHIM',
	'SOCIETE CIVILE': 'SOC CIV',
	'SOCIETE COMMERCIALE': 'SOC COMML',
	'SOCIETE COMMERCIALES': 'SOC COMML',
	'SOCIETE EN NOM COLLECTIF': 'SNC',
	'SOCIETE ETUDE': 'SOC ETUD',
	'SOCIETE ETUDES': 'SOC ETUD',
	'SOCIETE EXPLOITATION': 'SOC EXPL',
	'SOCIETE GENERALE': 'SOC GEN',
	'SOCIETE INDUSTRIELLE': 'SOC IND',
	'SOCIETE INDUSTRIELLES': 'SOC IND',
	'SOCIETE MECANIQUE': 'SOC MEC',
	'SOCIETE MECANIQUES': 'SOC MEC',
	'SOCIETE NATIONALE': 'SOC NAT',
	'SOCIETE NOUVELLE': 'SOC NOUV',
	'SOCIETE PARISIEN': 'SOC PARIS',
	'SOCIETE PARISIENN': 'SOC PARIS',
	'SOCIETE PARISIENNE': 'SOC PARIS',
	'SOCIETE PRIVEE A RESPONSABILITE LIMITEE': 'SPRL',
	'SOCIETE TECHNIQUE': 'SOC TECH',
	'SOCIETE TECHNIQUES': 'SOC TECH',
	'SOCIETY': 'SOC',
	'SPITALUL': 'SPITAL',
	'STIINTIFICA': 'STIINT',
	'SUDDEUTSCH': 'SUDDEUT',
	'SUDDEUTSCHE': 'SUDDEUT',
	'SUDDEUTSCHER': 'SUDDEUT',
	'SUDDEUTSCHES': 'SUDDEUT',
	'TECHNICAL': 'TECH',
	'TECHNICO': 'TECH',
	'TECHNICZNY': 'TECH',
	'TECHNIK': 'TECH',
	'TECHNIKAI': 'TECH',
	'TECHNIKI': 'TECH',
	'TECHNIQUE': 'TECH',
	'TECHNIQUES': 'TECH',
	'TECHNISCH': 'TECH',
	'TECHNISCHE': 'TECH',
	'TECHNISCHES': 'TECH',
	'TECHNOLOGIES': 'TECH',
	'TECHNOLOGY': 'TECH',
	'TELECOMMUNICACION': 'TELECOM',
	'TELECOMMUNICATION': 'TELECOM',
	'TELECOMMUNICATIONS': 'TELECOM',
	'TELECOMMUNICAZIONI': 'TELECOM',
	'TELECOMUNICAZIONI': 'TELECOM',
	'TRUSTUL': 'TRUST',
	'UNITED KINGDOM': 'UK',
	'UNITED STATES': 'USA',
	'UNITED STATES GOVERNMENT AS REPRESENTED BY THE SECRETARY OF': 'US SEC',
	'UNITED STATES OF AMERICA': 'USA',
	'UNITED STATES OF AMERICA ADMINISTRATOR': 'US ADMIN',
	'UNITED STATES OF AMERICA AS REPRESENTED BY THE ADMINISTRATOR': 'US ADMIN',
	'UNITED STATES OF AMERICA AS REPRESENTED BY THE DEPT': 'US DEPT',
	'UNITED STATES OF AMERICA AS REPRESENTED BY THE SECRETARY': 'US SEC',
	'UNITED STATES OF AMERICA AS REPRESENTED BY THE UNITED STATES DEPT': 'US DEPT',
	'UNITED STATES OF AMERICA REPRESENTED BY THE SECRETARY': 'US SEC',
	'UNITED STATES OF AMERICA SECRETARY OF': 'US SEC',
	'UNITED STATES OF AMERICAN AS REPRESENTED BY THE UNITED STATES DEPT': 'US DEPT',
	'UNITED STATES OF AMERICAS AS REPRESENTED BY THE SECRETARY': 'US SEC',
	'UNITES STATES OF AMERICA AS REPRESENTED BY THE SECRETARY': 'US SEC',
	'UNIVERSIDAD': 'UNIV',
	'UNIVERSIDADE': 'UNIV',
	'UNIVERSITA': 'UNIV',
	'UNIVERSITA DEGLI STUDI': 'UNIV',
	'UNIVERSITAET': 'UNIV',
	'UNIVERSITAIR': 'UNIV',
	'UNIVERSITAIRE': 'UNIV',
	'UNIVERSITAT': 'UNIV',
	'UNIVERSITATEA': 'UNIV',
	'UNIVERSITE': 'UNIV',
	'UNIVERSITEIT': 'UNIV',
	'UNIVERSITET': 'UNIV',
	'UNIVERSITETA': 'UNIV',
	'UNIVERSITETAM': 'UNIV',
	'UNIVERSITETAMI': 'UNIV',
	'UNIVERSITETE': 'UNIV',
	'UNIVERSITETOM': 'UNIV',
	'UNIVERSITETOV': 'UNIV',
	'UNIVERSITETU': 'UNIV',
	'UNIVERSITETY': 'UNIV',
	'UNIVERSITY': 'UNIV',
	'UNIWERSYTET': 'UNIV',
	'UTILAJ': 'UTIL',
	'UTILAJE': 'UTIL',
	'UTILISATION VOLKSEIGENER BETRIEBE': 'VEB',
	'UTILISATIONS VOLKSEIGENER BETRIEBE': 'VEB',
	'VEB KOMBINAT': 'VEB KOMB',
	'VEREENIGDE': 'VER',
	'VEREIN': 'VER',
	'VEREINIGTE VEREINIGUNG': 'VER',
	'VEREINIGTES VEREINIGUNG': 'VER',
	'VEREINIGUNG VOLKSEIGENER BETRIEBUNG': 'VVB',
	'VERENIGING': 'VER',
	'VERWALTUNGEN': 'VERW',
	'VERWALTUNGS': 'VERW',
	'VERWALTUNGSGESELLSCHAFT': 'VERW GES',
	'VERWERTUNGS': 'VERW',
	'VYZK USTAV': 'VU',
	'VYZK VYVOJOVY USTAV': 'VVU',
	'VYZKUMNY USTAV': 'VU',
	'VYZKUMNY VYVOJOVY USTAV': 'VVU',
	'VYZKUMNYUSTAV': 'VU',
	'WERKZEUGMASCHINENFABRIK': 'WERKZ MASCHFAB',
	'WERKZEUGMASCHINENKOMBINAT': 'WERKZ MASCH KOMB',
	'WESTDEUTSCH': 'WESTDEUT',
	'WESTDEUTSCHE': 'WESTDEUT',
	'WESTDEUTSCHER': 'WESTDEUT',
	'WESTDEUTSCHES': 'WESTDEUT',
	'WISSENSCHAFTLICHE(S)': 'WISS',
	'WISSENSCHAFTLICHES TECHNISCHES ZENTRUM': 'WTZ',
	'YUGEN KAISHA': 'YG YUGEN GAISHA',
	'YUUGEN GAISHA': 'YG YUGEN GAISHA',
	'YUUGEN KAISHA': 'YG YUGEN GAISHA',
	'YUUGEN KAISYA': 'YG YUGEN GAISHA',
	'ZAIDAN HOJIN': 'ZH',
	'ZAIDAN HOUJIN': 'ZH',
	'ZAVODU': 'ZAVOD',
	'ZAVODY': 'ZAVOD',
	'ZENTRALE': 'ZENT',
	'ZENTRALEN': 'ZENT',
	'ZENTRALES': 'ZENT',
	'ZENTRALINSTITUT': 'ZENT INST',
	'ZENTRALLABORATORIUM': 'ZENT LAB',
	'ZENTRALNA': 'ZENT',
	'ZENTRUM': 'ZENT'}
	# load data
	with open(path, 'r') as fr:
		lines = fr.readlines()
	i = 0
	new_assignee_name = [[] for i in range(len(lines))]
	patent_id = []
	GrantDate = []
	CountryCode = []
	StateCode = []
	CityCode = []
	Reference = []
	CPCClass = []
	for line in lines:
		assignee_name = line.strip().split('\t')[2].split('+')[0] # extract the first assignee name
		assignee_name = assignee_name.split()
		patent_id.append(line.strip().split('\t')[0])
		GrantDate.append(line.strip().split('\t')[1])
		CountryCode.append(line.strip().split('\t')[3])
		StateCode.append(line.strip().split('\t')[4])
		CityCode.append(line.strip().split('\t')[5])
		Reference.append(line.strip().split('\t')[6])
		CPCClass.append(line.strip().split('\t')[7])
		for part in assignee_name:
			if part.upper() in abbreviations:
				new_assignee_name[i].append(abbreviations[part.upper()])
				continue
			if part.upper() in derwent:
				new_assignee_name[i].append(derwent[part.upper()])
				continue
			if part.upper() in univ:
				new_assignee_name[i].append(univ[part.upper()])
				continue
			if part.upper() not in abbreviations and part not in derwent and part not in univ:
				new_assignee_name[i].append(part.upper())
				continue
		i += 1

	with open('./data/result.std.txt', 'a') as fw:
		for j in range(len(lines)):
			fw.writelines(patent_id[j]+'\t'+GrantDate[j]+'\t'+' '.join(new_assignee_name[j])+'\t'+CountryCode[j]+'\t'+StateCode[j]+'\t'+CityCode[j]+'\t'+Reference[j]+'\t'+CPCClass[j]+'\n')


import argparse

parser = argparse.ArgumentParser(description="Standard assignee names")
parser.add_argument('--path', dest='path', type=str, default='./data/result.txt', help='Specify where to get the data')
args = parser.parse_args()

standardize(args.path)
