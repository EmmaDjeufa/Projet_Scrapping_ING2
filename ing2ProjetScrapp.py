#Library import
import requests
from bs4 import BeautifulSoup
import pandas as pd

tables = []

#The confs list contains lists of links to map and the number of arrays to map for each link.

confs = [
    
    [
        'https://ec.europa.eu/clima/ets/nap.do?languageCode=fr&nap.registryCodeArray=AT&nap.registryCodeArray=BE&nap.registryCodeArray=BG&nap.registryCodeArray=HR&nap.registryCodeArray=CY&nap.registryCodeArray=CZ&nap.registryCodeArray=DK&nap.registryCodeArray=EE&nap.registryCodeArray=EU&nap.registryCodeArray=FI&nap.registryCodeArray=FR&nap.registryCodeArray=DE&nap.registryCodeArray=GR&nap.registryCodeArray=HU&nap.registryCodeArray=IS&nap.registryCodeArray=IE&nap.registryCodeArray=IT&nap.registryCodeArray=LV&nap.registryCodeArray=LI&nap.registryCodeArray=LT&nap.registryCodeArray=LU&nap.registryCodeArray=MT&nap.registryCodeArray=NL&nap.registryCodeArray=XI&nap.registryCodeArray=NO&nap.registryCodeArray=PL&nap.registryCodeArray=PT&nap.registryCodeArray=RO&nap.registryCodeArray=SK&nap.registryCodeArray=SI&nap.registryCodeArray=ES&nap.registryCodeArray=SE&nap.registryCodeArray=&nap.registryCodeArray=GB&periodCode=-1&currentSortSettings=&resultList.currentPageNumber={page_number}&nextList=Next%3E',
        'tblNapSearchResult',
        6,
        2
    ],
    [
        'https://ec.europa.eu/clima/ets/caat.do?languageCode=fr&nap.registryCodeArray=AT&nap.registryCodeArray=BE&nap.registryCodeArray=BG&nap.registryCodeArray=HR&nap.registryCodeArray=CY&nap.registryCodeArray=CZ&nap.registryCodeArray=DK&nap.registryCodeArray=EE&nap.registryCodeArray=EU&nap.registryCodeArray=FI&nap.registryCodeArray=FR&nap.registryCodeArray=DE&nap.registryCodeArray=GR&nap.registryCodeArray=HU&nap.registryCodeArray=IS&nap.registryCodeArray=IE&nap.registryCodeArray=IT&nap.registryCodeArray=LV&nap.registryCodeArray=LI&nap.registryCodeArray=LT&nap.registryCodeArray=LU&nap.registryCodeArray=MT&nap.registryCodeArray=NL&nap.registryCodeArray=XI&nap.registryCodeArray=NO&nap.registryCodeArray=PL&nap.registryCodeArray=PT&nap.registryCodeArray=RO&nap.registryCodeArray=SK&nap.registryCodeArray=SI&nap.registryCodeArray=ES&nap.registryCodeArray=SE&nap.registryCodeArray=&nap.registryCodeArray=GB&periodCode=-1&currentSortSettings=&resultList.currentPageNumber={page_number}&nextList=Next%3E',
        'tblNapSearchResult',
        5,
        2
    ],
    [    
    'https://ec.europa.eu/clima/ets/euSwissCaatInstallationInformation.do?languageCode=en.CurrentPageNumber={page_number}&nextList=Next%3E',
        'tblIntAllocList',
        1,
        1
    ],
    [
        'https://ec.europa.eu/clima/ets/swissEuCaat.do?languageCode=fr&intAlloc.registryCodeArray=-1&intAlloc.registryCodeArray=AT&intAlloc.registryCodeArray=BE&intAlloc.registryCodeArray=BG&intAlloc.registryCodeArray=HR&intAlloc.registryCodeArray=CZ&intAlloc.registryCodeArray=DK&intAlloc.registryCodeArray=EE&intAlloc.registryCodeArray=FI&intAlloc.registryCodeArray=FR&intAlloc.registryCodeArray=DE&intAlloc.registryCodeArray=GR&intAlloc.registryCodeArray=HU&intAlloc.registryCodeArray=IS&intAlloc.registryCodeArray=IE&intAlloc.registryCodeArray=IT&intAlloc.registryCodeArray=LV&intAlloc.registryCodeArray=LU&intAlloc.registryCodeArray=MT&intAlloc.registryCodeArray=NL&intAlloc.registryCodeArray=NO&intAlloc.registryCodeArray=PL&intAlloc.registryCodeArray=PT&intAlloc.registryCodeArray=RO&intAlloc.registryCodeArray=ES&intAlloc.registryCodeArray=SE&intAlloc.registryCodeArray=&intAlloc.registryCodeArray=GB&currentSortSettings=&resultList.currentPageNumber={page_number}&nextList=Next%3E',
        'tblIntAllocSearchResult',
        3,
        2
    ],
    [
        "https://ec.europa.eu/clima/ets/allocationCompliance.do?languageCode=en&registryCode=-1&periodCode=-1&search=Search.CurrentPageNumber={page_number}-&nextList=Next%3E',",
        "tblCommitmentPeriodList",
        8,
        1
    ],
    [
        'https://ec.europa.eu/clima/ets/oha.do?form=oha&languageCode=fr&account.registryCodes=AT&account.registryCodes=BE&account.registryCodes=BG&account.registryCodes=HR&account.registryCodes=CY&account.registryCodes=CZ&account.registryCodes=DK&account.registryCodes=EE&account.registryCodes=EU&account.registryCodes=FI&account.registryCodes=FR&account.registryCodes=DE&account.registryCodes=GR&account.registryCodes=HU&account.registryCodes=IS&account.registryCodes=IE&account.registryCodes=IT&account.registryCodes=LV&account.registryCodes=LI&account.registryCodes=LT&account.registryCodes=LU&account.registryCodes=MT&account.registryCodes=NL&account.registryCodes=XI&account.registryCodes=NO&account.registryCodes=PL&account.registryCodes=PT&account.registryCodes=RO&account.registryCodes=SK&account.registryCodes=SI&account.registryCodes=ES&account.registryCodes=SE&account.registryCodes=&account.registryCodes=GB&accountHolder=&installationIdentifier=&installationName=&permitIdentifier=&mainActivityType=-1&account.complianceStatusArray=0&account.complianceStatusArray=-&account.complianceStatusArray=A&account.complianceStatusArray=B&account.complianceStatusArray=C&account.complianceStatusArray=D&account.complianceStatusArray=E&account.complianceStatusArray=X&searchType=oha&currentSortSettings=&resultList.currentPageNumber={page_number}&nextList=Next%3E',
        "tblAccountSearchResult",
        2101,
        1
    ],
    [
        'https://ec.europa.eu/clima/ets/oha.do?form=oha&languageCode=fr&account.registryCodes=AT&account.registryCodes=BE&account.registryCodes=BG&account.registryCodes=HR&account.registryCodes=CY&account.registryCodes=CZ&account.registryCodes=DK&account.registryCodes=EE&account.registryCodes=EU&account.registryCodes=FI&account.registryCodes=FR&account.registryCodes=DE&account.registryCodes=GR&account.registryCodes=HU&account.registryCodes=IS&account.registryCodes=IE&account.registryCodes=IT&account.registryCodes=LV&account.registryCodes=LI&account.registryCodes=LT&account.registryCodes=LU&account.registryCodes=MT&account.registryCodes=NL&account.registryCodes=XI&account.registryCodes=NO&account.registryCodes=PL&account.registryCodes=PT&account.registryCodes=RO&account.registryCodes=SK&account.registryCodes=SI&account.registryCodes=ES&account.registryCodes=SE&account.registryCodes=&account.registryCodes=GB&accountHolder=&installationIdentifier=&installationName=&permitIdentifier=&mainActivityType=-1&account.complianceStatusArray=0&account.complianceStatusArray=-&account.complianceStatusArray=A&account.complianceStatusArray=B&account.complianceStatusArray=C&account.complianceStatusArray=D&account.complianceStatusArray=E&account.complianceStatusArray=X&searchType=oha&currentSortSettings=&resultList.currentPageNumber={page_number}&nextList=Next%3E',
        "tblAccountSearchResult",
        898,
        1
    ],
    [    
    'https://ec.europa.eu/clima/ets/transactionsEntitlements.do?languageCode=fr&startDate=&endDate=&transactionStatusCode=4&transactionId=&suppTransactionTypeCode=-1&transferringEsdRegistryCode=-1&acquiringEsdRegistryCode=-1&transferringEsdYear=&acquiringEsdYear=&search=Search&egistryCodeArray=GB&periodCode=-1&currentSortSettings=&resultList.CurrentPageNumber={page_number}&nextList=Next%3E',
        'tblTransactionSearchResult',
        58526,
        1
    ],
    [    
    'https://ec.europa.eu/clima/ets/ice.do?languageCode=en&registryCode=-1&accountFullTypeCode=-1&iceInstallationId=&search=Search&currentSortSettings=.CurrentPageNumber={page_number}&nextList=Next%3E',
        'tblEntitlements',
        899,
        1
    ],
    [    
    'https://ec.europa.eu/clima/ets/registryHoldings.do?languageCode=en&search=Search.CurrentPageNumber={page_number}&nextList=Next%3E',
        'tblRegistryHoldings',
        1,
        1
    ],
    [    
    'https://ec.europa.eu/clima/ets/swissAllowancesTransacted.do?languageCode=en&search=Search.CurrentPageNumber={page_number}&nextList=Next%3E',
        'tblRegistryHoldings',
        1,
        1
    ]
]

#Conf_number allows you to select the link you want to trap
conf_number = 2

#Extract the URL of the web page containing the information to be retrieved;
URL = confs[conf_number][0]

#extract the ID of the HTML table containing the data 
table_id = confs[conf_number][1]

#extract the number of pages required to retrieve all conference data.
number_of_pages = confs[conf_number][2]

#identifies table column headers to avoid repeating them in the .csv file
header_position = confs[conf_number][3]


#The create_all_links function returns a list containing all generated links.
def create_all_links(url, number_of_pages):
    links = []
    for page_number in range(number_of_pages):
        links.append(url.format(page_number = page_number))
    return links
    
    
#The function finally returns the table contents as a BeautifulSoup object.
def parse_table(link, table_id):
    response = requests.get(link)
    soup = BeautifulSoup(response.content, 'html.parser')
    table = soup.find('table', {'id': table_id})
    return table

#function retrieves data in a .csv file
def construct_csv(url, number_of_pages, table_id, header_position):
    links = create_all_links(url, number_of_pages)
    tables = []
    for page_number, link in enumerate(links):
        print("[I] Parsing page number:", page_number+1)
        tables.append(parse_table(link, table_id))
    
    if len(tables) != 0:
        # -------------------- Header --------------------------------
        header_items = []
        header = tables[0].find_all("tr")[header_position]
        
        for items in header:
            try:
                header_items.append(items.get_text().strip()) if items.get_text().strip() != '' else ''
            except:
                continue

        # ---------------------- Tables data -------------------------
        data = []
        for table in tables:
            rows = table.find_all("tr")[header_position+1:]
            table_data = []
            for row in rows:
                row_data = []
                cells = row.findAll("td", {'class': 'bgcelllist'})
                for cell in cells:
                    try:
                        row_data.append(cell.get_text().strip()) if cell.get_text().strip() != '' else ''
                    except:
                        continue
                table_data.append(row_data) if len(row_data) != 0 else ''
            data.extend(table_data)
        
        dataFrame = pd.DataFrame(data = data, columns = header_items[:-1])
        print("[I] Generating CSV...")
        dataFrame.to_csv('result7.csv')

    else: 
        raise Exception ("No table found")


print("[I] Starting scraping operation...")
print("[I] URL:", URL.format(page_number = 0))
print("[I] Number of pages:", number_of_pages)

construct_csv(URL, number_of_pages, table_id, header_position)

print("[I] Done.")


# https://ec.europa.eu/clima/ets/emissionsOverview.do



